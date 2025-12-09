import asyncio

async def print_msg (delay: int, msg: str):
    await asyncio.sleep(delay)
    print(msg)
async def main():
    task1 = asyncio.create_task(print_msg(2, "Hello "))
    task2 = asyncio.create_task(print_msg(3, "world"))
    await task1
    await task2
asyncio.run(main())