import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "22663254")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "8b4160634727b3d63c51c63e1cdcbd06")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7203938689:AAGJMHD-pOvIGQP29ifN7RNRbl0OxgtcMc0") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://autorenamev2:WoNI30mnh7hUtPUz@cluster0.9xhdp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/b8cb11aa0a8075d855612.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7062828064').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'AshutoshGoswami24,BotzPW,PandaWep').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001869105126"))
    PORT = int(os.environ.get("PORT", "8899"))
    

    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

➻ Use /metadata Command To Use Metadata

➻ <code>/setmedia video<code> To Upload File In Video Format

<b>Bot Is Made By @AshutoshGoswami24</b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code>/autorename Naruto Shippuden [quality]  [episode] [hinid] @AshuSupport</code>

<b>➻ Your Current Auto Rename Format :<code>{format_template}</code></b> """ 
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/BotzPW'>PW Botz</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/AshutoshGoswami24'>Asʜᴜᴛᴏsʜ Gᴏsᴡᴀᴍɪ 𝟸𝟺 🇮🇳</a>
    
<b>♻️ Bot Made By :</b> @AshutoshGoswami24"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @AshutoshGoswami24
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - PandaWep@ybl</b>"""
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @AshutoshGoswami24 To Help """

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:

◦ <code>Telegram : @AshutoshGoswami24</code>
"""



# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @AshutoshGoswami24
# Developer @AshutoshGoswami24
