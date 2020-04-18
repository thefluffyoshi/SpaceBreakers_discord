import discord
import time
import asyncio
#id = 599461294428520490
#messages = joined = 0

client = discord.Client()

#async def update_stats():
    #await client.wait_until_ready()
    #global messages, joined

    #while not client.is_closed():
        #try:
            #with open("stats.txt", "a") as f:
                #f.write(f"""Time: {int (time.time())}, Messages: {messages}, Members Joined: {joined}\n""")
            #messages = 0
            #joined = 0
            #await asyncio.sleep(5)
        #except Exception as e:
            #print(e)
            #await asyncio.sleep(5)

@client.event
async def on_member_join(member):
    #global joined
    #joined += 1

    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await client.send_message(f"""Welcome to Space Breakers {member.mention}""")

@client.event
async def on_message(message):
    #global messages
    #messages += 1
    id = client.get_guild(599461294428520490)
    channels = ["test", "bot-spam", "bot-spam-2", "test-2", "welcome"]
    valid_users = ["thefluffyoshi#6195", "friend#5869", "adria#9936", "silver~#2010", "raisinbran#6564", "clxudy#6666"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("/hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "/users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
#    else:
#        print(f"""User: {message.author} tried to do command {message.content}, in channel {message.channel}""")

#client.loop.create_task(update_stats())
client.run("Njk0NDE4MDAxOTM5OTIyOTc2.Xpf1eA.OnXLj7lVjycEkhrerDO4v36f27s")