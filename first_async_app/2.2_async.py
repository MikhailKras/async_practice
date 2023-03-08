import asyncio
import time


async def func1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print('func1 ended')


async def func2(x):
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('func2 ended')


async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    await task1
    await task2


print(time.strftime('%X'))


asyncio.run(main())


print(time.strftime('%X'))
