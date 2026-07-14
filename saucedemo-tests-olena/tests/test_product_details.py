import re

from playwright.sync_api import expect, sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage


def test_product_details_consistency_for_problem_user():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        try:
            page = browser.new_page()

            login_page = LoginPage(page)
            inventory_page = InventoryPage(page)
            product_details_page = ProductDetailsPage(page)

            login_page.navigate()
            login_page.login("problem_user", "secret_sauce")

            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
            expect(inventory_page.backpack_title).to_be_visible()
            expect(inventory_page.backpack_price).to_be_visible()
            expect(inventory_page.backpack_image).to_be_visible()

            inventory_backpack_name = inventory_page.get_backpack_name()
            inventory_backpack_price = inventory_page.get_backpack_price()
            inventory_backpack_image_src = inventory_page.get_backpack_image_src()

            inventory_page.open_backpack_details()

            expect(page).to_have_url(re.compile(r".*/inventory-item\.html\?id=\d+"))

            actual_product_name = product_details_page.product_name.inner_text()
            actual_product_price = product_details_page.product_price.inner_text()
            actual_description_visible = product_details_page.product_description.is_visible()
            actual_image_visible = product_details_page.product_image.is_visible()
            actual_image_src = product_details_page.get_product_image_src()

            # store errors in a list to report all of them at once without stopping the test at the first failure
            errors = []
            if actual_product_name != inventory_backpack_name:
                errors.append(
                    f"Expected product name '{inventory_backpack_name}', "
                    f"but opened '{actual_product_name}'."
                )
            if actual_product_price != inventory_backpack_price:
                errors.append(
                    f"Expected product price '{inventory_backpack_price}', "
                    f"but opened '{actual_product_price}'."
                )
            if not actual_description_visible:
                errors.append("Expected product description to be visible.")
            if not actual_image_visible:
                errors.append("Expected product image to be visible.")
            if actual_image_src != inventory_backpack_image_src:
                errors.append(
                    f"Expected product image src '{inventory_backpack_image_src}', "
                    f"but opened image src '{actual_image_src}'."
                )

            if errors:
                raise AssertionError("\n".join(errors))
        finally:
            browser.close()
