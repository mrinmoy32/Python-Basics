import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)

async def main():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    await fetch_data(url)

# Run the async main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
