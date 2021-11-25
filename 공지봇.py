import discord
import asyncio
import datetime
import pytz

bot = discord.Client()
token = "토큰"
channel = # 채널 id (int)


@bot.event
async def on_ready():
    print("성공적으로 로그인되었습니다.")


@bot.event
async def on_message(ctx):
    global channel
    if ctx.content.startswith("!공지"):
        await ctx.channel.purge(limit=1)
        if ctx.author.guild_permissions.administrator is True:
            embed = discord.Embed(title="📢 **공지사항**", description="{}".format(
                ctx.content[4:]), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x7289DA)
            embed.set_footer(text="공지 발송자: {}".format(
                ctx.author), icon_url=ctx.author.avatar_url)
            await bot.get_channel(channel).send("새로운공지입니다!", embed=embed)
        else:
            await ctx.channel.send(f"{ctx.author.mention}, 당신은 관리자가 아닙니다")

    elif ctx.content.startswith("!리붓"):
        await ctx.channel.purge(limit=1)
        i = (ctx.author.guild_permissions.administrator)
        if i is True:
            embed = discord.Embed(title="📢 **봇리붓알림**", description="{}".format(
                ctx.content[4:]), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x7289DA)
            embed.set_footer(text="공지 발송자: {}".format(
                ctx.author), icon_url=ctx.author.avatar_url)
            await bot.get_channel(channel).send("", embed=embed)
        else:
            await ctx.channel.send(f"{ctx.author.mention}, 당신은 관리자가 아닙니다")

bot.run(token)
