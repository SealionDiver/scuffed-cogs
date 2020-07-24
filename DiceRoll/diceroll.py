from redbot.core import commands
import random
import asyncio

class diceroll(commands.Cog):
    """simple d4, d6, d8, d10, and d20 roller"""

    @commands.command()
    async def d4(self, ctx):
        """Roll a four-sided die"""
        result = random.randint(1, 4)
        await ctx.send(result)

    @commands.command()
    async def d6(self, ctx):
        """Roll a six-sided die"""
        result = random.randint(1, 6)
        await ctx.send(result)
        
    @commands.command()
    async def d8(self, ctx):
        """Roll a eight-sided die"""
        result = random.randint(1, 8)
        await ctx.send(result)

    @commands.command()
    async def d10(self, ctx):
        """Roll a ten-sided die"""
        result = random.randint(1,8)
        await ctx.send(result)

    @commands.command()
    async def d12(self,ctx):
        """Roll a twelve-sided die"""
        result = random.randint(1, 12)
        await ctx.send(result)

    @commands.command()
    async def d20(self, ctx):
        """Roll a twenty-sided die"""
        # Your code will go here
        result = random.randint(1, 20)
        await ctx.send(result)
    
    
    