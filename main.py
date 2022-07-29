import string
import asyncio

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

from api_keys import *

intents = discord.Intents.default()

client = commands.Bot(command_prefix = '!', intents = intents)

file_names = [
    {'names': ['1', 'yes'], 'file_name': 'Yes'},
    {'names': ['2', 'no'], 'file_name': 'No'},
    {'names': ['3', 'food please'], 'file_name': 'Food_please'},
    {'names': ['4', 'wood please'], 'file_name': 'Wood_please'},
    {'names': ['5', 'gold please'], 'file_name': 'Gold_please'},
    {'names': ['6', 'stone please'], 'file_name': 'Stone_please'},
    {'names': ['7', 'ah', 'ahh', 'ahhh', 'ahhhh', 'ahhhhh'], 'file_name': 'Ahh'},
    {'names': ['8', 'all hail king of the losers', 'all hail', 'king of the losers'], 'file_name': 'All_hail'},
    {'names': ['9', 'oh', 'ooh', 'oooh', 'ooooh', 'oooooh'], 'file_name': 'Oooh'},
    {'names': ['10', 'ill beat you back to age of empires', 'ill beat you', 'back to age one'], 'file_name': 'Back_to_age_one'},
    {'names': ['11', 'laugh', 'herb laugh', 'haha', 'hahaha', 'hahahaha'], 'file_name': 'Herb_laugh'},
    {'names': ['12', 'aah being rushed', 'aa being rushed', 'being rushed', 'aaah being rushed'], 'file_name': 'Being_rushed'},
    {'names': ['13', 'sure blame it on your isp', 'blame it on your isp', 'blame your isp', 'isp'], 'file_name': 'Blame_your_isp'},
    {'names': ['14', 'start the game already', 'start the game'], 'file_name': 'Start_the_game'},
    {'names': ['15', 'dont point that thing at me', 'dont point that thing'], 'file_name': 'Dont_point_that_thing'},
    {'names': ['16', 'enemy sighted'], 'file_name': 'Enemy_sighted'},
    {'names': ['17', 'it is good to be the king', 'good to be the king', 'it is good', 'its good to be the king', 'it is good to be king', 'its good to be king'], 'file_name': 'It_is_good'},
    {'names': ['18', 'monk i need a monk', 'i need a monk', 'monk'], 'file_name': 'I_need_a_monk'},
    {'names': ['19', 'long time no siege', 'no siege', 'long time'], 'file_name': 'Long_time_no_siege'},
    {'names': ['20', 'my granny could scrap better than that', 'my granny'], 'file_name': 'My_granny'},
    {'names': ['21', 'nice town ill take it', 'nice town'], 'file_name': 'Nice_town'},
    {'names': ['22', 'quit touchin me', 'quit touchin'], 'file_name': 'Quit_touchin'},
    {'names': ['23', 'raiding party'], 'file_name': 'Raiding_party'},
    {'names': ['24', 'dadgum'], 'file_name': 'Dadgum'},
    {'names': ['25', 'eh smite me', 'ehh smite me', 'smite me'], 'file_name': 'Smite_me'},
    {'names': ['26', 'the wonder the wonder no', 'the wonder no', 'the wonder'], 'file_name': 'The_wonder'},
    {'names': ['27', 'you played two hours to die like this', 'two hours'], 'file_name': 'You_play_two_hours'},
    {'names': ['28', 'yeah well you should see the other guy', 'you should see the other guy'], 'file_name': 'You_should_see_the_other_guy'},
    {'names': ['29', 'rogan', 'roggan'], 'file_name': 'Roggan'},
    {'names': ['30', 'wololo', 'wolo'], 'file_name': 'Wololo'},
    {'names': ['31', 'attack an enemy now', 'attack'], 'file_name': 'Attack_an_enemy_now'},
    {'names': ['32', 'cease creating extra villagers', 'stop creating extra villagers'], 'file_name': 'Cease_creating_extra_villagers'},
    {'names': ['33', 'create extra villagers', 'create villagers'], 'file_name': 'Create_extra_villagers'},
    {'names': ['34', 'build a navy'], 'file_name': 'Build_a_navy'},
    {'names': ['35', 'stop building a navy'], 'file_name': 'Stop_building_a_navy'},
    {'names': ['36', 'wait for my signal to attack', 'wait'], 'file_name': 'Wait_for_my_signal_to_attack'},
    {'names': ['37', 'build a wonder', 'wonder'], 'file_name': 'Build_a_wonder'},
    {'names': ['38', 'give me your extra resources', 'extra resources'], 'file_name': 'Give_me_your_extra_resources'},
    {'names': ['39', 'ally'], 'file_name': 'Ally'},
    {'names': ['40', 'neutral'], 'file_name': 'Neutral'},
    {'names': ['41', 'enemy'], 'file_name': 'Enemy'},
    {'names': ['42', 'what age are you in', 'what age'], 'file_name': 'What_age_are_you_in'}
]

time = 0

def is_connected (ctx):

    voice_client = ctx.voice_client
    return voice_client and voice_client.is_connected()

def get_audio_path (given_name):

    clean_name = given_name.translate(str.maketrans('', '', string.punctuation)).lower()

    for f in file_names:

        names = f['names']

        for n in names:

            if (clean_name == n):

                return 'Taunts/' + f['file_name'] + '.mp3'


@client.event
async def on_ready():

    print('Bot ready')
    print('-----------------------')

    await client.change_presence(status=discord.Status.online, activity=discord.Game('Age of Empires II: Definitive Edition'))

@client.command(pass_context = True)
async def aoe (ctx, *args):

    if (args[0] == 'help' or args[0] == 'list' or args[0] == 'h' or args[0] == 'l'):

        print('Listing taunts')

        text = 'Type `!aoe [number/taunt]` and I\'ll join your voice channel and say it.\nI allow for some variations (e.g. `What age are you in?` or `What age?`).\n'
        text += '```'

        for f in file_names:

            names = f['names']
            text += names[0] + ' - ' + names[1] + '\n'

        text += '```'

        await ctx.send(text)

        return

    if (len(args) == 0) :

        given_name = 'wololo'

    else:

        given_name = ' '.join(args)

    path = get_audio_path(given_name)

    if (path == None):

        await ctx.send('Can\'t find that clip!')
        return

    voice_client = ctx.voice_client

    if (not voice_client):

        print('Joining channel')

        if (ctx.author.voice):

            channel = ctx.message.author.voice.channel
            voice_client = await channel.connect()

        else:

            print('User not in a voice channel so couldn\'t join')
            return

    print('Playing ' + path)

    source = FFmpegPCMAudio(path)
    player = voice_client.play(source)

@client.command(pass_context = True)
async def leave(ctx):

    if (ctx.voice_client):

        print('Leaving voice channel')
        await ctx.guild.voice_client.disconnect()

    else:

        print('Not in a voice channel')

@client.event
async def on_voice_state_update(member, before, after):

    voice_state = member.guild.voice_client

    if voice_state is None:

        return 

    if len(voice_state.channel.members) == 1:

        await voice_state.disconnect()

client.run(BOT_TOKEN)
