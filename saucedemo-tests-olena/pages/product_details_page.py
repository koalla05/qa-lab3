class ProductDetailsPage:
    def __init__(self, page):
        self.page = page
        self.product_name = page.locator('[data-test="inventory-item-name"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')
        self.product_description = page.locator('[data-test="inventory-item-desc"]')
        # if there is no specific product image locator, we can use a more general locator that matches any product image
        self.product_image = page.locator('[data-test="item-sauce-labs-backpack-img"], [data-test^="item-"][data-test$="-img"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def get_product_image_src(self):
        return self.product_image.get_attribute("src")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def open_cart(self):
        self.cart_link.click()
