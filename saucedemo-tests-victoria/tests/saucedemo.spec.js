const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { InventoryPage } = require('../pages/InventoryPage');
const { CartPage } = require('../pages/CartPage');

test.describe('Saucedemo E2E User Flows (Victoria)', () => {

  let loginPage, inventoryPage, cartPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    inventoryPage = new InventoryPage(page);
    cartPage = new CartPage(page);
  });

  test('User Flow 1: Sorting & Cart Management', async ({ page }) => {
    // 1-3. Логін
    await loginPage.navigate();
    await loginPage.login('standard_user', 'secret_sauce');
    await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');

    // 4-5. Сортування за ціною (зростання) -> перший товар найдешевший
    await inventoryPage.sortBy('lohi');
    await expect(inventoryPage.firstItemName()).toHaveText('Sauce Labs Onesie');

    // 6-7. Додати два товари, перевірити лічильник = 2
    await inventoryPage.addBikeLightToCart();
    await inventoryPage.addFleeceJacketToCart();
    await expect(inventoryPage.cartBadge).toHaveText('2');

    // 8-9. Відкрити кошик, перевірити наявність обох товарів
    await inventoryPage.openCart();
    await expect(page).toHaveURL('https://www.saucedemo.com/cart.html');
    await expect(cartPage.cartItemNames).toHaveText([
      'Sauce Labs Bike Light',
      'Sauce Labs Fleece Jacket',
    ]);

    // 10-11. Видалити один товар, перевірити лічильник = 1 і що лишився правильний товар
    await cartPage.removeBikeLight();
    await expect(cartPage.cartBadge).toHaveText('1');
    await expect(cartPage.cartItemNames).toHaveText(['Sauce Labs Fleece Jacket']);
  });

  test('User Flow 2: Negative Login (Locked Out User)', async ({ page }) => {
    // 1-3. Спроба входу заблокованим користувачем
    await loginPage.navigate();
    await loginPage.login('locked_out_user', 'secret_sauce');

    // 4. Переходу на inventory НЕ сталося (лишились на сторінці входу)
    await expect(page).toHaveURL('https://www.saucedemo.com/');

    // 5. Показано коректне повідомлення про помилку
    await expect(loginPage.errorMessage).toHaveText(
      'Epic sadface: Sorry, this user has been locked out.'
    );
  });

});
