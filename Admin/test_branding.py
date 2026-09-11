import random
import string
from playwright.sync_api import Page, expect
def test_room(page: Page):
    page.goto("https://automationintesting.online/")
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(1000)
    page.get_by_role("link", name="Branding").click()
    litere_aleatorii = ''.join(random.choices(string.ascii_letters, k=6))
    Nume_nou = f"TestQA {litere_aleatorii}"
    page.get_by_role("textbox", name="Enter B&B name").fill(Nume_nou)
    page.get_by_role("textbox", name="Enter image url").click()
    page.get_by_role("textbox", name="Enter image url").fill("https://automationintesting.online/images/rbp-logo.jpg")
    page.get_by_role("button", name="Submit").click()
    mesaj_succes = page.get_by_text("Branding updated!")
    expect(mesaj_succes).to_be_visible()
    print("\nValidare QA: brainding salvat")
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="Report").click()
    page.get_by_role("link", name="Branding").click()
    camp_nume = page.get_by_role("textbox", name="Enter B&B name")
    expect(camp_nume).to_have_value(Nume_nou)
    print("\nValidare QA: brainding vizibil in report")