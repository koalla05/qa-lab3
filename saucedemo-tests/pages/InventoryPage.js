class InventoryPage {
  constructor(page) {
    this.page = page;
    this.backpackTitle = page.locator('#item_4_title_link');
    this.addToCartBackpackBtn = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]');
    this.cartBadge = page.locator('[data-test="shopping-cart-badge"]');
    this.cartLink = page.locator('[data-test="shopping-cart-link"]');
  }

  // Path A: Пряме додавання з головної сторінки
  async addBackpackToCart() {
    await this.addToCartBackpackBtn.click();
  }

  // Path B: Клік на назву для переходу в картку товару
  async openBackpackDetails() {
    await this.backpackTitle.click();
  }

  async clickCart() {
    await this.cartLink.click();
  }
}

module.exports = { InventoryPage };