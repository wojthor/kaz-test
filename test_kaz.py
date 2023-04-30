from playwright.async_api import async_playwright
import asyncio


async def test_kaz():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(
            "https://incomparable-speculoos-744618.netlify.app/login?redirectTo=/"
        )
        await page.fill('input[type="email"]', "matiborek@gmail.com")
        await page.fill('input[name="password"]', "matiborek2115")
        await page.click('button[class="btn btn-primary"]')
        await asyncio.sleep(5)
        searching = await page.fill(
            'input[class="input input-bordered text-primary input-md w-full"]',
            "Kaz Bałagane",
        )
        search_result_selector = 'a.item[href="/artist/2GzZAv52VCMdVli7QzkteT"]'
        search_result_visible = await page.is_visible(search_result_selector)
        await asyncio.sleep(5)
        await page.click('a[class="item"]')

        assert search_result_visible, "Search field not found or not visible"
        assert searching, "Tab loading error"

        await browser.close()


asyncio.run(test_kaz())
