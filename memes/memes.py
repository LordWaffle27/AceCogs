from redbot.core import commands
import asyncio
import aiohttp
import discord

class Memes(commands.Cog):
    """Retreive the dankest memes Reddit has to offer"""
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
    @commands.command()
    async def memes(self, ctx):
        """Get the dankest memes Reddit has to offer. Soon, you'll be able to specify by subreddit."""
        async with aiohttp.ClientSession() as session:
            url = "https://meme-api.herokuapp.com/gimme"
            async with session.get(url) as response:
                response = await response.json()
            embed = discord.Embed(
                title= response['title'],
                url = response['postLink'],
                color=0x0276FD,
            )
            embed.set_image(url=response['url'])
            embed.set_footer(text=f"r/{response['subreddit']} | Enjoy your dank memes!")
            await ctx.send(embed=embed)
