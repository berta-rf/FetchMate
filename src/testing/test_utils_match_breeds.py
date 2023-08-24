from unittest import TestCase, main
from unittest.mock import patch
import os
from src.utils import get_matched_breeds


class TestMatchedBreeds(TestCase):

    @patch("utils.download_dog_image")  # creates a mock of download_dog_image
    def test_perfect_matches(self, mock_download_dog_image):
        quiz_input = dict(shedding=3, barking=1, energy=3, protectiveness=3, trainability=5)

        mock_download_dog_image.return_value.status_code = 200  # returns a successful HTTP response
        mock_download_dog_image.return_value = [dict(name="Affenpinscher"), dict(name="Appenzeller Sennenhund")]

        # Set up the environment variable for image paths
        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.environ["DOG_IMAGE_PATH"] = os.path.join(project_directory, "static", "img")

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Affenpinscher": "static/img/Affenpinscher.jpg",
            "Appenzeller Sennenhund": "static/img/Appenzeller Sennenhund.jpg"
        }

        self.assertEqual(result, expected)

        # Clean up the environment variable after the test
        del os.environ["DOG_IMAGE_PATH"]

    @patch("utils.download_dog_image")
    def test_perfect_matches_edge_case1(self, mock_download_dog_image):
        quiz_input = dict(shedding=1, barking=1, energy=1, protectiveness=1, trainability=1)

        mock_download_dog_image.return_value.status_code = 200
        mock_download_dog_image.return_value = [dict(name="Afghan Hound"), dict(name="Bergamasco Sheepdog")]

        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.environ["DOG_IMAGE_PATH"] = os.path.join(project_directory, "static", "img")

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Afghan Hound": "static/img/Afghan Hound.jpg",
            "Bergamasco Sheepdog": "static/img/Bergamasco Sheepdog.jpg"
        }
        self.assertEqual(result, expected)

        del os.environ["DOG_IMAGE_PATH"]

    @patch("utils.download_dog_image")
    def test_perfect_matches_edge_case2(self, mock_download_dog_image):

        quiz_input = dict(shedding=5, barking=5, energy=5, protectiveness=5, trainability=5)

        mock_download_dog_image.return_value.status_code = 200
        mock_download_dog_image.return_value = [dict(name="Barbado da Terceira"), dict(name="Doberman Pinscher")]

        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.environ["DOG_IMAGE_PATH"] = os.path.join(project_directory, "static", "img")

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Barbado da Terceira": "static/img/Barbado da Terceira.jpg",
            "Doberman Pinscher": "static/img/Doberman Pinscher.jpg"
        }
        self.assertEqual(result, expected)

        del os.environ["DOG_IMAGE_PATH"]

    def test_no_matches(self):

        quiz_input = dict(shedding=0, barking=0, energy=0, protectiveness=0, trainability=0)

        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "You're a Cat Person🐱": "static/img/cat-white-wall.jpg"
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
