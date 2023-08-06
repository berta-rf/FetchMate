import requests
import json
from collections import Counter


# To hide api key?
API_KEY = "ksc1s4R35m4sMTnY5VmHhQ==aAfj6NgzuUGtlmIn"
API_URL = "https://api.api-ninjas.com/v1/dogs?"

# Quiz inputs example
quiz_inputs = {
    "shedding": 3,
    "barking": 1,
    "energy": 3,
    "protectiveness": 3,
    "trainability": 5,
    "min_life_expectancy": 6,  # 6 is the shortest minimum lifespan
}

"""
which describes better for size?
    "max_height_male":
    "max_weight_male":
"""


def matched_breeds(quiz_input: dict):
    """
    Takes dog quiz input from users and returns a list of breeds
    """
    matched_candidates = []

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
            matched_candidates.append(breed["name"])

    # Return matched breeds if there is one perfect match or above
    if matched_candidates:
        return matched_candidates

    # Otherwise find a most compatible breed
    possible_candidates = []

    # Pass each quiz option at a time to API request and store matched breeds in a list
    for option, score in quiz_inputs.items():
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={option: score},
        )
        if response.status_code == requests.codes.ok:
            for breed in response.json():
                breed = dict(breed)
                possible_candidates.append(breed["name"])

    # Find the most compatible breed
    most_compatible_breed = Counter(possible_candidates).most_common(1)[0][0]
    return [most_compatible_breed]


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
