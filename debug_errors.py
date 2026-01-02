from playwright.sync_api import sync_playwright

def check_error_messages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        
        # Test locked out user
        page.fill("#user-name", "locked_out_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        error = page.locator("[data-test='error']").text_content()
        print(f"Locked out user: {error}")
        
        # Clear and test invalid password
        page.fill("#user-name", "standard_user")
        page.fill("#password", "wrong")
        page.click("#login-button")
        error = page.locator("[data-test='error']").text_content()
        print(f"Invalid password: {error}")
        
        # Clear and test empty username
        page.fill("#user-name", "")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        error = page.locator("[data-test='error']").text_content()
        print(f"Empty username: {error}")
        
        # Clear and test empty password
        page.fill("#user-name", "standard_user")
        page.fill("#password", "")
        page.click("#login-button")
        error = page.locator("[data-test='error']").text_content()
        print(f"Empty password: {error}")
        
        browser.close()

if __name__ == "__main__":
    check_error_messages()