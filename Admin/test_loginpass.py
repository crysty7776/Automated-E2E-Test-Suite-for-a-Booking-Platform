from playwright.sync_api import Page, expect
import re
def test_login_pass(page: Page):
    page.goto("https://automationintesting.online/")  
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    mesaj_screen = page.get_by_text(re.compile(r"logout", re.IGNORECASE))
    expect(mesaj_screen).to_be_visible()
    
    print("\nValidare QA: Login pass")