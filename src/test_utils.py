from unittest import TestCase, main
from unittest.mock import patch
from src import utils
from utils import get_matched_breeds, download_dog_image, requests


class TestMatchedBreeds(TestCase):

    @patch("utils.download_dog_image")
    def test_perfect_matches(self, mock_download_dog_image):
        quiz_input = dict(shedding=3, barking=1, energy=3, protectiveness=3, trainability=5)

        mock_download_dog_image.return_value.status_code = 200
        mock_download_dog_image.return_value = [dict(name="Affenpinscher"), dict(name="Appenzeller Sennenhund")]

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Affenpinscher": f"static/img/Affenpinscher.jpg",
            "Appenzeller Sennenhund": f"static/img/Appenzeller Sennenhund.jpg"
        }
        self.assertEqual(result, expected)

        quiz_input = dict(shedding=1, barking=1, energy=1, protectiveness=1, trainability=1)

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Afghan Hound": f"static/img/Afghan Hound.jpg",
            "Bergamasco Sheepdog": f"static/img/Bergamasco Sheepdog.jpg"
        }
        self.assertEqual(result, expected)

        quiz_input = dict(shedding=5, barking=5, energy=5, protectiveness=5, trainability=5)
        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Barbado da Terceira": "static/img/Barbado da Terceira.jpg",
         "Doberman Pinscher": "static/img/Doberman Pinscher.jpg"
        }
        self.assertEqual(result, expected)

    def test_no_matches(self):

        quiz_input = dict(shedding=0, barking=0, energy=0, protectiveness=0, trainability=0)

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "You're a Cat Person🐱": "static/img/cat-white-wall.jpg"
        }
        self.assertEqual(result, expected)


# need testing for download_dog_image

# if __name__ == '__main__':
#     main()



