class CartPage:
    def __init__(self, page):
        self.page = page
        self.backpack_item = page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Backpack")

    def is_backpack_visible(self):
        return self.backpack_item.is_visible()
