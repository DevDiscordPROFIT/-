import discord
import asyncio
import datetime
import pytz

bot = discord.Client()
token = "TOKEN"

@bot.event
async def on_ready():
    print("성공적으로 로그인되었습니다.")

@bot.event
async def on_message(ctx):
    if ctx.content.startswith ("!공지"):
        await ctx.channel.purge(limit=1)
        i = (ctx.author.guild_permissions.administrator)
        if i is True:
            notice = ctx.content[4:]
            channel = bot.get_channel(#공지전송채널)
            embed = discord.Embed(title="📢 **공지사항**", description="{}".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x7289DA)
            embed.set_footer(text="공지 발송자: {}".format(ctx.author), icon_url=ctx.author.avatar_url)
            await channel.send ("새로운공지입니다!", embed=embed)
 
        if i is False:
            await ctx.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))


@bot.event
async def on_message(ctx):
    if ctx.content.startswith ("!리붓"):
        await ctx.channel.purge(limit=1)
        i = (ctx.author.guild_permissions.administrator)
        if i is True:
            notice = ctx.content[4:]
            channel = bot.get_channel(#)
            embed = discord.Embed(title="📢 **봇리붓알림**", description="{}".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x7289DA)
            embed.set_footer(text="공지 발송자: {}".format(ctx.author), icon_url=ctx.author.avatar_url)
            await channel.send ("", embed=embed)
 
        if i is False:
            await ctx.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))




bot.run(token)
