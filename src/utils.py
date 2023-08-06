import requests
import json
from collections import Counter
from config import API_KEY

API_URL = "https://api.api-ninjas.com/v1/dogs?"


def get_matched_breeds(quiz_input: dict, n=3):
    """
    Takes dog quiz input from users and number of matched breeds
    Returns a list of specified number of breeds

    # Quiz inputs example
    quiz_inputs = {
        "shedding": 3,
        "barking": 1,
        "energy": 3,
        "protectiveness": 3,
        "trainability": 5,
        "min_life_expectancy": 6,  # 6 is the shortest minimum lifespan,
        "max_weight_male":
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
        return matched_breeds

    # Otherwise find a most compatible breed
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
    Takes a name of breed and returns its image link
    """
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": breed},
    )
    if response.status_code == requests.codes.ok:
        return dict(response.json()[0])["image_link"]
