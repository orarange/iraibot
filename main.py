import os
import discord
from discord.app_commands import CommandTree
from discord import Intents, Client, Interaction, Member, ButtonStyle
from discord.ext import tasks
import datetime
import asyncio
from discord.ext.tasks import loop

class MyClient(Client):
    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()


intents = Intents.default()
client = MyClient(intents=intents)

#四則演算
@client.tree.command()
async def calc(interaction: Interaction, a:str, b: int, c: int):
    if a == "+":
        await interaction.response.send_message(f"{b} + {c} = {b + c}")
    elif a == "-":
        await interaction.response.send_message(f"{b} - {c} = {b - c}")
    elif a == "*":
        await interaction.response.send_message(f"{b} * {c} = {b * c}")
    elif a == "/":
        await interaction.response.send_message(f"{b} / {c} = {b / c}")
    else:
        await interaction.response.send_message(f"計算できません")

@loop(count=None)
async def send_message():
    # 現在の曜日を取得する
    today = datetime.datetime.now().weekday()

    # 月曜日であれば、メッセージを送信する
    if today == 0:
        # チャンネルを取得する
        channel = client.get_channel("")

        # メッセージを送信する
        await channel.send("今日は月曜日です！")

send_message.start()

client.run()