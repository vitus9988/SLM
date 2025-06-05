import os, asyncio, requests, discord
from discord.ext import commands

URL = "http://localhost:8080/v1/chat/completions"

SYSTEM_PROMPT = """
system_prompt
"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=None, intents=intents)

buffers: dict[int, list[str]] = {}
tasks:   dict[int, asyncio.Task] = {}

def llm_call(text: str) -> str:
    payload = {
        "model": "gpt-3.5-turbo",
        "presence_penalty": 0.3,
        "temperature": 0.7,
        "top_p": 0.9,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": text},
        ],
    }
    r = requests.post(URL, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()

async def flush(channel: discord.TextChannel):
    content = "\n".join(buffers.pop(channel.id, []))
    if not content:
        tasks.pop(channel.id, None)
        return
    loop = asyncio.get_running_loop()
    try:
        reply = await loop.run_in_executor(None, llm_call, content)
    except Exception as e:
        reply = f"⚠️ LLM 오류: {e}"
    await channel.send(reply)
    tasks.pop(channel.id, None)

@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot:
        return
    speaker = msg.author.display_name
    buffers.setdefault(msg.channel.id, []).append(f"{speaker}: {msg.content}")

    if (t := tasks.get(msg.channel.id)):
        t.cancel()

    async def debounce(c=msg.channel):
        try:
            await asyncio.sleep(8)
            await flush(c)
        except asyncio.CancelledError:
            pass

    tasks[msg.channel.id] = asyncio.create_task(debounce())

token = "token"
bot.run(token)

