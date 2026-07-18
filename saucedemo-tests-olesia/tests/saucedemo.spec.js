const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { InventoryPage } = require('../pages/InventoryPage');
const { CartPage } = require('../pages/CartPage');
const { CheckoutPage } = require('../pages/CheckoutPage');

// Products used across both test cases.
const PRODUCTS = ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt'];

test.describe('Saucedemo E2E User Flows (Olesia)', () => {
  let loginPage, inventoryPage, cartPage, checkoutPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    inventoryPage = new InventoryPage(page);
    cartPage = new CartPage(page);
    checkoutPage = new CheckoutPage(page);

    // Every flow starts logged in on the inventory page.
    await loginPage.navigate();
    await loginPage.login('standard_user', 'secret_sauce');
    await expect(page).toHaveURL(/.*\/inventory\.html/);
  });

  test('Test Case 1: Add multiple products to cart', async ({ page }) => {
    // Add the two products from the inventory page.
    for (const product of PRODUCTS) {
      await inventoryPage.addProductToCart(product);
    }

    // Badge reflects the number of added items.
    expect(await inventoryPage.getCartCount()).toBe('2');

    // Cart holds exactly the two products we added.
    await inventoryPage.openCart();
    await expect(page).toHaveURL(/.*\/cart\.html/);

    const names = await cartPage.getItemNames();
    expect(names).toHaveLength(2);
    expect(names).toEqual(expect.arrayContaining(PRODUCTS));
  });

  test('Test Case 2: Full checkout with price verification', async ({ page }) => {
    // Setup: add the two products and open the cart.
    for (const product of PRODUCTS) {
      await inventoryPage.addProductToCart(product);
    }
    await inventoryPage.openCart();
    await expect(page).toHaveURL(/.*\/cart\.html/);

    // Capture the prices shown in the cart, then compute their sum.
    const cartPrices = await cartPage.getItemPrices();
    const expectedTotal = Number(cartPrices.reduce((a, b) => a + b, 0).toFixed(2));

    // Fill checkout information.
    await cartPage.proceedToCheckout();
    await expect(page).toHaveURL(/.*\/checkout-step-one\.html/);
    await checkoutPage.fillInformation('Olesia', 'Mykhailyshyn', '04070');

    // Summary page: item total equals the sum of the cart prices.
    await expect(page).toHaveURL(/.*\/checkout-step-two\.html/);
    expect(await checkoutPage.getItemTotal()).toBe(expectedTotal);

    // Finish and confirm the order.
    await checkoutPage.finish();
    await expect(page).toHaveURL(/.*\/checkout-complete\.html/);
    await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');
  });
});
