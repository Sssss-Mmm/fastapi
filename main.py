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

# 스크린샷
@app.post("/rpa/screenshot")
## URL을 입력받아 스크린샷을 저장
async def take_screenshot(input_data: URLInput):
    # playwright를 사용하여 브라우저를 실행
    async with async_playwright() as p:
        # 브라우저를 실행
        browser = await p.chromium.launch(headless=True)
        # 브라우저에서 새로운 페이지를 생성
        page = await browser.new_page()
        try:
            # URL로 이동
            await page.goto(input_data.url)
            # 스크린샷을 저장
            filename = "screenshot.png"
            # 스크린샷을 저장
            await page.screenshot(path=filename)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            await browser.close()
    # 스크린샷이 저장된 경로를 반환
    return {"status": "success", "message": f"Screenshot saved as {filename}", "url": input_data.url}


# 타이틀 스크래핑
@app.post("/rpa/scrape")
async def scrape_title(input_data: URLInput):
    # playwright를 사용하여 브라우저를 실행
    async with async_playwright() as p:
        # 브라우저를 실행
        browser = await p.chromium.launch(headless=True)
        # 브라우저에서 새로운 페이지를 생성
        page = await browser.new_page()
        # URL로 이동
        try:
            await page.goto(input_data.url)
            # URL의 타이틀을 가져옴
            title = await page.title()
        except Exception as e:
            # 오류가 발생하면 HTTPException을 발생시킴
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            # 브라우저를 종료
            await browser.close()
    # URL의 타이틀을 반환
    return {"status": "success", "url": input_data.url, "title": title}
