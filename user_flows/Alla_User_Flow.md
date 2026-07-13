# User Flows — saucedemo.com

## User Flow 1: Add Product to Cart

**Base URL:** https://www.saucedemo.com

1. **Start**
2. **Login Page** — navigate to the login page
3. **Enter credentials** (Credentials to login):
   - Login: `standard_user`
   - Password: `secret_sauce`
4. **Inventory Page** — `https://www.saucedemo.com/inventory.html`
5. **Find product** "Sauce Labs Backpack"
6. **Decision point** — two equivalent paths to reach the product:
   - Path A: proceed directly to adding the product to cart
   - Path B: **Click on the product name** → opens product detail page
     `https://www.saucedemo.com/inventory-item.html?id=4`
   - Both paths converge before the next step
7. **Click on "Add to cart"**
8. **Verify:** Does the cart icon show **+1**?

---

## User Flow 2: Checkout Process

> Continues from the end of User Flow 1 ("The same steps as in User Flow 1")

1. **Click on Cart Icon**
2. **Cart Page** — `https://www.saucedemo.com/cart.html`
3. **Click on Checkout Button**
4. **Checkout Page** — `https://www.saucedemo.com/checkout-step-one.html`
5. **Enter checkout details** (Credentials to checkout):
   - First name: `Alla`
   - Last name: `Kovalchuk`
   - Postcode: `0613`
6. **Click on Continue Button**
7. **Verify details** — `https://www.saucedemo.com/checkout-step-two.html`
8. **Click on Finish Button**
9. **Finish Page** — `https://www.saucedemo.com/checkout-complete.html`
10. **Verify:** page should display **"Thank you for your order!"**

---

### Notes
- Flow 1 covers login → locate product → add to cart → confirm cart count updated.
- Flow 2 covers cart → checkout form → order confirmation.
- Color coding in the diagram: blue = navigation/pages, green = actions/checks, orange = credential/data input and final verification steps.