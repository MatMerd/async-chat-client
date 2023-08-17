import asyncio


async def main():
    reader, writer = await asyncio.open_connection("minechat.dvmn.org", 5000)
    try:
        while not reader.at_eof():
            data = await reader.read(4096)
            print(data.decode())
    finally:
        writer.close()
        await writer.wait_closed()


asyncio.run(main())
