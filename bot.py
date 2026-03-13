import discord
from discord.ext import commands
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


def search_book(query):
    url = f"https://gutendex.com/books/?search={query}"
    r = requests.get(url).json()

    if not r["results"]:
        return None

    book = random.choice(r["results"])

    title = book["title"]
    author = book["authors"][0]["name"] if book["authors"] else "Autor desconocido"

    text_url = None
    for key, value in book["formats"].items():
        if "text/plain" in key:
            text_url = value
            break

    if not text_url:
        return None

    return title, author, text_url


def get_fragment(url):
    text = requests.get(url).text

    paragraphs = [
        p.strip() for p in text.split("\n\n")
        if len(p.strip()) > 120
    ]

    return random.choice(paragraphs)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command()
async def buscar(ctx, *, query):

    await ctx.send("🔎 Buscando libro...")

    result = search_book(query)

    if not result:
        await ctx.send("No encontré libros con ese nombre.")
        return

    title, author, url = result

    fragment = get_fragment(url)

    embed = discord.Embed(
        title=f"📖 {title}",
        description=fragment[:1000],
        color=0x6c5ce7
    )

    embed.set_footer(text=f"Autor: {author}")

    await ctx.send(embed=embed)


bot.run(TOKEN)
