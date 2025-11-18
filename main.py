from fastapi.security import APIKeyHeader
from fastapi import FastAPI, Query, HTTPException, Depends, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from datetime import datetime, timedelta

from data_collector import fetch_sector_news
from ai_analysis import generate_ai_report

app = FastAPI()


VALID_TOKEN = "mysecrettoken"
VALID_SECTORS = ["pharmaceuticals", "technology", "agriculture", "energy", "finance"]

# FastAPI will extract "authorization" header automatically
api_key_header = APIKeyHeader(name="authorization", auto_error=True)


# RATE LIMIT STORAGE
rate_limit_store = {}   


class RateLimitException(Exception):
    def __init__(self, retry_after: int):
        self.retry_after = retry_after


@app.exception_handler(RateLimitException)
async def rate_limit_handler(request: Request, exc: RateLimitException):
    return JSONResponse(
        status_code=429,
        content={"detail": f"⏳ Rate limit exceeded. Try again in {exc.retry_after} seconds."}
    )

def check_rate_limit(token: str):
    now = datetime.utcnow()

    if token not in rate_limit_store or rate_limit_store[token][1] < now:
        rate_limit_store[token] = [1, now + timedelta(minutes=1)]
        return

    count, reset_time = rate_limit_store[token]

    if count >= 5:
        seconds_left = (reset_time - now).seconds
        raise RateLimitException(seconds_left)

    rate_limit_store[token][0] = count + 1


# MAIN ENDPOINT
@app.get("/analyzesector", response_class=PlainTextResponse)
def analyze_sector(
        sector: str = Query(..., min_length=3),
        authorization: str = Depends(api_key_header),
        request: Request = None
):
    print("\n HEADERS RECEIVED:", dict(request.headers))

    #  TOKEN VALIDATION
    if authorization != VALID_TOKEN:
        raise HTTPException(status_code=401, detail=" Unauthorized Token")

    #  SECTOR VALIDATION
    if sector.lower() not in VALID_SECTORS:
        raise HTTPException(status_code=400, detail=" Invalid Sector Name")

    #  RATE LIMIT CHECK
    check_rate_limit(authorization)

    #  FETCH NEWS
    news_list = fetch_sector_news(sector)

    #  GENERATE AI REPORT
    report = generate_ai_report(sector, news_list)

    return report



# RUN SERVER
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
