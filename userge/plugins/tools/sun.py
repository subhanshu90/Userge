from asyncio import sleep
from collections import deque

from userge import userge, Message


@userge.on_cmd("sun$", about={'header': "kensar sun animation"})
async def sun_(message: Message):
    """sun"""
    deq = deque(list("😎🌤🌥☀️⛅️🌦🌞"))
    try:
        for _ in range(32):
            await sleep(0.3)
            await message.edit("".join(deq))
            deq.rotate(1)
    except Exception:
        await message.delete()
