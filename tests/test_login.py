from playwright.sync_api import Page, expect

def test_login(page: Page):
    
    #open the login page
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    expect(page.get_by_text("Products",exact=True)).to_be_visible()
    
def test_login_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service",exact=True)).to_be_visible()
    expect(page.get_by_role("button",name="Login")).to_be_visible()