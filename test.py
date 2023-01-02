from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').fill('wikipedia batata')
    page.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    WikipediaResponse = page.locator('xpath=//*[@id="rso"]/div[1]/div/div/div[2]/div/span').inner_text()
    print(WikipediaResponse)
    browser.close()
