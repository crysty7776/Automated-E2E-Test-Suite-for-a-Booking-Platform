from playwright.sync_api import Page, expect


def test_room(page: Page):
    page.goto("https://automationintesting.online/")
    page.get_by_test_id("ContactName").click()
    page.get_by_test_id("ContactName").press("CapsLock")
    page.get_by_test_id("ContactName").fill("T")
    page.get_by_test_id("ContactName").press("CapsLock")
    page.get_by_test_id("ContactName").fill("Test613")
    page.get_by_test_id("ContactEmail").click()
    page.get_by_test_id("ContactEmail").fill("test613613@yahoo.com")
    page.get_by_test_id("ContactPhone").click()
    page.get_by_test_id("ContactPhone").fill("724724616714")
    page.get_by_test_id("ContactSubject").click()
    page.get_by_test_id("ContactSubject").fill("dasfhfstest")
    page.get_by_test_id("ContactDescription").click()
    page.get_by_test_id("ContactDescription").fill("83583564shsdfgsdftesttt")
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Thanks for getting in touch Test613!We'll get back to you aboutdasfhfstestas").click()
    mesaj_succes = page.get_by_text("Thanks for getting in touch")
    expect(mesaj_succes).to_be_visible()
    print("\nValidare QA: mesajul a fost trimis!")