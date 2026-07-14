class CartPage {
  constructor(page) {
    this.page = page;
    // Назви товарів у кошику
    this.cartItemNames = page.locator('.inventory_item_name');
    // Лічильник кошика
    this.cartBadge = page.locator('[data-test="shopping-cart-badge"]');
    // Кнопка видалення конкретного товару
    this.removeBikeLightBtn = page.locator('[data-test="remove-sauce-labs-bike-light"]');
  }

  async removeBikeLight() {
    await this.removeBikeLightBtn.click();
  }
}

module.exports = { CartPage };
