import asyncio
import os

from browser_use import Agent, Tools
from browser_use.llm import ChatMistral
from dotenv import load_dotenv


load_dotenv() # load mistral key from .env file


async def main():
    # mistral offers free tokens and a native browser-use provider wrapper
    llm = ChatMistral(
        model="mistral-medium-latest",
        api_key=os.getenv("MISTRAL_API_KEY"),
        timeout=90.0,
        max_retries=2,
    )

    # Disable the built-in web search action: the agent must read values from
    # the page under test, never from the internet.
    tools = Tools(exclude_actions=["search"])

    task_prompt = """
    You are an automated QA engineer running E2E tests on https://www.saucedemo.com.
    Use ONLY the content visible in the browser. Do not search the web.
    Execute the two test cases below in order and report the results.

    TEST CASE 1: Add multiple products to the cart
    1. Navigate to https://www.saucedemo.com.
    2. Log in with Username 'standard_user' and Password 'secret_sauce'.
    3. On the inventory page, click "Add to cart" for "Sauce Labs Bike Light".
    4. Click "Add to cart" for "Sauce Labs Bolt T-Shirt".
    5. VERIFY: the shopping-cart badge in the top-right shows the number 2.
    6. Open the cart by clicking the shopping-cart icon.
    7. VERIFY: the cart contains exactly two items — "Sauce Labs Bike Light"
       and "Sauce Labs Bolt T-Shirt".
    8. If the badge is not 2, or either product is missing, mark TEST CASE 1
       as FAILED and explain the exact mismatch.

    TEST CASE 2: Full checkout with price verification (continue from Test Case 1)
    9.  While on the cart page, read and remember the price of each of the two items.
    10. Click the "Checkout" button.
    11. On the checkout information page, enter:
        - First Name: Olesia
        - Last Name: Mykhailyshyn
        - Zip/Postal Code: 04070
    12. Click "Continue".
    13. On the summary page, read the "Item total" value.
    14. VERIFY: the "Item total" equals the sum of the two item prices you read
        in step 9.
    15. Click "Finish".
    16. VERIFY: the final page displays the message "Thank you for your order!".
    17. If the item total does not match, or the confirmation message is missing,
        mark TEST CASE 2 as FAILED and explain the exact issue.

    Final answer format:
    TEST CASE 1: PASSED or FAILED
    Details: short explanation with observed values (badge count, cart items).

    TEST CASE 2: PASSED or FAILED
    Details: short explanation with observed values (item prices, item total).

    Overall result: SUCCESS only if both test cases passed; otherwise FAILED.
    """

    print("Starting AI-driven E2E test agent (Mistral)...")

    agent = Agent(
        task=task_prompt,
        llm=llm,
        tools=tools,
    )

    history = await agent.run()

    print("\nTest execution finished.")
    print(history.final_result())


if __name__ == "__main__":
    asyncio.run(main())
