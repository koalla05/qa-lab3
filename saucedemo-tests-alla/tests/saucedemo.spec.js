const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { InventoryPage } = require('../pages/InventoryPage');
const { CartPage } = require('../pages/CartPage');
const { CheckoutPage } = require('../pages/CheckoutPage');

test.describe('Saucedemo E2E User Flows', () => {
  
  // page instances
  let loginPage, inventoryPage, cartPage, checkoutPage;

  test.beforeEach(async ({ page }) => {
    // init before each test
    loginPage = new LoginPage(page);
    inventoryPage = new InventoryPage(page);
    cartPage = new CartPage(page);
    checkoutPage = new CheckoutPage(page);
  });

  test('User Flow 1: Add Product to Cart (Path A)', async ({ page }) => {
    // 1-3. open login page, fill credentials and login
    await loginPage.navigate();
    await loginPage.login('standard_user', 'secret_sauce');

    // 4-5. Verify we are on the inventory page
    await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');

    // 6-7. Add product "Sauce Labs Backpack" to cart
    await inventoryPage.addBackpackToCart();

    // 8. Verify: cart badge shows 1 item
    await expect(inventoryPage.cartBadge).toHaveText('1');
  });

  test('User Flow 2: Checkout Process', async ({ page }) => {
    // repeat steps from User Flow 1 to add product to cart
    await loginPage.navigate();
    await loginPage.login('standard_user', 'secret_sauce');
    await inventoryPage.addBackpackToCart();

    // 1-2. click on cart icon -> Verify we are on the cart page
    await inventoryPage.clickCart();
    await expect(page).toHaveURL('https://www.saucedemo.com/cart.html');

    // 3-4. click on Checkout -> Transition to Checkout Step One
    await cartPage.proceedToCheckout();
    await expect(page).toHaveURL('https://www.saucedemo.com/checkout-step-one.html');

    // 5-6. fill in shipping details and click Continue
    await checkoutPage.fillCheckoutDetails('Alla', 'Kovalchuk', '0613');

    // 7. Verify details page URL
    await expect(page).toHaveURL('https://www.saucedemo.com/checkout-step-two.html');

    // 8-9. click Finish to complete the order
    await checkoutPage.finishCheckout();
    await expect(page).toHaveURL('https://www.saucedemo.com/checkout-complete.html');

    // 10. Verify: text of successful order completion
    await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');
  });

});