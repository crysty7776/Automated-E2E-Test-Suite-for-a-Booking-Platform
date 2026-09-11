import re
import random
from playwright.sync_api import Page, expect


def test_room(page: Page):
    page.goto("https://automationintesting.online/")
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Rooms").click()
    tipuri_rf = ["WiFi", "TV", "Radio", "Refreshments", "Safe"]
    tip_rf = random.choice(tipuri_rf)
    tipuri_camere = ["Single", "Double", "Twin", "Family", "Suite"]
    tip_nou = random.choice(tipuri_camere)
    pret_nou = str(random.randint(50, 350))
    descriere_noua = f"Test QA {random.randint(1000, 9999)}"
    toate_camerele = page.locator("[id^='room']")
    toate_camerele.first.wait_for(state="visible")
    numar_total_camere = toate_camerele.count()
    index_ales = random.randint(0, numar_total_camere - 1)
    page.wait_for_timeout(1000)
    toate_camerele.nth(index_ales).click()
    page.get_by_role("button", name="Edit").click()
    page.get_by_label("Type:").select_option(tip_nou)
    page.get_by_role("textbox", name="Room price:").fill(pret_nou)
    if page.get_by_role("checkbox", name=tip_rf).is_checked():
        page.get_by_role("checkbox", name=tip_rf).uncheck()
    else:
        page.get_by_role("checkbox", name=tip_rf).check()

    page.get_by_role("textbox", name="Description").fill(descriere_noua)
    page.get_by_role("button", name="Update").click()
    expect(page.locator("body")).to_contain_text(descriere_noua)
    print(f"\nValidare QA: A fost editata camera cu indexul {index_ales}. Setari: {tip_nou} / Preț {pret_nou}")