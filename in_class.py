import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

def random_url():
    random_number=random.randint(1,10)
    print(random_number)
    if random_number<3:
        random_url= "https://random-d.uk/api/random"
    else:
        random_url="https://random.dog/woof.json"
    return random_url


def get_animal_image_url(animal_url):    
    url = animal_url
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('animal')
async def animal(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_animal_image_url()
    await ctx.send(image_url)

bot.run("")
