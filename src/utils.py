import requests
import shutil
import json
import urllib.request
import io
import os
from collections import Counter
from config import API_KEY
from PIL import Image


API_URL = "https://api.api-ninjas.com/v1/dogs?"


def get_matched_breeds(quiz_input: dict, n=2):
    """
    Takes dog quiz input from users and number of matched breeds
    Returns a dict of specified number of breeds and its image url

    # Quiz input example
    quiz_input = {
        "shedding": 3,
        "barking": 1,
        "energy": 3,
        "protectiveness": 3,
        "trainability": 5,
    }
    """
    matched_breeds = dict()

    # Pass all quiz options to API request
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params=quiz_input,
    )

    if response.status_code == requests.codes.ok:
        # Loop over results from API response and store only the name of breed in a list
        for breed in response.json()[:n]:
            breed = dict(breed)
            breed_name = breed["name"]
            download_dog_image(breed_name)
            matched_breeds[breed_name] = f"static/img/{breed_name}.jpg"

    # Return matched breeds if there is one perfect match or above
    if matched_breeds:
        return matched_breeds

    # Otherwise find the compatible breeds
    candidates = []

    # Pass each quiz option at a time to API request and store matched breeds in a list
    for option, score in quiz_input.items():
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={option: score},
        )
        if response.status_code == requests.codes.ok:
            for breed in response.json():
                breed = dict(breed)
                breed_name = breed["name"]
                candidates.append(breed_name)

    # Find the compatible breeds
    candidates_count = Counter(candidates).most_common(n)
    if candidates_count:
        compatible_breeds = dict()
        for breed, count in candidates_count:
            download_dog_image(breed)
            compatible_breeds[breed] = f"static/img/{breed}.jpg"
        return compatible_breeds

    # Return a cat-person message and a cat image if no breeds matched
    return {"You're a Cat Person🐱": "static/img/cat-white-wall.jpg"}


def download_dog_image(breed: str):
    """
    Takes a name of breed and saves its image to static/img
    """
    image_path = f"static/img/{breed}.jpg"

    # Checks if the image has been downloaded before
    if not os.path.isfile(image_path):
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"name": breed},
        )
        if response.status_code == requests.codes.ok:
            image_url = dict(response.json()[0])["image_link"]

            # Retrieve image from url to static/img
            r = requests.get(image_url, stream=True)
            if r.status_code == 200:
                with open(image_path, "wb") as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

            img = Image.open(image_path)
            data = io.BytesIO()
            img.save(data, "JPEG")
