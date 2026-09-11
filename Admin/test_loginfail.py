from playwright.sync_api import Page, expect
def test_login_invalid(page: Page):
    page.goto("https://automationintesting.online/")
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").fill("cutarescutest")
    page.get_by_role("textbox", name="Password").fill("cutarescutest123")
    page.get_by_role("button", name="Login").click()
    mesaj_eroare = page.get_by_text("Invalid credentials")
    expect(mesaj_eroare).to_be_visible()
    print("\nValidare QA: Sistemul a respins corect datele de login invalide!")