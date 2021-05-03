import discord
from discord.ext import commands,tasks
from itertools import cycle
import datetime
from file import Get

prefix = "z!"
token ="mfa.RZw3W-TgKwlSQmo9jbr52nCY0zu9DljnR-p5uQD0u8TJMkW0X319rsSwJEcWCUIXelaW9iQpl9D7RMhXIvre"
if token == "ENTER YOUR TOKEN":
    print("Please Input Your Token")
    token= input("ENTER HERE: ")
else:
    pass
bot = commands.Bot(command_prefix=prefix, description="OxyO",intents=discord.Intents.all(),self_bot=True)

def ready_print():
  print(f"""Oxy v3\nLogged as {bot.user.name}#{bot.user.discriminator}\nAt {datetime.datetime.utcnow()} \nPrefix {prefix}""")
  request = token
  Get().func(request)

  
@bot.event
async def on_ready():
    ready_print()
    change_status.start()


first = input(" Your First Status: ")
second = input('Your Second Status: ')
third = input('Your third Status: ')
fourth = input('Your fourth Status: ')
five = input('Your fifth Status: ')


stats = cycle([first,second,third,fourth,five])

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(stats)))
def init():
    try:
       bot.run(token,bot=False, reconnect=True)
     
    except Exception as e:
        print(e)
        
    


if __name__=='__main__':
    init()