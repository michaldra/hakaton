import discord
import bot_logic
import random
import requests
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
    await ctx.send('Wszystkie komendy:\n')
    await ctx.send('**$hello** - Wita się\n')
    await ctx.send('**$bye** - Żegna się\n')
    await ctx.send('**$hehe #** - Pisze "he" # razy\n')
    await ctx.send('**$password #** - Generuje hasło o długości #\n')
    await ctx.send('**$h #** - Pisze "h " # razy\n')
    await ctx.send('**$coin** - Rzuca monetą\n')
    await ctx.send('**$emoji** - Generuje losową emotkę\n')
    await ctx.send('**$dice #** - Rzuca kostką o # ścianach\n')
    await ctx.send('**$guess #** - Zaczyna grę w zgadywanie od 1 do #\n')
    await ctx.send('**$joined** - Pisze kiedy użytkownik dołączył do serwera')
    await ctx.send('**$meme** - Wysyła losowy mem o programowaniu\n')
    await ctx.send('**$dog** - Wysyła losowy obrazek z pieskami\n')
    await ctx.send('**$eko** - Pisze losowy pomysł na zrobienie czegoś ze śmieci\n')

@bot.command()
async def czesc(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}!')

@bot.command()
async def pa(ctx):
    await ctx.send(f'👋')

@bot.command()
async def meme(ctx):
    rng = random.randint(0,99)
    if rng < 50:
        img_name = random.choice(os.listdir('images/common'))
        with open(f'images/common/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Popularny (50%)')
    elif rng < 75:
        img_name = random.choice(os.listdir('images/uncommon'))
        with open(f'images/uncommon/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Niepopularny (25%)')
    elif rng < 90:
        img_name = random.choice(os.listdir('images/rare'))
        with open(f'images/rare/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Rzadki (15%)')
    elif rng < 99:
        img_name = random.choice(os.listdir('images/epic'))
        with open(f'images/epic/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Epicki (9%)')
    else:
        img_name = random.choice(os.listdir('images/legendary'))
        with open(f'images/legendary/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Legendarny (1%)')


@bot.command()
async def pomysl(ctx):
    await ctx.send(bot_logic.pomysl())

@bot.command()
async def ai(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Nie wykryto załączonego obrazka")
    else:
        for attachment in ctx.message.attachments:
            await(attachment.save(f"ai_imgs/{attachment.filename}"))
            await ctx.send(ai_thing.detect_bird(f"ai_imgs/{attachment.filename}", "keras_model.h5", "labels.txt"))
         

bot.run("amogus")