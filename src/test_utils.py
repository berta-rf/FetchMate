from unittest import TestCase, main
from src.utils import get_matched_breeds


class TestMatchedBreeds(TestCase):
    def test_get_matched_breeds(self):
        quiz_inputs = {
            "shedding": 4,
            "barking": 1,
            "energy": 3,
            "protectiveness": 3,
            "trainability": 5
        }
        self.assertEqual(get_matched_breeds(quiz_inputs), {"Golden Retriever": "static/img/Golden Retriever.jpg"})


if __name__ == "__main__":
    main()
