import discord
import asyncio
import random
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("와우봇 가동중입니다")
    game = discord.Game("대화중")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요 와우봇입니다 도움이 필요하시면 와우봇 도움이라고 말해주세요!")
    if message.content.startswith("!도움"):
        embed = discord.Embed(title="도움말들", description="!안녕 = 안녕이라고 말합니다 \n !도움 = 도움말들을 알려줍니다 \n !정보 = 서버 정보와 내 정보를 알려줍니다.", color=0x00ff00)
        embed.set_footer(text="문의 = ༺ৡ『𝒽𝓸𝓊𝓁𝒹𝒶𝓎』ৡ༻#6057 ")
        await message.channel.send("", embed=embed)
    if message.content.startswith("쓸때 없는 빠빠.png"):
        pic = message.content.split(" ") [1]
        await message.channel.send(file=discord.File(pic))
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일" + str(date.hour) + "시간" + str(date.minute) + "분", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)




client.run("your token")