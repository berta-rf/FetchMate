import requests
import json
from collections import Counter
from config import API_KEY

API_URL = "https://api.api-ninjas.com/v1/dogs?"


def get_matched_breeds(quiz_input: dict, n=1):
    """
    Takes dog quiz input from users and number of matched breeds (default is 1)
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
    matched_breeds = []

    # Pass all quiz options to API request
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params=quiz_input,
    )

    if response.status_code == requests.codes.ok:
        # Loop over results from API response and store only the name of breed in a list
        for breed in response.json():
            breed = dict(breed)
            matched_breeds.append(breed["name"])

    # Return matched breeds if there is one perfect match or above
    if matched_breeds:
        return matched_breeds[:n]

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
                candidates.append(breed["name"])

    # Find the compatible breeds
    candidates_count = Counter(candidates).most_common(n)
    compatible_breeds = [breed for breed, count in candidates_count]
    return compatible_breeds


def get_dog_image(breed: str):
    """
    Takes a name of breed and returns its image url
    """
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": breed},
    )
    if response.status_code == requests.codes.ok:
        return dict(response.json()[0])["image_link"]
