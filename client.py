import asyncio
import socket
from datetime import datetime

import aiofiles
from aioconsole import aprint


HISTORY_FILENAME = "minechat.history"
INIT_MESSAGE = "Подключились к серверу"


async def main():
    async with aiofiles.open(HISTORY_FILENAME, mode="a") as f:
        reader, writer = await asyncio.open_connection("minechat.dvmn.org", 5000)
        connect_message = f"[{datetime.now().strftime('%d.%m.%Y %H:%M')}] {INIT_MESSAGE}\n"
        await f.write(connect_message)
        await aprint(connect_message)

        while True:
            try:
                if reader.at_eof():
                    break
                data = await reader.read(1024)
                await f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M')}] {data.decode()}")
                await aprint(data.decode())
            except UnicodeDecodeError as ex:
                await aprint(ex)
                continue
            except socket.gaierror:
                await asyncio.sleep(3)

        writer.close()
        await writer.wait_closed()


asyncio.run(main())
