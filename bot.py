from pyrogram import Client, filters
import pyshorteners

bot = Client('gplink bot',
             api_id=1212909,
             api_hash='759e1450bdc5857ac302f565b5b6e639',
             bot_token='1760586958:AAECMGgx4gMK74vCnTZuE5b_Dc4Wn6wJyfs',
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        
        "You can watch MxPlayer Content for Free without ads \n For more please Join \n @yssprojects")

@bot.on_message(filters.command('help') & filters.private)
async def help(bot, message):
    await message.reply(
        f"**Help!**\n"
        '''Example Links 👇

        Movie : `https://www.mxplayer.in/movie/watch-kis-kisko-pyaar-karoon-movie-online-c431d9c123b50f3fffc8e479ef119376`
        Episode : `https://www.mxplayer.in/show/watch-aashram/chapter-2/triya-charit-online-a27d0095cc646c7b0fde0825ca570f9c`
        If Any Issue Contact @seshu2004 ''')

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    if "https://www.mxplayer.in/" in link:
        x = link.split("-", -1)
        data = x[-1]
        if "movie" in link:
            ur = "http://sh.st/st/967915bd6c1e9a5720a2989759acc03e/https://mx.tpro.ga/player?id="+data+"&type=movie"
        elif "show" in link:
            ur = "http://sh.st/st/967915bd6c1e9a5720a2989759acc03e/https://mx.tpro.ga/player?id="+data+"&type=episode"
        s = pyshorteners.Shortener()
        mlink = s.qpsru.short(ur)
        await message.reply(
        "Watch Using This Link \n"+ mlink)

bot.run()
