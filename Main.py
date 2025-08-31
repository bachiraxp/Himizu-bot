import discord
import os

# As "intents" são as permissões que o seu bot precisa
intents = discord.Intents.default()
intents.message_content = True

# Cria o cliente do Discord com as intents
client = discord.Client(intents=intents)

# O evento 'on_ready' é ativado quando o bot se conecta com sucesso
@client.event
async def on_ready():
    print(f'Olá! Eu sou o {client.user} e estou online!')

# O bot se conecta usando o token que você vai adicionar no Replit
client.run(os.environ['DISCORD_BOT_TOKEN'])
