import discord
from discord.ext import commands
import io

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

def obfuscate_lua(code: str) -> str:
    encoded_parts = []
    for char in code:
        encoded_parts.append(str(ord(char)))
    obfuscated = 'loadstring("' + '\\'.join(encoded_parts) + '")()'
    return obfuscated

@bot.command(name='obf')
async def obfuscate(ctx):
    await ctx.send("Please send the Lua script to obfuscate (paste text or upload .lua/.txt file).")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await bot.wait_for('message', check=check, timeout=60.0)
    except Exception:
        return await ctx.send("Timeout, please try again.")
    
    raw_code = ""
    
    if msg.attachments:
        attachment = msg.attachments[0]
        file_bytes = await attachment.read()
        raw_code = file_bytes.decode('utf-8', errors='ignore')
    else:
        raw_code = msg.content
    
    if not raw_code.strip():
        return await ctx.send("No valid code content detected.")
    
    result_code = obfuscate_lua(raw_code)
    
    await ctx.send("✅ Obfuscation successful! Check the `.lua` file below.")
    
    file = discord.File(
        fp=io.BytesIO(result_code.encode('utf-8')),
        filename="obfuscated.lua"
    )
    await ctx.send(file=file)

bot.run('MTU2MzIwMDA1ODQwMzU5MDE3Ng.GyGMDp.YICH8IgHqfUDdfwTZjEUrdq4YpjZuwM6i3OaV0')
