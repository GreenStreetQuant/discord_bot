import discord
import os
from datetime import datetime

client = discord.Client()

"""
channel list 
xrp_channel = 832097265903861791
berpro_min_channel = 832100873483190292
litecoin_hr_channel = 832100924431401020
bepro_hr_channel = 832100970438721577
litecoin_daily_channel = 832101017604456448
"""

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M")

#logging the client into server
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#getting the buy or sell signal from specific server
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel_names = ['xrp','litecoin-1hr','bepro-1hr','litecoin-daily']

    for cn in channel_names:
        if message.channel.name == cn:
            if message.content.startswith('BUY'):
                if cn == 'xrp':

                elif cn == 'litecoin-1hr':

                elif cn == 'bepro-1hr':

                elif cn == 'litecoin-daily':
                
            elif message.content.startswith('SELL'):
                if cn == 'xrp':

                elif cn == 'litecoin-1hr':

                elif cn == 'bepro-1hr':

                elif cn == 'litecoin-daily':

            else:
                return
                
        else:
            return

client.run('')
