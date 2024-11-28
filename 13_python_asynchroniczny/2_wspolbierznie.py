import asyncio
import random

async def task (name, delay):
    print(f'Task {name} rozpoczęty. Opóżnienie {delay}')
    await asyncio.sleep(delay)
    print(f'Task {name} zakończony')

async def main():

    tasks = [
        task('A', random.uniform(1, 3)),
        task('B', random.uniform(1, 3)),
        task('C', random.uniform(1, 3)),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())