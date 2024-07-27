import hikari
import lightbulb
import pyfiglet
import cowsay

bot = lightbulb.BotApp(token = '******', default_enabled_guilds=(1262226628571041802))


#Welcome Page
@bot.command
@lightbulb.command('fontstart', 'Get_Started!')
@lightbulb.implements(lightbulb.SlashCommand)
async def start(context):
    await context.respond("Welcome to Font Changer!\nModify your texts with this simple bot's shortcuts.\nGet started by entering: /font")

#font help
@bot.command
@lightbulb.command('fonthelp', 'Help_Page')
@lightbulb.implements(lightbulb.SlashCommand)
async def help(context):
    line1 = "Thank you for using Font Changer!!"
    line2  = "To replicate a message:\n1. Copy message from bot\n2. Type: \n\```ansi\n <paste message from bot>\n\```"
    line3 = "Acknowledgements:\n...."
    line4 = "Enjoy!"
    await context.respond(line1 + "\n\n" +line2+ "\n\n" + line3 + "\n" + line4)

#Main Menu
@bot.command
@lightbulb.command('font', 'Main_Menu')
@lightbulb.implements(lightbulb.SlashCommand)
async def menu(context):
    line1 = "Here are a list of commands:"
    line2 = "/fontcolor - change your text color"
    line3 = "/fontart - turn your text into font art"
    line4 = "/cowsay - make a cow talk"
    line5 = "\n\nFor more help, type: /fonthelp"
    await context.respond("```" + line1 + "\n\n" +line2+ "\n" + line3 + "\n" + line4 + line5 + "\n```")

#turns user input into acii font art
@bot.command
#option needs to be aABOVE LB.COMMAND and UNDER BOT.CMD
@lightbulb.option('userinput', 'user message', type=str) #prolly defaults to string but for example purposes
#@lightbulb.option('fonttype', 'Pick a font', type=str)
@lightbulb.command('fontart', 'Text into ACII Art')
@lightbulb.implements(lightbulb.SlashCommand)
async def art(context):
    inputtext = context.options.userinput
    #fonttype = context.options.fonttype
    text = pyfiglet.figlet_format(inputtext)
    await context.respond("```\n" + text + "\n```")

#cowsay bot its on discord
@bot.command
@lightbulb.option('userinput', 'user message', type=str) #prolly defaults to string but for example purposes
#@lightbulb.option('fonttype', 'Pick a font', type=str)
@lightbulb.command('cowsay', 'Make a cow talk')
@lightbulb.implements(lightbulb.SlashCommand)
async def art(context):
    inputtext = context.options.userinput
    #fonttype = context.options.fonttype
    text = cowsay.get_output_string('cow', inputtext)
    await context.respond("```" + text + "```")

####CLOLR

#list of colors
#Main Menu
@bot.command
@lightbulb.command('fontcolor', 'List of text colors')
@lightbulb.implements(lightbulb.SlashCommand)
async def clrmenu(context):
    line1 = "Here are a list of colors: \n\n"
    pink = "\033[35mpink\033[0m\n"
    cyan = "\033[36mcyan\033[0m"
    red = "\033[31mred\033[0m\n"
    green = "\033[32mgreen\033[0m\n"
    yellow = "\033[33myellow\033[0m\n"
    blue = "\033[34mblue\033[0m\n"
    example = "\n\nType: /clr <color> <message>"
    await context.respond("```ansi\n" + line1 + red + pink + yellow + green + blue + cyan + example + "\n```")

#make groups
@bot.command
@lightbulb.command('clr', 'Group of colors')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def color(context):
    pass

#red
@bot.command
@color.child
@lightbulb.option('message', 'user send word', type=str)
@lightbulb.command("red", "turns text red")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clr(context):
    inputtext = context.options.message
    await context.respond("```ansi\n" + "\033[31m" + inputtext + "\033[0m" + "\n```")

#green
@bot.command
@color.child
@lightbulb.option('message', 'user send word', type=str)
@lightbulb.command("green", "turns text green")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clr(context):
    inputtext = context.options.message
    await context.respond("```ansi\n" + "\033[32m" + inputtext + "\033[0m" + "\n```")

#yellow
@bot.command
@color.child
@lightbulb.option('message', 'user send word', type=str)
@lightbulb.command("yellow", "turns text yellow")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clr(context):
    inputtext = context.options.message
    await context.respond("```ansi\n" + "\033[33m" + inputtext + "\033[0m" + "\n```")

#blue
@bot.command
@color.child
@lightbulb.option('message', 'user send word', type=str)
@lightbulb.command("blue", "turns text blue")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clr(context):
    inputtext = context.options.message
    await context.respond("```ansi\n" + "\033[34m" + inputtext + "\033[0m" + "\n```")

#pink
@bot.command
@color.child
@lightbulb.option('message', 'user send word', type=str)
@lightbulb.command("pink", "turns text pink")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clr(context):
    inputtext = context.options.message
    await context.respond("```ansi\n" + "\033[35m" + inputtext + "\033[0m" + "\n```")

#Cyan
@bot.command
@color.child
@lightbulb.option('message', 'user send word', type=str)
@lightbulb.command("cyan", "turns text cyan")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def clr(context):
    inputtext = context.options.message
    await context.respond("```ansi\n" + "\033[36m" + inputtext + "\033[0m" + "\n```")

bot.run()