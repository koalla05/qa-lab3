# User Flows — saucedemo.com (Victoria)

**Base URL:** https://www.saucedemo.com

---

## User Flow 1: Sorting & Cart Management

> Мета: перевірити, що працює сортування товарів за ціною,
> що в кошик можна додати кілька товарів і видалити один із них.

1. **Login Page** — відкрити сторінку входу
2. **Enter credentials:**
   - Login: `standard_user`
   - Password: `secret_sauce`
3. **Inventory Page** — `https://www.saucedemo.com/inventory.html`
4. **Sort products** — обрати сортування **"Price (low to high)"**
5. **Verify:** перший товар у списку — найдешевший, тобто **"Sauce Labs Onesie"** ($7.99)
6. **Add to cart** два товари:
   - "Sauce Labs Bike Light" ($9.99)
   - "Sauce Labs Fleece Jacket" ($49.99)
7. **Verify:** іконка кошика показує **2**
8. **Cart Page** — `https://www.saucedemo.com/cart.html` (клік на іконку кошика)
9. **Verify:** у кошику присутні обидва товари
10. **Remove** товар "Sauce Labs Bike Light" з кошика
11. **Verify:** лічильник кошика тепер **1**, залишився лише "Sauce Labs Fleece Jacket"

---

## User Flow 2: Negative Login (Locked Out User)

> Мета (негативний тест): переконатися, що заблокований користувач
> НЕ може увійти і бачить коректне повідомлення про помилку.

1. **Login Page** — відкрити сторінку входу
2. **Enter credentials:**
   - Login: `locked_out_user`
   - Password: `secret_sauce`
3. **Click** кнопку Login
4. **Verify:** переходу на inventory НЕ відбулось (користувач лишився на сторінці входу)
5. **Verify:** відображається повідомлення про помилку:
   **"Epic sadface: Sorry, this user has been locked out."**

---

### Notes
- Flow 1 — позитивний сценарій: сортування → додавання кількох товарів → видалення.
- Flow 2 — негативний сценарій: перевірка обробки заблокованого акаунта.
- Обидва флоу реалізовані через Page Object Model (папка `pages/`).
