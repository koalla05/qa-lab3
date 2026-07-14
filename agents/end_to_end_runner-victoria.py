import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, Tools
from browser_use.llm import ChatMistral

load_dotenv()

async def main():
    llm = ChatMistral(
        model="mistral-medium-latest",
        api_key=os.getenv("MISTRAL_API_KEY"),
        timeout=90.0,
        max_retries=2,
        max_tokens=4000,
    )

    fallback_llm = ChatMistral(
        model="mistral-small-latest",
        api_key=os.getenv("MISTRAL_API_KEY"),
        timeout=90.0,
        max_retries=2,
        max_tokens=4000,
    )

    tools = Tools(exclude_actions=['search'])

    task_prompt = """
    You are an automated QA engineer running E2E tests on https://www.saucedemo.com.
    Execute the following two user flows precisely and verify the results.
    If a step fails, stop and report the failure.

    USER FLOW 1: Sorting & Cart Management
    1. Navigate to https://www.saucedemo.com
    2. Log in using credentials: Username 'standard_user', Password 'secret_sauce'.
    3. On the Inventory page, open the sort dropdown (top-right) and select 'Price (low to high)'.
    4. VERIFY: The first product in the list is now the cheapest one, 'Sauce Labs Onesie'.
    5. Click 'Add to cart' for 'Sauce Labs Bike Light'.
    6. Click 'Add to cart' for 'Sauce Labs Fleece Jacket'.
    7. VERIFY: The shopping cart badge in the top-right corner shows the number '2'.
       Read the number directly from the page, do not search the web.
    8. Click the shopping cart icon to open the cart page (URL contains cart.html).
    9. VERIFY: The cart contains exactly two items: 'Sauce Labs Bike Light' and 'Sauce Labs Fleece Jacket'.
    10. Click the 'Remove' button next to 'Sauce Labs Bike Light'.
    11. VERIFY: The cart badge now shows '1' and only 'Sauce Labs Fleece Jacket' remains in the cart.

    USER FLOW 2: Negative Login (Locked Out User)
    12. Navigate to https://www.saucedemo.com (open the login page).
    13. Log in using credentials: Username 'locked_out_user', Password 'secret_sauce'.
    14. VERIFY: The login FAILED - you are still on the login page (URL does NOT contain inventory.html).
    15. VERIFY: An error message is displayed with the exact text:
        'Epic sadface: Sorry, this user has been locked out.'

    At the end, provide a short text summary: 'SUCCESS' if all assertions met,
    or 'FAILED' with details.
    """

    print("Starting AI-Driven E2E Test Agent (Mistral)...")

    agent = Agent(
        task=task_prompt,
        llm=llm,
        tools=tools,
        fallback_llm=fallback_llm,
        max_actions_per_step=2,
    )

    history = await agent.run()

    print("\nTest Execution Finished!")
    print(history.final_result())

if __name__ == "__main__":
    asyncio.run(main())
