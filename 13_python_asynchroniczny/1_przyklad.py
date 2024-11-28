import asyncio

async def example():
    print('Start')
    await asyncio.sleep(1)
    print('End')

async def main():
    print('Przed mainem')
    await example()
    print ('po mainie')

asyncio.run(main())