import asyncio

async def task_1():
    print("Первая задача")
    await asyncio.sleep(2)
async def task_2():
    print("Вторая задача")
    await asyncio.sleep(3)
async def main():
    task1 = asyncio.create_task(task_1())
    task2 = asyncio.create_task(task_2())
    await asyncio.gather(task1, task2)
asyncio.run(main())