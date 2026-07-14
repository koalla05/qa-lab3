import re

from playwright.sync_api import expect, sync_playwright

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage


def test_problem_user_can_add_backpack_to_cart_from_product_page():
    with sync_playwright() as playwright: # "with" is for context management to ensure proper cleanup of resources
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        try:
            page = browser.new_page()

            login_page = LoginPage(page)
            inventory_page = InventoryPage(page)
            product_details_page = ProductDetailsPage(page)
            cart_page = CartPage(page)

            login_page.navigate()
            login_page.login("problem_user", "secret_sauce")

            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
            expected_product_name = inventory_page.get_backpack_name()

            inventory_page.open_backpack_details()

            expect(page).to_have_url(re.compile(r".*/inventory-item\.html\?id=\d+"))
            actual_product_name = product_details_page.product_name.inner_text()

            product_details_page.add_to_cart()

            errors = []
            if actual_product_name != expected_product_name:
                errors.append(
                    f"Expected to open '{expected_product_name}', "
                    f"but opened '{actual_product_name}'."
                )

            if product_details_page.cart_badge.count() == 0:
                errors.append("Expected cart badge to display '1', but badge is missing.")
            elif product_details_page.cart_badge.inner_text() != "1":
                errors.append(
                    f"Expected cart badge to display '1', "
                    f"but it displays '{product_details_page.cart_badge.inner_text()}'."
                )

            product_details_page.open_cart()

            expect(page).to_have_url("https://www.saucedemo.com/cart.html")
            if not cart_page.is_backpack_visible():
                errors.append(f"Expected '{expected_product_name}' to be present in the cart.")

            if errors:
                raise AssertionError("\n".join(errors))
        finally: # to ensure that the browser is closed even if an error occurs
            browser.close()
