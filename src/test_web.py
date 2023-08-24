import pytest
from app import test_app
from playwright.sync_api import sync_playwright, expect

BASE_URL = "http://localhost:5001"


# Tests Start Quiz button redirects to Quiz page
@pytest.mark.usefixtures("test_app")
def test_start_quiz(test_app):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        page.click("#hero_button")

        assert page.url == f"{BASE_URL}/quiz"

        context.close()
        browser.close()


# Tests about link in navbar redirects to About page
@pytest.mark.usefixtures("test_app")
def test_open_about(test_app):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        page.click(".aboutlink")
        assert page.url == f"{BASE_URL}/about/"

        context.close()
        browser.close()


# Tests breed results cards show the right breed name
@pytest.mark.usefixtures("test_app")
def test_correct_breed_name_shown(test_app):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(f"{BASE_URL}/quiz")

        page.get_by_text("No shedding at all, please!").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text("Silence is golden with a dog.").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text(
            "Couch potato mode, please! Let's set a new record for belly rubs."
        ).click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text(
            "I'd rather avoid training challenges. Canine college dropout here!"
        ).click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text("I prefer a more easygoing, less protective pal.").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text("Twice a day runs are my thing!").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text(
            "I'm okay with drool, but not a swimming pool's worth."
        ).click()
        page.get_by_role("button", name="Next").click()
        page.get_by_text(
            "Absolutely! I'd love a breed that's a social butterfly and enjoys playdates."
        ).click()

        page.goto(
            f"{BASE_URL}/results?shedding=5&barking=5&playfulness=5&trainability=5&protectiveness=4&energy=1&drooling=1&good_with_other_dogs=1"
        )

        result_1 = page.locator(".card-text").nth(0)
        result_2 = page.locator(".card-text").nth(1)

        expect(result_1).to_contain_text("1. Australian Terrier")
        expect(result_2).to_contain_text("2. Barbado da Terceira")

        context.close()
        browser.close()


# Tests breed name from results links to corresponding breed kennel club page
@pytest.mark.usefixtures("test_app")
def test_breed_akc_links(test_app):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            f"{BASE_URL}/results?shedding=1&barking=5&playfulness=4&trainability=3&protectiveness=3&energy=4&drooling=5&good_with_other_dogs=5"
        )

        # American Foxhound
        page.get_by_text("American Foxhound").click()

        assert page.url == "https://www.akc.org/dog-breeds/american-foxhound/"

        context.close()
        browser.close()
