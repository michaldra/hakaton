import discord
import bot_logic
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def all(ctx):
    with open('all.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'👋')

@bot.command()
async def meme(ctx):
    rng = random.randint(0,99)
    if rng < 50:
        img_name = random.choice(os.listdir('memes/1common'))
        with open(f'memes/1common/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Popularny (50%)')
    elif rng < 75:
        img_name = random.choice(os.listdir('memes/2uncommon'))
        with open(f'memes/2uncommon/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Niepopularny (25%)')
    elif rng < 90:
        img_name = random.choice(os.listdir('memes/3rare'))
        with open(f'memes/3rare/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Rzadki (15%)')
    elif rng < 99:
        img_name = random.choice(os.listdir('memes/4epic'))
        with open(f'memes/4epic/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Epicki (9%)')
    else:
        img_name = random.choice(os.listdir('memes/5legendary'))
        with open(f'memes/5legendary/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Legendarny (1%)')


@bot.command()
async def pomysl(ctx):
    await ctx.send(bot_logic.pomysl())

@bot.command()
async def ciekawostka(ctx):
    await ctx.send(bot_logic.ciekawostka())

@bot.command()
async def ai(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Nie wykryto załączonego obrazka")
    else:
        for attachment in ctx.message.attachments:
            await(attachment.save(f"ai_imgs/{attachment.filename}"))
            await ctx.send(bot_logic.detect_trash(f"ai_imgs/{attachment.filename}", "keras_model.h5", "labels.txt"))

@bot.command()
async def kalkulator_info(ctx):
    await ctx.send("Oblicz efektywność energetyczną twojego domu!")
    await ctx.send("Użyj następującej komendy: **$kalkulator X Y Z**")
    await ctx.send("Podaj wielkość swojego domu:\n(A) - mały\n(B) - średni\n(C) - duży")

@bot.command()
async def joe(ctx):
    await ctx.send(f'joe MAMA')
    with open(f'memes\laughter-cartoon.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("hansko")