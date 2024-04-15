import requests
from requests import Response

import asyncio
from asyncio import Task

async def fetch_status(url : str) -> dict:
    print(f'Fetching status for {url}')
    response : Response = await asyncio.to_thread(requests.get, url, None)
    print(f'Done ! {url}')
    return({'status' : response.status_code, 'url' : url})

async def main() -> None:
    apple_task : Task[dict] = asyncio.create_task(fetch_status('https://apple.com'))
    google_task : Task[dict] = asyncio.create_task(fetch_status('https://google.com'))
    
    apple_status : dict = await apple_task
    google_status : dict = await google_task
    
    print(apple_status)
    print(google_status)
    
if __name__ == '__main__':
    asyncio.run(main=main())
    