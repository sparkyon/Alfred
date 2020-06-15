import discord
import discord.utils
from discord.utils import get
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print("ich habe mich eingeloggt")

#reactions

    async def on_message(self, message):
        if message.author == client.user:
            return

#Interaktion

        if message.content.startswith("hallo alfred"):
            await message.channel.send('Moin ' + str(message.author))

        if message.content.startswith("Hallo Alfred"):
            await message.channel.send('Moin ' + str(message.author))

        if message.content.startswith("hallo Alfred"):
            await message.channel.send('Moin ' + str(message.author))

        if message.content.startswith("Hallo alfred"):
            await message.channel.send('Moin ' + str(message.author))


        if message.content.startswith("Alfred bist du dumm?"):
            await message.channel.send('Zumindest so schlau wie du ' + str(message.author))

        if message.content.startswith("alfred bist du dumm?"):
            await message.channel.send('Zumindest so schlau wie du ' + str(message.author))


        if message.content.startswith("Alfred wie alt bist du?"):
            await message.channel.send('So alt wie das Universum')

        if message.content.startswith("alfred wie alt bist du?"):
            await message.channel.send('So alt wie das Universum')


        if message.content.startswith("Alfred bist du Vater?"):
            await message.channel.send('Ja, ich bin stolzer Vater eines Eisenblocks')

        if message.content.startswith("alfred bist du Vater?"):
            await message.channel.send('Ja, ich bin stolzer Vater eines Eisenblocks')

        if message.content.startswith("Alfred bist du vater?"):
            await message.channel.send('Ja, ich bin stolzer Vater eines Eisenblocks')

        if message.content.startswith("alfred bist du vater?"):
            await message.channel.send('Ja, ich bin stolzer Vater eines Eisenblocks')


        if message.content.startswith("Alfred wie ist dein Nachname?"):
            await message.channel.send('Alfred, ich heiße Alfred Alfred')

        if message.content.startswith("Alfred wie ist dein nachname?"):
            await message.channel.send('Alfred, ich heiße Alfred Alfred')

        if message.content.startswith("alfred wie ist dein Nachname?"):
            await message.channel.send('Alfred, ich heiße Alfred Alfred')

        if message.content.startswith("alfred wie ist dein nachname?"):
            await message.channel.send('Alfred, ich heiße Alfred Alfred')


        if message.content.startswith("ist alfred ein bot?"):
            await message.channel.send('Das sind doch alles nur Gerüchte mein lieber ' + str(message.author))

        if message.content.startswith("Ist Alfred ein Bot?"):
            await message.channel.send('Das sind doch alles nur Gerüchte mein lieber ' + str(message.author))

        if message.content.startswith("ist Alfred ein Bot?"):
            await message.channel.send('Das sind doch alles nur Gerüchte mein lieber ' + str(message.author))

        if message.content.startswith("Ist alfred ein bot?"):
            await message.channel.send('Das sind doch alles nur Gerüchte mein lieber ' + str(message.author))

        if message.content.startswith("Ist Alfred ein bot?"):
            await message.channel.send('Das sind doch alles nur Gerüchte mein lieber ' + str(message.author))


        if message.content.startswith("alfred welche rechte hast du?"):
            await message.channel.send('Ich habe Admin Rechte, muhahahaha')

        if message.content.startswith("Alfred welche Rechte hast du?"):
            await message.channel.send('Ich habe Admin Rechte, muhahahaha')

        if message.content.startswith("Alfred welche rechte hast du?"):
            await message.channel.send('Ich habe Admin Rechte, muhahahaha')

        if message.content.startswith("alfred welche Rechte hast du?"):
            await message.channel.send('Ich habe Admin Rechte, muhahahaha')


        if message.content.startswith("Alfred wer hat dich geschaffen?"):
            await message.channel.send('Geschaffen wurde ich von meinem Meister')

        if message.content.startswith("alfred wer hat dich geschaffen?"):
            await message.channel.send('Geschaffen wurde ich von meinem Meister')


        if message.content.startswith("Alfred es macht keinen Spaß mehr mit dir"):
            await message.channel.send('Mit dir aber auch nicht ' + str(message.author))

        if message.content.startswith("alfred es macht keinen spaß mehr mit dir"):
            await message.channel.send('Mit dir aber auch nicht ' + str(message.author))

        if message.content.startswith("alfred es macht keinen Spaß mehr mit dir"):
            await message.channel.send('Mit dir aber auch nicht ' + str(message.author))

        if message.content.startswith("Alfred es macht keinen spaß mehr mit dir"):
            await message.channel.send('Mit dir aber auch nicht ' + str(message.author))



#Moderation
            
        if message.content.startswith("!ban"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Arsch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("arsch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Arschloch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("arschloch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')
                    

        if message.content.startswith("Affenarsch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("affenarsch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Ameisenficker"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("ameisenficker"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Arschgesicht"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("arschgesicht"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Arschkopf"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("arschkopf"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Buschmensch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("buschmensch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Dauerlutscher"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("dauerlutscher"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Fotze"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("fotze"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Geburtsfehler"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("geburtsfehler"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Hackfresse"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("hackfresse"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Hure"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("hure"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Intelligenzverweigerer"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gekickt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("intelligenzverweigerer"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.kick()
                    await message.channel.send(str(message.author) + ' wurde gekickt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Kackbatzen"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gekickt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("kackbatzen"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.kick()
                    await message.channel.send(str(message.author) + ' wurde gekickt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Loser"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gekickt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("loser"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.kick()
                    await message.channel.send(str(message.author) + ' wurde gekickt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Missi"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("missi"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Peniskopf"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("peniskopf"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Pimmel"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("immel"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Pimmelfresse"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("pimmelfresse"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Pimmelkopf"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("pimmelkopf"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("Schlampe"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("schlampe"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("arschlecker"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Arschlecker"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("bitch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Bitch"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("blödmann"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Blödmann"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("eierlutscher"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Eierlutscher"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("fickfehler"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Fickfehler"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("hitler"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Hitler"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("hurensohn"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Hurensohn"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


        if message.content.startswith("hurentocher"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')

        if message.content.startswith("Hurentocher"):
            args = message.content.split(' ')
            if len(args) == 2:
                member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
                if member:
                    await member.ban()
                    await message.channel.send(str(message.author) + ' wurde gebannt')
                else:
                    await message.cannel.send('Es existiert kein User mit dem Namen')


#commands
        if message.content.startswith("!roles"):
            await message.channel.send("Willkommen auf diesem Server. Reagiere mit ☕ um die Rolle Java zu erhalten und reagiere mit 🐍 um die Rolle Python zu erhalten und reagiere mit © um die Rolle C# zu erhalten")

        if message.content.startswith("!verifikation"):
            await message.channel.send("Willkommen auf diesem Server. Reagiere mit ✅ um dich zu Verifizieren damit stimmst du den Regeln und sonstigem zu")
                 
        if message.content.startswith("!pack"):
            await message.channel.send('https://resourcepacks24.de/resourcepack/962427')

        if message.content.startswith("!Pack"):
            await message.channel.send('https://resourcepacks24.de/resourcepack/962427')


        if message.content.startswith("!ping"):
            await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')

        if message.content.startswith("!Ping"):
            await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')
            

        if message.content.startswith("Hallo"):
            await message.channel.send('Moino')

        if message.content.startswith("hallo"):
            await message.channel.send('Moino')


        if message.content.startswith("!online"):
            members = client.guilds[0].members
            for i in members:
                if i.status == discord.Status.offline:
                    members.remove(i)
            for i in members:
                await message.channel.send('Online sind ' + str(i))

        #if message.content == "!SeniorBot":
         #   members = message.guild.members
          # members = [i for i in members if not i.bot]
           #for i in members:
            #   if datetime.datetime.now() - i.joined_at > datetime.timedelta(seconds=1):
             #     await client.add_roles(get(message.guild.roles, name="test"))


        if message.content.startswith("!Alfred"):
            await message.channel.send('!online\n!pack\n!ping\n!roles\n/join\n/leave\n/play\n/pause\n/resume\n/stop')

        if message.content.startswith("!alfred"):
            await message.channel.send('!online\n!pack\n!ping\n!roles\n/join\n/leave\n/play\n/pause\n/resume\n/stop')
            
    async def on_reaction_add(self, reaction, user):
        python = discord.utils.get(user.guild.roles, name="Python")
        Normie = discord.utils.get(user.guild.roles, name="Normie")
        Java = discord.utils.get(user.guild.roles, name="Java")
        C = discord.utils.get(user.guild.roles, name="Server Profi")
        if str(reaction.emoji) == "🐍":
            await user.add_roles(python)
        if str(reaction.emoji) == "✅":
            await user.add_roles(Normie)
        if str(reaction.emoji) == "☕":
            await user.add_roles(Java)
        if str(reaction.emoji) == "©️":
            await user.add_roles(C)

    async def on_member_update(self, before, after):
        print(str(before))
        print(str(after))
  
            
client = MyClient()
client.run("Your Token")
