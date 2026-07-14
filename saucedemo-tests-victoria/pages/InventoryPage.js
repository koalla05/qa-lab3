class InventoryPage {
  constructor(page) {
    this.page = page;
    // Випадаючий список сортування
    this.sortDropdown = page.locator('[data-test="product-sort-container"]');
    // Назви всіх товарів у списку
    this.itemNames = page.locator('.inventory_item_name');
    // Кнопки "Add to cart" для конкретних товарів
    this.addBikeLightBtn = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]');
    this.addFleeceJacketBtn = page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]');
    // Іконка та лічильник кошика
    this.cartBadge = page.locator('[data-test="shopping-cart-badge"]');
    this.cartLink = page.locator('[data-test="shopping-cart-link"]');
  }

  // Сортування за значенням: 'az', 'za', 'lohi', 'hilo'
  async sortBy(value) {
    await this.sortDropdown.selectOption(value);
  }

  // Назва першого товару в списку (для перевірки сортування)
  firstItemName() {
    return this.itemNames.first();
  }

  async addBikeLightToCart() {
    await this.addBikeLightBtn.click();
  }

  async addFleeceJacketToCart() {
    await this.addFleeceJacketBtn.click();
  }

  async openCart() {
    await this.cartLink.click();
  }
}

module.exports = { InventoryPage };
