import asyncio


async def async_generator(num):
    for i in range(num):
        await asyncio.sleep(1)
        yield i


async def main():
    async for value in async_generator(3):
        print(value)


asyncio.run(main())