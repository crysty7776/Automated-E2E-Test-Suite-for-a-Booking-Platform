import random
from playwright.sync_api import Page, expect
def test_room(page: Page):
    page.goto("https://automationintesting.online/")
    page.get_by_role("link", name="Cookie-Policy").click()
    page.goto("https://automationintesting.online/")
    mesaj_succes = page.get_by_text("Welcome to Shady Meadows B&B")
    expect(mesaj_succes).to_be_visible()
    print("\nValidare QA: Pass validare policy")