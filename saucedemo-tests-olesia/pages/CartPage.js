class CartPage {
  constructor(page) {
    this.page = page;
    this.itemNames = page.locator('[data-test="inventory-item-name"]');
    this.itemPrices = page.locator('[data-test="inventory-item-price"]');
    this.checkoutButton = page.locator('[data-test="checkout"]');
  }

  async getItemNames() {
    return this.itemNames.allInnerTexts();
  }

  async getItemPrices() {
    const raw = await this.itemPrices.allInnerTexts();
    return raw.map((p) => parseFloat(p.replace('$', '')));
  }

  async proceedToCheckout() {
    await this.checkoutButton.click();
  }
}

module.exports = { CartPage };
