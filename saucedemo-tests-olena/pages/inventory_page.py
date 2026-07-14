class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.backpack_title = page.locator('[data-test="item-4-title-link"]')
        self.backpack_price = page.locator('[data-test="inventory-item-price"]').first
        self.backpack_image = page.locator('[data-test="inventory-item-sauce-labs-backpack-img"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def open_backpack_details(self):
        self.backpack_title.click()

    def get_backpack_name(self):
        return self.backpack_title.inner_text()

    def get_backpack_price(self):
        return self.backpack_price.inner_text()

    def get_backpack_image_src(self):
        return self.backpack_image.get_attribute("src")

    def open_cart(self):
        self.cart_link.click()
