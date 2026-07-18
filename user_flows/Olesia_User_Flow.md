# User Flows — saucedemo.com (Olesia)

**Framework:** Playwright (`@playwright/test`, JavaScript)
**Pattern:** Page Object Model
**Base URL:** https://www.saucedemo.com

---

## Test Case 1: Add Multiple Products to Cart

**Goal:** Verify that a standard user can add several products from the inventory
page and that the cart badge and cart contents stay consistent.

**Preconditions:** logged out.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Navigate to `https://www.saucedemo.com` | Login page is shown |
| 2 | Log in with `standard_user` / `secret_sauce` | Redirect to `/inventory.html` |
| 3 | Add **"Sauce Labs Bike Light"** to cart from the inventory page | Its button switches to "Remove" |
| 4 | Add **"Sauce Labs Bolt T-Shirt"** to cart from the inventory page | Its button switches to "Remove" |
| 5 | Read the shopping-cart badge | Badge shows **2** |
| 6 | Open the cart (`/cart.html`) | Cart page is shown |
| 7 | Read the list of item names in the cart | Cart contains exactly **"Sauce Labs Bike Light"** and **"Sauce Labs Bolt T-Shirt"** |

**Assertion:** badge count = 2 AND cart item names = the two added products.

---

## Test Case 2: Full Checkout with Price Verification

> Continues the "add two products" scenario from Test Case 1.

**Goal:** Complete the checkout flow and verify that the item total on the
summary page equals the sum of the individual product prices.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | (Setup) Log in and add the two products, open the cart | Cart holds 2 items |
| 2 | Record each item's price on the cart page | Two prices captured |
| 3 | Click **Checkout** | Redirect to `/checkout-step-one.html` |
| 4 | Fill checkout info — First: `Olesia`, Last: `Mykhailyshyn`, Zip: `04070` | Fields filled |
| 5 | Click **Continue** | Redirect to `/checkout-step-two.html` |
| 6 | Read the **Item total** value on the summary page | `Item total: $<sum>` |
| 7 | Click **Finish** | Redirect to `/checkout-complete.html` |
| 8 | Read the confirmation header | Header = **"Thank you for your order!"** |

**Assertion:** item total on summary = sum of the two recorded cart prices
AND confirmation header = "Thank you for your order!".

---

### Notes
- Both flows use the **Page Object Model**: one class per page
  (`LoginPage`, `InventoryPage`, `CartPage`, `CheckoutPage`) holding locators
  and actions; the spec file contains only orchestration + assertions.
- Test Case 2 reuses the setup from Test Case 1 (add-to-cart), then extends it
  through the checkout funnel — mirroring a realistic end-to-end purchase.
- Difference from teammates' flows: this scenario adds **two** products and
  verifies both the **cart contents** and the **computed price total**, rather
  than a single-item add or a product-details consistency check.
