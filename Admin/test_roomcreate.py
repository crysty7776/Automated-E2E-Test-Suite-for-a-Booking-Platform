import random
from playwright.sync_api import Page, expect
def test_room(page: Page):
    page.goto("https://automationintesting.online/")
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Rooms").click()
    nume_camera = str(random.randint(100, 999))
    page.get_by_test_id("roomName").fill(nume_camera)
    page.locator("#roomPrice").fill(str(random.randint(50, 500)))
    optiuni_tip = page.locator("#type option").all_inner_texts()
    tip_ales = random.choice(optiuni_tip)
    page.locator("#type").select_option(tip_ales)
    optiuni_acc = page.locator("#accessible option").all_inner_texts()
    acc_ales = random.choice(optiuni_acc)
    page.locator("#accessible").select_option(acc_ales)
    toate_checkboxurile = page.get_by_role("checkbox")
    numar_checkboxuri = toate_checkboxurile.count()
    for i in range(numar_checkboxuri):
        if random.choice([True, False]):
            toate_checkboxurile.nth(i).check()
    page.get_by_role("button", name="Create").click()
    expect(page.get_by_text(nume_camera)).to_be_visible()
    print(f"\nCamera creata cu tipul {tip_ales} si accesibilitate {acc_ales}.")