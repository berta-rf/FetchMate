from unittest import TestCase, main
from src.utils import get_matched_breeds


class TestMatchedBreeds(TestCase):

    def test_perfect_matches(self):
        quiz_input = {
            "shedding": 3,
            "barking": 1,
            "energy": 3,
            "protectiveness": 3,
            "trainability": 5,
        }
        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "Affenpinscher": f"static/img/Affenpinscher.jpg",
            "Appenzeller Sennenhund": f"static/img/Appenzeller Sennenhund.jpg"
        }
        self.assertEqual(result, expected)

    def test_no_matches(self):

        quiz_input = {
            "shedding": 0,
            "barking": 0,
            "energy": 0,
            "protectiveness": 0,
            "trainability": 0,
        }
        result = get_matched_breeds(quiz_input, n=2)
        expected = {
            "You're a Cat Person🐱": "static/img/cat-white-wall.jpg"
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()



