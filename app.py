import asyncio
from pyppeteer import launch
import asyncio
from pyppeteer import launch

async def main():
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto("https://medigence.com/hospitals/neurology/brain-tumour/india")
    # create a screenshot of the page and save it
    await page.screenshot({"path": "python.png"})
    # close the browserimport pandas as pd
import asyncio
from pyppeteer import launch
import nest_asyncio
nest_asyncio.apply()
# csv = pd.read_csv('/Users/gautammishra/Python/MediGence/Pyppeteer/URLs.csv')
async def main():
    browser = await launch()
    page = await browser.newPage()
    # Google Desktop Bot
    # await page.setUserAgent("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    #Yahoo Bot
    await page.setUserAgent("Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)")
    # Google Smartphone Bot
    # await page.setUserAgent("Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +https://www.google.com/bot.html)")
    # await page.setUserAgent('Googlebot/2.1 (+http://www.google.com/bot.html)')
    #Yahoo Bot
    # await page.setUserAgent("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp")
    # Setting up the Viewport Mobile
    await page.setViewport({'width': 1920, 'height': 1080})
    # Desktop Viewport
    # await page.setViewport({'width': 1920, 'height': 1080})
    # Loop around to scrape all the URLs in CSV
    # for i in range(len(csv)):
    # for i in range(len(csv)):
    url = 'https://medigence.com/hospitals/neurology/brain-tumour/india '
    name = 'Brain Tumor India 1'
        # name = 'Apollo 2 Indraprastha'
    await page.goto(url)
    await page.screenshot(
        {'path': "python.png",
        'fullPage': True})
    await browser.close()
print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")