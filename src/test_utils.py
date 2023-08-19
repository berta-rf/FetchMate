from unittest import TestCase, main
from unittest.mock import patch

from src.utils import get_matched_breeds


class TestMatchedBreeds(TestCase):

    @patch('requests.get')
    def test_no_matches(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        quiz_input = {
            "shedding": 1,
            "barking": 1,
            "energy": 1,
            "protectiveness": 1,
            "trainability": 1,
        }
        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "You're a Cat Person🐱": "static/img/cat-white-wall.jpg"
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
