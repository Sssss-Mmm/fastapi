from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from playwright.async_api import async_playwright
import os

app = FastAPI()

class URLInput(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/rpa/screenshot")
async def take_screenshot(input_data: URLInput):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(input_data.url)
            filename = "screenshot.png"
            await page.screenshot(path=filename)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            await browser.close()
    
    return {"status": "success", "message": f"Screenshot saved as {filename}", "url": input_data.url}

@app.post("/rpa/scrape")
async def scrape_title(input_data: URLInput):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(input_data.url)
            title = await page.title()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            await browser.close()
    return {"status": "success", "url": input_data.url, "title": title}
