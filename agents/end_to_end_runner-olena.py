import asyncio
import os

from browser_use import Agent, Tools
from browser_use.llm import ChatMistral
from dotenv import load_dotenv


load_dotenv()


async def main():
    llm = ChatMistral(
        model="mistral-medium-latest",
        api_key=os.getenv("MISTRAL_API_KEY"),
        timeout=90.0,
        max_retries=2,
    )

    tools = Tools(exclude_actions=["search"])

    task_prompt = """
    You are an automated QA engineer executing E2E tests on https://www.saucedemo.com.
    Use only the website content visible in the browser. Do not search the web.
    Execute the test cases carefully and report all observed mismatches.

    TEST CASE 1: Product details consistency for problem_user
    1. Navigate to https://www.saucedemo.com.
    2. Log in using:
       - Username: problem_user
       - Password: secret_sauce
    3. On the inventory page, find the product "Sauce Labs Backpack".
    4. Record the product name, product price, and product image shown on the inventory page.
    5. Click the "Sauce Labs Backpack" product name to open its product details page.
    6. Verify that the product details page shows the same product name, price, and image
       as the inventory page.
    7. If any value differs, mark TEST CASE 1 as FAILED and explain the exact mismatch.

    TEST CASE 2: Add product to cart for problem_user
    1. Start from a clean state on https://www.saucedemo.com if needed.
    2. Log in using:
       - Username: problem_user
       - Password: secret_sauce
    3. On the inventory page, find the product "Sauce Labs Backpack".
    4. Click the "Sauce Labs Backpack" product name to open its product details page.
    5. Confirm which product details page opened.
    6. Click the "Add to cart" button.
    7. Verify that the cart badge displays "1".
    8. Open the cart.
    9. Verify that "Sauce Labs Backpack" is present in the cart.
    10. If the wrong product opens, the badge is missing, or the product is absent from the cart,
        mark TEST CASE 2 as FAILED and explain the exact issue.

    Final answer format:
    TEST CASE 1: PASSED or FAILED
    Details: short explanation with observed values.

    TEST CASE 2: PASSED or FAILED
    Details: short explanation with observed values.

    Overall result: SUCCESS only if both test cases passed; otherwise FAILED.
    """

    print("Starting AI-driven E2E test agent...")

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
