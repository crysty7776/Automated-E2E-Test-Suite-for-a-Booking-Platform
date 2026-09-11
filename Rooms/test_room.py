from playwright.sync_api import Page, expect
from datetime import datetime, timedelta


def test_room(page: Page):
    data_checkin = datetime.now() + timedelta(days=3)
    data_checkout = datetime.now() + timedelta(days=6)
    page.goto("https://automationintesting.online/")
    page.locator("#navbarNav").get_by_role("link", name="Rooms").click()
    page.get_by_role("textbox").first.click()
    page.get_by_role("gridcell", name="Choose Thursday, 27 August").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("gridcell", name="Choose Sunday, 30 August").click()
    page.get_by_role("button", name="Check Availability").click()
    page.get_by_role("link", name="Book now").nth(2).click()
    page.get_by_role("button", name="Reserve Now").click()
    page.get_by_role("textbox", name="Firstname").click()
    page.get_by_role("textbox", name="Firstname").fill("612436136")
    page.get_by_role("textbox", name="Lastname").click()
    page.get_by_role("textbox", name="Firstname").fill("6124361361")
    page.get_by_role("textbox", name="Lastname").fill("361361")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("hadshasd@gmail.com")
    page.get_by_role("textbox", name="Phone").click()
    page.get_by_role("textbox", name="Phone").fill("7214712613636")
    page.get_by_role("button", name="Reserve Now").click()
    mesaj_succes = page.get_by_text("Booking Confirmed")
    expect(mesaj_succes).to_be_visible()
    print("\nValidare QA: Rezervarea a fost confirmată cu succes!")