import discord
from discord.ext import commands, tasks

import asyncio
import requests
from bs4 import BeautifulSoup 

# import user
import tier_image
import token_id

bot_TOKEN = token_id.bot_TOKEN
guild_id = token_id.guild_id
channel_id = token_id.channel_id

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/',intents=intents)
headers = {'User-Agent':'Mozilla/5.0'}

@tasks.loop(seconds=60)
async def alarm_60():
    cnt = 1
    while True:
        print('\r알람 {}회 실행'.format(cnt), end="")
        cnt+=1
        userid = user.userlist()
        print(userid)
        for id in userid:
            try:
                find_url = "https://www.acmicpc.net/status?problem_id=&user_id="+id+"&language_id=-1&result_id=4"
                 
                resp = requests.get(find_url, headers=headers)

                data = BeautifulSoup(resp.content, 'html.parser')
                contents = data.find('tbody').find_all('tr')
                a = contents[0].find_all('td')
                name = a[2].find('a')['title']
                num = a[2].text
                link = 'https://www.acmicpc.net/problem/'+num
                print(id,user.user_num(id))
                if user.user_num(id) != num:
                    user.change_num(id,num)
                    embed=discord.Embed(title=name, url=link, description=num+"번", color=0x00ff40)
                    embed.set_author(name="맞았습니다!")
                    tierlink = tier_image.get_tier_img(num)
                    embed.set_thumbnail(url=tierlink)
                    embed.add_field(name="제출한 사람", value="["+id+"](https://www.acmicpc.net/user/"+id+")", inline=False)
                    
                    await bot.get_guild(guild_id).get_channel(channel_id).send(embed=embed)
            except Exception as e:
                print("알람 에러")
                print(e)
                continue   
        await asyncio.sleep(60)

@bot.tree.command(name='problemlist')
@discord.app_commands.describe(userid='아이디')
async def problemlist(ctx: discord.interactions.Interaction, userid : str):
    embed = discord.Embed(title=f"{userid} 문제 리스트")
    embed.set_thumbnail(url="https://static.solved.ac/uploads/profile/360x360/jhp98-picture-1700321247648.png")
    embed.add_field(name="문제",value="1001...",inline=False)

    await ctx.response.send_message(embed=embed)



@bot.event
async def on_ready():
    print('Done')
    await bot.tree.sync()
    # bot.loop.create_task(alarm_60())


@bot.tree.command(name='hello',description='say hello')
async def hello(ctx: discord.interactions.Interaction):
    await ctx.response.send_message('Hello I am Bot!')

@bot.tree.command(name='문제리셋',description='유저가 푼 문제 초기화')
async def 문제리셋(ctx: discord.interactions.Interaction):
    user.numreset()
    await ctx.response.send_message('해결한 문제 초기화 완료')    

@bot.tree.command(name='유저목록', description='유저 목록을 보여줍니다')
async def 유저목록(ctx: discord.interactions.Interaction):
    userid = user.userlist()
    embed = discord.Embed(title="유저 정보", color=0x22aedd)
    for id in userid:
        embed.add_field(name=" ",value="["+id+"](https://www.acmicpc.net/user/"+id+")",inline=False)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name='등록', description='새로운 아이디를 등록합니다')
@discord.app_commands.describe(name='아이디')
async def 등록(ctx: discord.interactions.Interaction, name: str):
    find_url = "https://www.acmicpc.net/status?problem_id=&user_id="+name+"&language_id=-1&result_id=4"
    resp = requests.get(find_url, headers=headers)

    data = BeautifulSoup(resp.content, 'html.parser')
    contents = data.find('tbody').find_all('tr')
    a = contents[0].find_all('td')
    
    num = a[2].text
    if user.adduser(name,num):
        find_url = "https://www.acmicpc.net/user/"+name
        resp = requests.get(find_url, headers=headers)

        data = BeautifulSoup(resp.content, 'html.parser')
        contents = data.find('img',class_='solvedac-tier')["src"]
        print(contents)
        embed=discord.Embed(title=" ", color=0x4aeb00)
        embed.set_author(name=name, url="https://www.acmicpc.net/user/"+name)
        # embed.set_thumbnail(url='https://d2gd6pc034wcta.cloudfront.net/tier/16.svg')
        
        embed.add_field(name=" ", value="등록완료", inline=False)
        # embed.add_field(name="", value="["+name+"](https://www.acmicpc.net/user/"+name+")", inline=True)
        await ctx.response.send_message(embed=embed)
    else:
        embed=discord.Embed(title=" ", color=0xef0606)
        embed.set_author(name=name, url="https://www.acmicpc.net/user/"+name)
        embed.add_field(name=" ", value="이미 등록되어 있습니다", inline=False)
        await ctx.response.send_message(embed=embed)

@bot.tree.command(name='알람', description='가장 최근에 푼 문제 출력')
@discord.app_commands.describe(id='아이디')
async def 알람(ctx: discord.interactions.Interaction, id: str):
    find_url = "https://www.acmicpc.net/status?problem_id=&user_id="+id+"&language_id=-1&result_id=4"
    
    resp = requests.get(find_url, headers=headers)

    data = BeautifulSoup(resp.content, 'html.parser')
    contents = data.find('tbody').find_all('tr')
    a = contents[0].find_all('td')
    name = a[2].find('a')['title']
    num = a[2].text
    link = 'https://www.acmicpc.net/problem/'+num
    await ctx.response.send_message('아이디 : {} \n문제 : {}번 {}\n{}'.format(id,num,name,link))

bot.run(bot_TOKEN)