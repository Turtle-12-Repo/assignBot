# imports
import discord
from discord.ext import commands
from dotenv import dotenv_values

# retrieve token from .env file
env = dotenv_values(".env")
TOKEN = env['DISCORD_TOKEN']                                                                                             # CHANGE WITH SERVER MOVE
GUILD = env['DISCORD_GUILD']

# static var
choice1 = env['CHOICE_1']
choice2 = env['CHOICE_2']
choice3 = env['CHOICE_3']
checker_role = env['CHECKER_ROLE']

# init client
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


# bot command for making the embed and adding three reactions
@bot.command(name="embed", help="Makes embed for auto branch assignment.")
@commands.has_permissions(administrator=True, manage_roles=True)
async def poll(ctx):
    emb = discord.Embed(
        title="Invictus Intergalactic Federation:"
              "\nAutomatic Branch Assignment Procedure:",
        url="https://www.invfed.com/home",
        description="This is a test for INVFED's automation of branch assignment."
                    "\n\n1. Read the branch descriptions."
                    "\n2. React to this message with the corresponding S, O, A emoji for your choice to be made."
                    "\n\nNOTICE: These choices are not permanent, however, we ask that you truly think about which "
                    "branch you would fit into best.",
        color=discord.Color.dark_blue()  # changes color of that little side bar in the embed
    )
    emb.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    emb.add_field(
        name="\n1️⃣ - Starfighter Corps:",
        value='''
                    DESCRIPTION
                    \n''',
        inline=False
    )
    emb.add_field(
        name="\n2️⃣ - Armored Corps:",
        value='''
                    DESCRIPTION
                    \n''',
        inline=False
    )
    emb.add_field(
        name="\n3️⃣ - Operations Corps:",
        value='''
                    DESCRIPTION
                    \n''',
        inline=False
    )
    emb.add_field(
        name="Please choose carefully.",
        value='Thank you.'
    )
    emb.set_image(
        url="https://media.discordapp.net/attachments/764714933400371220/868724710043709450/INVFED_FLEET_GIF.gif")  # that image at the bottom
    emb.set_footer(text="Bot made by turtallius#8013")
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')
    await msg.add_reaction('3️⃣')


# bot even listener to wait for reaction, assign role, remove their reaction, not let them react again
# handle adding role
@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 877109420994203650:  # need to manually enter the specific message id                               # CHANGE WITH SERVER MOVE
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        # assign role based on emoji reaction
        if payload.emoji.name == '1️⃣':
            role = discord.utils.get(guild.roles, name=choice1)                                              # CHANGE WITH SERVER MOVE
        elif payload.emoji.name == '2️⃣':
            role = discord.utils.get(guild.roles, name=choice2)                                                    # CHANGE WITH SERVER MOVE
        elif payload.emoji.name == '3️⃣':
            role = discord.utils.get(guild.roles, name=choice3)                                               # CHANGE WITH SERVER MOVE
        # push role change
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            # check member roles
            enlisted = discord.utils.get(guild.roles, name=checker_role)                                             # CHANGE WITH SERVER MOVE
            if enlisted in member.roles:
                print("Already enlisted.")
            else:
                if member is not None:
                    # add enlisted and branch roles
                    await member.add_roles(role)
                    await member.add_roles(enlisted)
                    print("Success.")
                    print(payload.member.roles)
                else:
                    print("Member not found.")
        else:
            print("Role not found.")


# mains
def main():
    print("Bot is live.")
    bot.run(TOKEN)  # runs the client using token from .env


if __name__ == "__main__":
    main()
