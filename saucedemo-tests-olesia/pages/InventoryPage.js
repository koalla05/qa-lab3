class InventoryPage {
  constructor(page) {
    this.page = page;
    this.cartBadge = page.locator('[data-test="shopping-cart-badge"]');
    this.cartLink = page.locator('[data-test="shopping-cart-link"]');
  }

  _slug(productName) {
    return productName.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }

  async addProductToCart(productName) {
    const slug = this._slug(productName);
    await this.page.locator(`[data-test="add-to-cart-${slug}"]`).click();
  }

  async getCartCount() {
    if (await this.cartBadge.count() === 0) return '0';
    return (await this.cartBadge.innerText()).trim();
  }

  async openCart() {
    await this.cartLink.click();
  }
}

module.exports = { InventoryPage };
