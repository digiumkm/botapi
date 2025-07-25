import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from telegram.constants import ParseMode


TOKEN = '8011757519:AAGdvaZX97PettdeBXvZoBjojsmcN14fk2s'
CHANNEL_IDS = ['-1002594953237', '-1002495716480','-1002373443980','-1002432716701','-4860688705']  # Tambahkan ID channel lain di sini

bot = Bot(token=TOKEN)

# Post: [Senin, Selasa, ..., Minggu][Jam ke-1, ke-2, ke-3]
weekly_posts = {
"monday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "𝐔𝐧𝐭𝐮𝐤 𝐒𝐞𝐦𝐮𝐚 𝐌𝐞𝐦𝐛𝐞𝐫 𝐒𝐞𝐭𝐢𝐚 𝐀𝐏𝐈𝟐𝟖𝟖 𝐘𝐚𝐧𝐠 𝐓𝐞𝐫𝐡𝐨𝐫𝐦𝐚𝐭 : 𝐒𝐚𝐚𝐭 𝐈𝐧𝐢 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐒𝐞𝐝𝐚𝐧𝐠 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍.𝐌𝐨𝐡𝐨𝐧 𝐌𝐚𝐚𝐟 𝐔𝐧𝐭𝐮𝐤 𝐁𝐞𝐫𝐬𝐚𝐛𝐚𝐫 𝐌𝐞𝐧𝐮𝐧𝐠𝐠𝐮 𝐒𝐚𝐦𝐩𝐚𝐢 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐒𝐞𝐥𝐞𝐬𝐚𝐢.  🙏🏼",
        "image_url": "https://i.imgur.com/w5iMTVp.png",
        "time": "09:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐊𝐚𝐦𝐢 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐬𝐢𝐤𝐚𝐧 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍 𝐬𝐮𝐝𝐚𝐡 𝐒𝐞𝐥𝐞𝐬𝐚𝐢. 𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐭𝐞𝐥𝐚𝐡 𝐦𝐞𝐧𝐮𝐧𝐠𝐠𝐮🙏🏼",
        "image_url": "https://i.imgur.com/FARXGVf.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐃𝐀𝐍 𝐁𝐎𝐍𝐔𝐒 𝐁𝐄𝐑𝐋𝐈𝐌𝐏𝐀𝐇",
        "image_url": "https://i.postimg.cc/50FRnn3p/YREYER4.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.postimg.cc/WzGfPzxk/bwqebqw.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
     {
        "channel_id": -1002312224443,
        "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟏𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
        "image_url": "https://i.postimg.cc/vB5BjFfC/tewbt.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
 {
        "channel_id": -1002312224443,
        "text": "𝐔𝐧𝐭𝐮𝐤 𝐒𝐞𝐦𝐮𝐚 𝐌𝐞𝐦𝐛𝐞𝐫 𝐒𝐞𝐭𝐢𝐚 𝐀𝐏𝐈𝟐𝟖𝟖 𝐘𝐚𝐧𝐠 𝐓𝐞𝐫𝐡𝐨𝐫𝐦𝐚𝐭 : 𝐒𝐚𝐚𝐭 𝐈𝐧𝐢 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐒𝐞𝐝𝐚𝐧𝐠 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍.𝐌𝐨𝐡𝐨𝐧 𝐌𝐚𝐚𝐟 𝐔𝐧𝐭𝐮𝐤 𝐁𝐞𝐫𝐬𝐚𝐛𝐚𝐫 𝐌𝐞𝐧𝐮𝐧𝐠𝐠𝐮 𝐒𝐚𝐦𝐩𝐚𝐢 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐒𝐞𝐥𝐞𝐬𝐚𝐢.  🙏🏼",
        "image_url": "https://i.imgur.com/w5iMTVp.png",
        "time": "09:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐊𝐚𝐦𝐢 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐬𝐢𝐤𝐚𝐧 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍 𝐬𝐮𝐝𝐚𝐡 𝐒𝐞𝐥𝐞𝐬𝐚𝐢. 𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐭𝐞𝐥𝐚𝐡 𝐦𝐞𝐧𝐮𝐧𝐠𝐠𝐮🙏🏼",
        "image_url": "https://i.imgur.com/FARXGVf.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐃𝐀𝐍 𝐁𝐎𝐍𝐔𝐒 𝐁𝐄𝐑𝐋𝐈𝐌𝐏𝐀𝐇",
        "image_url": "https://i.postimg.cc/50FRnn3p/YREYER4.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.postimg.cc/WzGfPzxk/bwqebqw.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
{
        "channel_id": -1002432716701,
        "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟏𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
        "image_url": "https://i.postimg.cc/vB5BjFfC/tewbt.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },



    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "𝐒𝐎𝐋𝐔𝐒𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈𝐍𝐘𝐀!",
        "image_url": "https://i.imgur.com/EFAmcrI.jpeg",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
     {
        "channel_id": -4820852926,
        "text": "𝐁𝐄𝐑𝐁𝐔𝐑𝐔 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐄𝐑𝐒𝐀𝐌𝐀 𝐀𝐏𝐈𝟐𝟖𝟖, 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐂𝐔𝐀𝐍 𝐓𝐈𝐀𝐃𝐀 𝐇𝐄𝐍𝐓𝐈 𝐃𝐈 𝐒𝐋𝐎𝐓 𝐆𝐀𝐂𝐎𝐑 𝐀𝐏𝐈𝟖𝟖",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },

    # ===== Channel 3 APINAGA -1002373443980 =====
    {
        "channel_id": -1002373443980,
        "text": "𝐔𝐧𝐭𝐮𝐤 𝐒𝐞𝐦𝐮𝐚 𝐌𝐞𝐦𝐛𝐞𝐫 𝐒𝐞𝐭𝐢𝐚 𝐀𝐏𝐈𝐍𝐀𝐆𝐀 𝐘𝐚𝐧𝐠 𝐓𝐞𝐫𝐡𝐨𝐫𝐦𝐚𝐭 : 𝐒𝐚𝐚𝐭 𝐈𝐧𝐢 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐒𝐞𝐝𝐚𝐧𝐠 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍.𝐌𝐨𝐡𝐨𝐧 𝐌𝐚𝐚𝐟 𝐔𝐧𝐭𝐮𝐤 𝐁𝐞𝐫𝐬𝐚𝐛𝐚𝐫 𝐌𝐞𝐧𝐮𝐧𝐠𝐠𝐮 𝐒𝐚𝐦𝐩𝐚𝐢 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐒𝐞𝐥𝐞𝐬𝐚𝐢.  🙏🏼",
        "image_url": "https://i.imgur.com/f2ncYpr.png",
        "time": "09:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002373443980,
        "text": "𝐊𝐚𝐦𝐢 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐬𝐢𝐤𝐚𝐧 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍 𝐬𝐮𝐝𝐚𝐡 𝐒𝐞𝐥𝐞𝐬𝐚𝐢. 𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐭𝐞𝐥𝐚𝐡 𝐦𝐞𝐧𝐮𝐧𝐠𝐠𝐮🙏🏼",
        "image_url": "https://i.imgur.com/36a2URR.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐘𝐀𝐍𝐆 𝐆𝐀𝐂𝐎𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐋𝐔𝐍𝐀𝐒",
            "image_url": "https://i.postimg.cc/ZnSVjZ0K/YHREY.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/T1JQ4SWj/r32g.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
        {
        "channel_id": -1002373443980,
            "text": "𝐌𝐀𝐊𝐈𝐍 𝐔𝐍𝐓𝐔𝐍𝐆 𝐀𝐍𝐓𝐈 𝐁𝐔𝐍𝐓𝐔𝐍𝐆. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐒𝐄𝐑𝐔𝐍𝐘𝐀 𝐁𝐄𝐑𝐌𝐀𝐈𝐍 𝐃𝐈 𝐀𝐏𝐈𝐍𝐀𝐆𝐀",
            "image_url": "https://i.postimg.cc/wBV4k3br/RTHY7.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
              # ===== Channel 3 BOSKU33 -1002568434905 =====
               {
        "channel_id": -1002568434905,
        "text": "𝐔𝐧𝐭𝐮𝐤 𝐒𝐞𝐦𝐮𝐚 𝐌𝐞𝐦𝐛𝐞𝐫 𝐒𝐞𝐭𝐢𝐚 𝐁𝐎𝐒𝐊𝐔𝟑𝟑 𝐘𝐚𝐧𝐠 𝐓𝐞𝐫𝐡𝐨𝐫𝐦𝐚𝐭 : 𝐒𝐚𝐚𝐭 𝐈𝐧𝐢 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐒𝐞𝐝𝐚𝐧𝐠 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍.𝐌𝐨𝐡𝐨𝐧 𝐌𝐚𝐚𝐟 𝐔𝐧𝐭𝐮𝐤 𝐁𝐞𝐫𝐬𝐚𝐛𝐚𝐫 𝐌𝐞𝐧𝐮𝐧𝐠𝐠𝐮 𝐒𝐚𝐦𝐩𝐚𝐢 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐒𝐞𝐥𝐞𝐬𝐚𝐢.  🙏🏼",
        "image_url": "https://i.imgur.com/BCl6Rn9.png",
        "time": "09:02",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
              
  {
        "channel_id": -1002568434905,
        "text": "𝐊𝐚𝐦𝐢 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐬𝐢𝐤𝐚𝐧 𝐌𝐀𝐈𝐍𝐓𝐄𝐍𝐀𝐍𝐂𝐄 𝐌𝐈𝐍𝐆𝐆𝐔𝐀𝐍 𝐬𝐮𝐝𝐚𝐡 𝐒𝐞𝐥𝐞𝐬𝐚𝐢. 𝐓𝐞𝐫𝐢𝐦𝐚𝐤𝐚𝐬𝐢𝐡 𝐭𝐞𝐥𝐚𝐡 𝐦𝐞𝐧𝐮𝐧𝐠𝐠𝐮🙏🏼",
        "image_url": "https://i.imgur.com/PNRleK4.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝐏𝐔𝐒𝐀𝐓𝐍𝐘𝐀 𝐆𝐀𝐌𝐄 𝐆𝐀𝐂𝐎𝐑 𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆 𝐃𝐀𝐍 𝐓𝐄𝐑𝐏𝐄𝐑𝐂𝐀𝐘𝐀!",
            "image_url": "https://i.postimg.cc/dtn4RbFw/FDY.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "𝐏𝐀𝐋𝐈𝐍𝐆 𝐅𝐀𝐈𝐑 𝐃𝐄𝐍𝐆𝐀𝐍 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐍𝐘𝐀𝐓𝐀✨",
            "image_url": "https://i.postimg.cc/vZBX0089/URU56.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝐑𝐀𝐒𝐀𝐊𝐀𝐍 𝐒𝐄𝐍𝐒𝐀𝐒𝐈 𝐌𝐀𝐗𝐖𝐈𝐍 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐀𝐔𝐓𝐎 𝐉𝐀𝐃𝐈 𝐒𝐔𝐋𝐓𝐀𝐍🔥",
            "image_url": "https://i.postimg.cc/6Q9YTt5f/BWETBS.png",
	    "time": "23:50",
            "buttons": [
           {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },

 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐈𝐏𝐀𝐓 𝐓𝐀𝐍𝐏𝐀 𝐑𝐔𝐍𝐆𝐊𝐀𝐃. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐒𝐄𝐌𝐔𝐀 𝐏𝐄𝐑𝐌𝐀𝐈𝐍𝐀𝐍 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖. 𝐇𝐀𝐍𝐘𝐀  𝟐𝟎𝐑𝐁 𝐁𝐈𝐒𝐀 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐋𝐎𝐇!!",
        "image_url": "https://i.postimg.cc/wxt5mCGC/KHJJK.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐏𝐔𝐒𝐀𝐓𝐍𝐘𝐀 𝐆𝐀𝐌𝐄 𝐆𝐀𝐂𝐎𝐑 𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆 𝐃𝐀𝐍 𝐓𝐄𝐑𝐏𝐄𝐑𝐂𝐀𝐘𝐀!",
            "image_url": "https://i.postimg.cc/kgyWCq2b/BEERWRB.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/L4YKmBW6/herths.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
{
        "channel_id": -1002336758098,
            "text": "𝐌𝐀𝐈𝐍 𝐆𝐀𝐌𝐄 𝐃𝐄𝐍𝐆𝐀𝐍 𝐓𝐈𝐍𝐆𝐊𝐀𝐓 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐓𝐄𝐑𝐓𝐈𝐍𝐆𝐆𝐈 𝐇𝐀𝐍𝐘𝐀 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖 𝐁𝐔𝐊𝐓𝐈𝐊𝐀𝐍 𝐃𝐀𝐍 𝐑𝐀𝐒𝐀𝐊𝐀𝐍 𝐒𝐄𝐍𝐃𝐈𝐑𝐈🔥🔥",
            "image_url": "https://i.postimg.cc/66ksq4sV/GJHF7.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 HOKI-1002262328897 =====

    {
        "channel_id": -1002262328897,
       "text": "𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐈𝐏𝐀𝐓 𝐓𝐀𝐍𝐏𝐀 𝐑𝐔𝐍𝐆𝐊𝐀𝐃. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐒𝐄𝐌𝐔𝐀 𝐏𝐄𝐑𝐌𝐀𝐈𝐍𝐀𝐍 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖. 𝐇𝐀𝐍𝐘𝐀  𝟐𝟎𝐑𝐁 𝐁𝐈𝐒𝐀 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐋𝐎𝐇!!",
        "image_url": "https://i.postimg.cc/wxt5mCGC/KHJJK.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "𝐏𝐔𝐒𝐀𝐓𝐍𝐘𝐀 𝐆𝐀𝐌𝐄 𝐆𝐀𝐂𝐎𝐑 𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆 𝐃𝐀𝐍 𝐓𝐄𝐑𝐏𝐄𝐑𝐂𝐀𝐘𝐀!",
            "image_url": "https://i.postimg.cc/kgyWCq2b/BEERWRB.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/L4YKmBW6/herths.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐁𝐀𝐍𝐘𝐀𝐊 𝐁𝐎𝐍𝐔𝐒𝐍𝐘𝐀, 𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐑𝐄𝐂𝐄𝐇 𝐁𝐈𝐒𝐀 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖 𝐉𝐔𝐓𝐀𝐀𝐍. 𝐏𝐀𝐒𝐓𝐈𝐍𝐘𝐀 𝐌𝐀𝐗𝐖𝐈𝐍 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈! ",
            "image_url": "https://i.postimg.cc/66ksq4sV/GJHF7.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        }
],
"tuesday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "𝐉𝐀𝐍𝐆𝐀𝐍 𝐑𝐀𝐆𝐔 𝐉𝐀𝐍𝐆𝐀𝐍 𝐁𝐈𝐌𝐁𝐀𝐍𝐆,𝐏𝐀𝐒𝐓𝐈 𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍 🔥",
        "image_url": "https://i.postimg.cc/gchCkLsZ/UMYU.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐃𝐀𝐏𝐀𝐓𝐊𝐀𝐍 𝐅𝐈𝐓𝐔𝐑 𝐓𝐄𝐑𝐁𝐀𝐑𝐔, 𝐌𝐔𝐃𝐀𝐇 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐃𝐈𝐒𝐄𝐌𝐔𝐀 𝐏𝐄𝐑𝐌𝐀𝐈𝐍𝐀𝐍",
        "image_url": "https://i.postimg.cc/8PVqFkXn/rneter.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 𝐒𝐥𝐨𝐭 𝐆𝐚𝐜𝐨𝐫 𝐒𝐞𝐭𝐢𝐚𝐩 𝐇𝐚𝐫𝐢. 𝐌𝐚𝐢𝐧𝐤𝐚𝐧 𝐒𝐥𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐑𝐓𝐏 𝐓𝐞𝐫𝐭𝐢𝐧𝐠𝐠𝐢 𝐇𝐚𝐧𝐲𝐚 𝐝𝐢 𝐀𝐏𝐈𝟐𝟖𝟖. 𝐒𝐥𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 𝐆𝐚𝐦𝐩𝐚𝐧𝐠 𝐌𝐚𝐱𝐰𝐢𝐧🥇",
        "image_url": "https://i.postimg.cc/MpsxJk2v/reghe.png",
        "time": "18:45",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐂𝐔𝐌𝐀 𝟏𝟎𝐑𝐈𝐁𝐔, 𝐆𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐀𝐗𝐖𝐈𝐍. 𝐆𝐀𝐂𝐎𝐑 𝐀𝐒𝐋𝐈 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐒𝐀 𝐁𝐀𝐒𝐈",
        "image_url": "https://i.postimg.cc/d1CKCL7y/HEE.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
    {
        "channel_id": -1002432716701,
        "text": "𝐉𝐀𝐍𝐆𝐀𝐍 𝐑𝐀𝐆𝐔 𝐉𝐀𝐍𝐆𝐀𝐍 𝐁𝐈𝐌𝐁𝐀𝐍𝐆,𝐏𝐀𝐒𝐓𝐈 𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍 🔥",
        "image_url": "https://i.postimg.cc/gchCkLsZ/UMYU.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 𝐒𝐥𝐨𝐭 𝐆𝐚𝐜𝐨𝐫 𝐒𝐞𝐭𝐢𝐚𝐩 𝐇𝐚𝐫𝐢. 𝐌𝐚𝐢𝐧𝐤𝐚𝐧 𝐒𝐥𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐑𝐓𝐏 𝐓𝐞𝐫𝐭𝐢𝐧𝐠𝐠𝐢 𝐇𝐚𝐧𝐲𝐚 𝐝𝐢 𝐀𝐏𝐈𝟐𝟖𝟖. 𝐒𝐥𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 𝐆𝐚𝐦𝐩𝐚𝐧𝐠 𝐌𝐚𝐱𝐰𝐢𝐧🥇",
        "image_url": "https://i.postimg.cc/8PVqFkXn/rneter.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐃𝐀𝐏𝐀𝐓𝐊𝐀𝐍 𝐅𝐈𝐓𝐔𝐑 𝐓𝐄𝐑𝐁𝐀𝐑𝐔, 𝐌𝐔𝐃𝐀𝐇 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐃𝐈𝐒𝐄𝐌𝐔𝐀 𝐏𝐄𝐑𝐌𝐀𝐈𝐍𝐀𝐍",
        "image_url": "https://i.postimg.cc/d1CKCL7y/HEE.png",
        "time": "18:45",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

{
        "channel_id": -1002432716701,
        "text": "𝐂𝐔𝐌𝐀 𝟏𝟎𝐑𝐈𝐁𝐔, 𝐆𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐀𝐗𝐖𝐈𝐍. 𝐆𝐀𝐂𝐎𝐑 𝐀𝐒𝐋𝐈 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐒𝐀 𝐁𝐀𝐒𝐈",
        "image_url": "https://i.imgur.com/KHMUMTL.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 𝐒𝐥𝐨𝐭 𝐆𝐚𝐜𝐨𝐫 𝐒𝐞𝐭𝐢𝐚𝐩 𝐇𝐚𝐫𝐢. 𝐌𝐚𝐢𝐧𝐤𝐚𝐧 𝐒𝐥𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐑𝐓𝐏 𝐓𝐞𝐫𝐭𝐢𝐧𝐠𝐠𝐢 𝐇𝐚𝐧𝐲𝐚 𝐝𝐢 𝐀𝐏𝐈𝟖𝟖. 𝐒𝐥𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 𝐆𝐚𝐦𝐩𝐚𝐧𝐠 𝐌𝐚𝐱𝐰𝐢𝐧🥇",
        "image_url": "https://i.imgur.com/EFAmcrI.jpeg",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐋𝐀𝐍𝐆𝐆𝐀𝐍𝐀𝐍 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑. 𝐑𝐀𝐉𝐈𝐍 𝐍𝐘𝐄𝐏𝐈𝐍 𝐃𝐈𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:45",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
  {
        "channel_id": -4820852926,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "00:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    # ===== Channel 3 APINAGA -1002849546546 =====
    {
        "channel_id": -1002373443980,
        "text": "𝐓𝐄𝐑𝐒𝐀𝐌𝐁𝐀𝐑 𝐏𝐄𝐓𝐈𝐑 𝐀𝐔𝐓𝐎 𝐓𝐀𝐉𝐈𝐑, 𝐉𝐄𝐌𝐏𝐔𝐓 𝐏𝐄𝐓𝐈𝐑𝐌𝐔 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
        "image_url": "https://i.postimg.cc/Xq2d0Yr7/1551.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐌𝐎𝐃𝐀𝐋 𝟏𝟎𝐑𝐁 𝐁𝐈𝐒𝐀 𝐉𝐀𝐃𝐈 𝐉𝐔𝐓𝐀𝐖𝐀𝐍, 𝐑𝐄𝐊𝐎𝐌𝐄𝐍𝐃𝐀𝐒𝐈 𝐏𝐀𝐋𝐈𝐍𝐆 𝐆𝐀𝐂𝐎𝐑 𝟐𝟎𝟐𝟓! 𝐂𝐎𝐁𝐀𝐈𝐍 𝐘𝐔𝐊 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀",
            "image_url": "https://i.postimg.cc/sfKpWwTd/IO.png",
	        "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/sg0F0p7W/54554.png",
	    "time": "18:45",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
         {
        "channel_id": -1002373443980,
            "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝐍𝐀𝐆𝐀, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
            "image_url": "https://i.postimg.cc/Dzt97nCy/N5445.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
              # ===== Channel 3 BOSKU33 -1002568434905 =====
    {
        "channel_id": -1002568434905,
        "text": "𝐌𝐨𝐝𝐚𝐥 𝐭𝐢𝐩𝐢𝐬, 𝐡𝐚𝐬𝐢𝐥 𝐟𝐚𝐧𝐭𝐚𝐬𝐭𝐢𝐬!💸",
        "image_url": "https://i.postimg.cc/sXmZpg99/48482.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐚𝐚𝐭 𝐲𝐚𝐧𝐠 𝐭𝐞𝐩𝐚𝐭 𝐮𝐧𝐭𝐮𝐤 𝐦𝐞𝐧𝐚𝐧𝐠! 𝐒𝐩𝐢𝐧 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐌𝐚𝐱𝐰𝐢𝐧 𝐭𝐢𝐧𝐠𝐠𝐚𝐥 𝐧𝐮𝐧𝐠𝐠𝐮!",
            "image_url": "https://i.postimg.cc/0jHMBX4z/8488.png",
	    "time": "14:50",
            "buttons": [
              {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "𝐏𝐄𝐍𝐃𝐀𝐓𝐀𝐍𝐆 𝐁𝐀𝐑𝐔 𝐃𝐈𝐊𝐀𝐒𝐈𝐇 𝐉𝐀𝐂𝐊𝐏𝐎𝐓. 𝐂𝐔𝐌𝐀 𝐃𝐈𝐒𝐈𝐍𝐈 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐘𝐆 𝐍𝐘𝐀𝐓𝐀!✨",
            "image_url": "https://i.postimg.cc/43h0LjJC/UYIYJH.png",
	    "time": "18:45",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝐋𝐚𝐠𝐢 𝐛𝐚𝐰𝐚 𝐡𝐨𝐤𝐢? 𝐂𝐨𝐛𝐚 𝐚𝐣𝐚 𝐬𝐩𝐢𝐧 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐬𝐢𝐚𝐩𝐚 𝐭𝐚𝐡𝐮 𝐉𝐏 𝐛𝐞𝐬𝐚𝐫!",
            "image_url": "https://i.postimg.cc/KzSHdQz1/BWERVA.png",
	    "time": "23:50",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },

 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!",
        "image_url": "https://i.postimg.cc/WbFh4nK7/futfru.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
            "image_url": "https://i.postimg.cc/brqFvJ18/JKGH.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/wTfb69M8/hehe.png",
	    "time": "18:45",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
 {
        "channel_id": -1002336758098,
            "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 𝐡𝐚𝐧𝐲𝐚 𝐝𝐢 𝐇𝐎𝐊𝐈𝟏𝟕𝟖! 🚀",
            "image_url": "https://i.postimg.cc/NM6zYT9p/JHGJK.png",
	    "time": "23:50",
            "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 HOKI -1002262328897 =====
    {
        "channel_id": -1002262328897,
       "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟐𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
        "image_url": "https://i.postimg.cc/WbFh4nK7/futfru.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
            "image_url": "https://i.postimg.cc/brqFvJ18/JKGH.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/wTfb69M8/hehe.png",
	    "time": "18:45",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002262328897,
            "text": "𝐖𝐀𝐉𝐈𝐁 𝐂𝐔𝐀𝐍 𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈 𝗛𝗢𝗞𝗜𝟭𝟳𝟴. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐂𝐔𝐀𝐍 𝐓𝐈𝐀𝐃𝐀 𝐇𝐄𝐍𝐓𝐈𝐍𝐘𝐀",
            "image_url": "https://i.postimg.cc/NM6zYT9p/JHGJK.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    }
],

"wednesday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆 - 𝐌𝐔𝐃𝐀𝐇 𝐌𝐀𝐗𝐖𝐈𝐍. 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖💰",
        "image_url": "https://i.postimg.cc/ZqhkWPfy/GWQGQ.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.postimg.cc/ZRVXsGJr/fasfas.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐇𝐀𝐍𝐘𝐀 𝐃𝐄𝐍𝐆𝐀𝐍 𝟏𝟎𝐑𝐈𝐁𝐔 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐇𝐀𝐍𝐘𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.postimg.cc/cL0wz8Zs/tyu.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐋𝐀𝐍𝐆𝐆𝐀𝐍𝐀𝐍 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑. 𝐑𝐀𝐉𝐈𝐍 𝐍𝐘𝐄𝐏𝐈𝐍 𝐃𝐈𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍, 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈  𝐀𝐏𝐈𝟐𝟖𝟖 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!",
        "image_url": "https://i.postimg.cc/xddHfDch/JHFJU.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
    {
        "channel_id": -1002432716701,
        "text": "𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆 - 𝐌𝐔𝐃𝐀𝐇 𝐌𝐀𝐗𝐖𝐈𝐍. 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖",
        "image_url": "https://i.postimg.cc/ZqhkWPfy/GWQGQ.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐇𝐀𝐍𝐘𝐀 𝐃𝐄𝐍𝐆𝐀𝐍 𝟏𝟎𝐑𝐈𝐁𝐔 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐇𝐀𝐍𝐘𝐀 𝐃𝐈𝐒𝐈𝐍𝐈💰",
        "image_url": "https://i.postimg.cc/ZRVXsGJr/fasfas.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟏𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
        "image_url": "https://i.postimg.cc/cL0wz8Zs/tyu.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

 {
        "channel_id": -1002432716701,
        "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.postimg.cc/xddHfDch/JHFJU.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟏𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
        "image_url": "https://i.imgur.com/YBEQ04i.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
       "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
 {
        "channel_id": -4820852926,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    # ===== Channel 3 APINAGA -1002373443980 =====
    {
        "channel_id": -1002373443980,
        "text": "🎰 𝐂𝐚𝐫𝐢 𝐩𝐥𝐚𝐭𝐟𝐨𝐫𝐦 𝐬𝐥𝐨𝐭 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐡𝐚𝐬𝐢𝐥 𝐦𝐚𝐤𝐬𝐢𝐦𝐚𝐥?𝐋𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐚𝐣𝐚 𝐃𝐈 𝐀𝐏𝐈𝐍𝐀𝐆𝐀 𝐒𝐈𝐓𝐔𝐒 𝐒𝐋𝐎𝐓 𝐏𝐀𝐋𝐈𝐍𝐆 𝐁𝐀𝐍𝐘𝐀𝐊 𝐃𝐈𝐂𝐀𝐑𝐈 𝐃𝐈 𝐀𝐒𝐈𝐀, 𝐭𝐞𝐦𝐩𝐚𝐭𝐧𝐲𝐚 𝐩𝐚𝐫𝐚 𝐩𝐞𝐧𝐜𝐚𝐫𝐢 𝐜𝐮𝐚𝐧 𝐬𝐞𝐣𝐚𝐭𝐢!",
        "image_url": "https://i.postimg.cc/GmmKq4HS/awgwga.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈.",
            "image_url": "https://i.postimg.cc/bNKW5HfF/fsaf.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "𝐋𝐀𝐍𝐆𝐆𝐀𝐍𝐀𝐍 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑. 𝐑𝐀𝐉𝐈𝐍 𝐍𝐘𝐄𝐏𝐈𝐍 𝐃𝐈𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍, 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈  𝐀𝐏𝐈𝐍𝐀𝐆𝐀 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!",
            "image_url": "https://i.postimg.cc/rmBtNDQ2/HJGMKG.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
{
        "channel_id": -1002373443980,
            "text": "𝐊𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧 𝐦𝐢𝐥𝐢𝐤 𝐲𝐚𝐧𝐠 𝐛𝐞𝐫𝐚𝐧𝐢! 𝐂𝐨𝐛𝐚 𝐬𝐩𝐢𝐧 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢, 𝐬𝐢𝐚𝐩𝐚 𝐭𝐚𝐡𝐮 𝐠𝐢𝐥𝐢𝐫𝐚𝐧𝐦𝐮!",
            "image_url": "https://i.postimg.cc/Wz0qWsHF/NDFY.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
                           # ===== Channel 3 BOSKU33 -1002568434905 =====
    {
        "channel_id": -1002568434905,
        "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈.💸",
        "image_url": "https://i.postimg.cc/X7HdNQYQ/j547546.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐢𝐚𝐩𝐤𝐚𝐧 𝐝𝐢𝐫𝐢𝐦𝐮 𝐬𝐚𝐦𝐛𝐮𝐭 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨 𝐫𝐢𝐧𝐠𝐚𝐧!",
            "image_url": "https://i.postimg.cc/ZYs18z7m/00025.png",
	    "time": "14:50",
            "buttons": [
              {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆 - 𝐌𝐔𝐃𝐀𝐇 𝐌𝐀𝐗𝐖𝐈𝐍. 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈 𝐁𝐎𝐒𝐊𝐔𝟑𝟑",
            "image_url": "https://i.postimg.cc/Y0RQ3pVr/NDFNR.png",
	    "time": "18:40",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
            "image_url": "https://i.postimg.cc/pXGRwwMp/MFGHM.png",
	    "time": "23:50",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "𝐘𝐀𝐍𝐆 𝐆𝐀𝐂𝐎𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐋𝐔𝐍𝐀𝐒",
        "image_url": "https://i.postimg.cc/WpSJSXgT/WBE543W.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈.",
            "image_url": "https://i.postimg.cc/bNJS5k9b/BQBQ.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/HL0KgM8B/VWAWD.png",
	    "time": "18:40",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
        {
        "channel_id": -1002336758098,
            "text": "𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐈𝐏𝐀𝐓 𝐓𝐀𝐍𝐏𝐀 𝐑𝐔𝐍𝐆𝐊𝐀𝐃. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐒𝐄𝐌𝐔𝐀 𝐏𝐄𝐑𝐌𝐀𝐈𝐍𝐀𝐍 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖. 𝐇𝐀𝐍𝐘𝐀  𝟐𝟎𝐑𝐁 𝐁𝐈𝐒𝐀 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐋𝐎𝐇!",
            "image_url": "https://i.postimg.cc/j5s1djzK/GDSGS.png",
	    "time": "23:50",
            "buttons": [
           {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 -1002262328897 =====
    {
        "channel_id": -1002262328897,
       "text": "𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐈𝐏𝐀𝐓 𝐓𝐀𝐍𝐏𝐀 𝐑𝐔𝐍𝐆𝐊𝐀𝐃. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐒𝐄𝐌𝐔𝐀 𝐏𝐄𝐑𝐌𝐀𝐈𝐍𝐀𝐍 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖. 𝐇𝐀𝐍𝐘𝐀  𝟐𝟎𝐑𝐁 𝐁𝐈𝐒𝐀 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐋𝐎𝐇!",
        "image_url": "https://i.postimg.cc/WpSJSXgT/WBE543W.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "𝐊𝐞𝐦𝐞𝐧𝐚𝐧𝐠𝐚𝐧 𝐛𝐞𝐬𝐚𝐫 𝐛𝐮𝐤𝐚𝐧 𝐜𝐮𝐦𝐚 𝐛𝐮𝐚𝐭 𝐩𝐞𝐦𝐚𝐢𝐧 𝐥𝐚𝐦𝐚, 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐩𝐞𝐦𝐮𝐥𝐚 𝐩𝐮𝐧 𝐛𝐢𝐬𝐚 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐖𝐃 𝐝𝐚𝐥𝐚𝐦 𝐡𝐢𝐭𝐮𝐧𝐠𝐚𝐧 𝐦𝐞𝐧𝐢𝐭! 𝐑𝐚𝐡𝐚𝐬𝐢𝐚𝐧𝐲𝐚? 𝐌𝐚𝐢𝐧 𝐝𝐢 𝐬𝐢𝐭𝐮𝐬 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐲𝐚𝐧𝐠 𝐮𝐝𝐚𝐡 𝐭𝐞𝐫𝐛𝐮𝐤𝐭𝐢 𝐠𝐚𝐜𝐨𝐫. 🎊",
            "image_url": "https://i.postimg.cc/bNJS5k9b/BQBQ.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈.",
            "image_url": "https://i.postimg.cc/HL0KgM8B/VWAWD.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002262328897,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/j5s1djzK/GDSGS.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    }
],
"thursday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "❗𝐁𝐎𝐍𝐔𝐒 𝐌𝐄𝐋𝐈𝐌𝐏𝐀𝐇❗𝐃𝐚𝐟𝐭𝐚𝐫 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐛𝐨𝐧𝐮𝐬 𝐚𝐰𝐚𝐥!",
        "image_url": "https://i.postimg.cc/T2Q1k5nm/BWERBWE.png",
        "time": "10:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "⚡️𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐊𝐈𝐋𝐀𝐓 𝐕𝐈𝐀 𝐐𝐑𝐈𝐒! 𝐂𝐮𝐤𝐮𝐩 𝐬𝐜𝐚𝐧 → 𝐬𝐚𝐥𝐝𝐨 𝐦𝐚𝐬𝐮𝐤 → 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐦𝐚𝐢𝐧! 𝐂𝐞𝐩𝐚𝐭, 𝐚𝐦𝐚𝐧, 𝐭𝐚𝐧𝐩𝐚 𝐫𝐢𝐛𝐞𝐭!",
        "image_url": "https://i.postimg.cc/wTvvnxkr/nytryrt.png",
        "time": "15:08",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐌𝐚𝐱𝐰𝐢𝐧 𝐦𝐚𝐤𝐢𝐧 𝐠𝐚𝐦𝐩𝐚𝐧𝐠, 𝐦𝐨𝐝𝐚𝐥 𝐦𝐚𝐤𝐢𝐧 𝐫𝐢𝐧𝐠𝐚𝐧!⚡️",
        "image_url": "https://i.postimg.cc/XvLrVvY5/1555.png",
        "time": "18:45",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 {
        "channel_id": -1002312224443,
        "text": "𝐊𝐄𝐒𝐄𝐑𝐈𝐍𝐆𝐀𝐍 𝐌𝐀𝐈𝐍 𝐃𝐈 𝗔𝗣𝗜𝟮𝟴𝟴, 𝐃𝐀𝐏𝐀𝐓𝐈𝐍 𝐂𝐔𝐀𝐍 𝐌𝐀𝐊𝐒𝐈𝐌𝐀𝐋 𝐃𝐄𝐍𝐆𝐀𝐍 𝐌𝐎𝐃𝐀𝐋 𝟭𝟎𝐑𝐈𝐁𝐔🔥🔥",
        "image_url": "https://i.postimg.cc/wTvBvDp4/DJHDF.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
    {
        "channel_id": -1002432716701,
        "text": "❗𝐁𝐎𝐍𝐔𝐒 𝐌𝐄𝐋𝐈𝐌𝐏𝐀𝐇❗𝐃𝐚𝐟𝐭𝐚𝐫 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐛𝐨𝐧𝐮𝐬 𝐚𝐰𝐚𝐥!",
        "image_url": "https://i.postimg.cc/T2Q1k5nm/BWERBWE.png",
        "time": "10:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "⚡️𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐊𝐈𝐋𝐀𝐓 𝐕𝐈𝐀 𝐐𝐑𝐈𝐒! 𝐂𝐮𝐤𝐮𝐩 𝐬𝐜𝐚𝐧 → 𝐬𝐚𝐥𝐝𝐨 𝐦𝐚𝐬𝐮𝐤 → 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐦𝐚𝐢𝐧! 𝐂𝐞𝐩𝐚𝐭, 𝐚𝐦𝐚𝐧, 𝐭𝐚𝐧𝐩𝐚 𝐫𝐢𝐛𝐞𝐭!",
        "image_url": "https://i.postimg.cc/wTvvnxkr/nytryrt.png",
        "time": "15:08",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐌𝐚𝐱𝐰𝐢𝐧 𝐦𝐚𝐤𝐢𝐧 𝐠𝐚𝐦𝐩𝐚𝐧𝐠, 𝐦𝐨𝐝𝐚𝐥 𝐦𝐚𝐤𝐢𝐧 𝐫𝐢𝐧𝐠𝐚𝐧!⚡️",
        "image_url": "https://i.postimg.cc/XvLrVvY5/1555.png",
        "time": "18:45",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 {
        "channel_id": -1002432716701,
        "text": "𝐊𝐄𝐒𝐄𝐑𝐈𝐍𝐆𝐀𝐍 𝐌𝐀𝐈𝐍 𝐃𝐈 𝗔𝗣𝗜𝟮𝟴𝟴, 𝐃𝐀𝐏𝐀𝐓𝐈𝐍 𝐂𝐔𝐀𝐍 𝐌𝐀𝐊𝐒𝐈𝐌𝐀𝐋 𝐃𝐄𝐍𝐆𝐀𝐍 𝐌𝐎𝐃𝐀𝐋 𝟭𝟎𝐑𝐈𝐁𝐔🔥🔥",
        "image_url": "https://i.postimg.cc/wTvBvDp4/DJHDF.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "𝐊𝐄𝐒𝐄𝐑𝐈𝐍𝐆𝐀𝐍 𝐌𝐀𝐈𝐍 𝐃𝐈 𝐀𝐏𝐈𝟖𝟖, 𝐃𝐀𝐏𝐀𝐓𝐈𝐍 𝐂𝐔𝐀𝐍 𝐌𝐀𝐊𝐒𝐈𝐌𝐀𝐋 𝐃𝐄𝐍𝐆𝐀𝐍 𝐌𝐎𝐃𝐀𝐋 𝟭𝟎𝐑𝐈𝐁𝐔🔥🔥",
        "image_url": "https://i.imgur.com/EFAmcrI.jpeg",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 𝐡𝐚𝐧𝐲𝐚 𝐝𝐢 𝐀𝐏𝐈𝟖𝟖! 🚀",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "15:08",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
 {
        "channel_id": -4820852926,
        "text": "𝐋𝐀𝐍𝐆𝐆𝐀𝐍𝐀𝐍 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑. 𝐑𝐀𝐉𝐈𝐍 𝐍𝐘𝐄𝐏𝐈𝐍 𝐃𝐈𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍, 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈  𝐀𝐏𝐈𝟖𝟖 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    # ===== Channel 3 APINAGA -1002373443980 =====
    {
        "channel_id": -1002373443980,
        "text": "⚡𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐊𝐈𝐋𝐀𝐓 𝐕𝐈𝐀 𝐐𝐑𝐈𝐒! 𝐂𝐮𝐤𝐮𝐩 𝐬𝐜𝐚𝐧 → 𝐬𝐚𝐥𝐝𝐨 𝐦𝐚𝐬𝐮𝐤 → 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐦𝐚𝐢𝐧! 𝐂𝐞𝐩𝐚𝐭, 𝐚𝐦𝐚𝐧, 𝐭𝐚𝐧𝐩𝐚 𝐫𝐢𝐛𝐞𝐭!",
        "image_url": "https://i.postimg.cc/26rjGC62/GGRTR.png",
        "time": "10:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟭𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
            "image_url": "https://i.postimg.cc/3wgJ2kKk/K879.png",
	    "time": "15:08",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "❗️𝐁𝐎𝐍𝐔𝐒 𝐌𝐄𝐋𝐈𝐌𝐏𝐀𝐇❗️ 𝐃𝐚𝐟𝐭𝐚𝐫 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐛𝐨𝐧𝐮𝐬 𝐚𝐰𝐚𝐥!",
            "image_url": "https://i.postimg.cc/x1yCRdHZ/b46343.png",
	    "time": "18:45",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
{
        "channel_id": -1002373443980,
            "text": "𝐌𝐀𝐊𝐈𝐍 𝐔𝐍𝐓𝐔𝐍𝐆 𝐀𝐍𝐓𝐈 𝐁𝐔𝐍𝐓𝐔𝐍𝐆. 𝐍𝐈𝐊𝐌𝐀𝐓𝐈 𝐒𝐄𝐑𝐔𝐍𝐘𝐀 𝐁𝐄𝐑𝐌𝐀𝐈𝐍 𝐃𝐈 𝐀𝐏𝐈𝐍𝐀𝐆𝐀",
            "image_url": "https://i.postimg.cc/LX2xB945/BQWBQW.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
                         # ===== Channel 3 BOSKU33 -1002568434905 =====
    {
        "channel_id": -1002568434905,
        "text": "⚡𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐊𝐈𝐋𝐀𝐓 𝐕𝐈𝐀 𝐐𝐑𝐈𝐒! 𝐂𝐮𝐤𝐮𝐩 𝐬𝐜𝐚𝐧 → 𝐬𝐚𝐥𝐝𝐨 𝐦𝐚𝐬𝐮𝐤 → 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐦𝐚𝐢𝐧! 𝐂𝐞𝐩𝐚𝐭, 𝐚𝐦𝐚𝐧, 𝐭𝐚𝐧𝐩𝐚 𝐫𝐢𝐛𝐞𝐭!",
        "image_url": "https://i.postimg.cc/ZRR24QDJ/BEWREW.png",
        "time": "10:02",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝗦𝗽𝗶𝗻 𝘀𝗮𝗻𝘁𝗮𝗶, 𝗰𝘂𝗮𝗻 𝗱𝗮𝘁𝗮𝗻𝗴 𝗽𝗲𝗿𝗹𝗮𝗵𝗮𝗻 𝘁𝗮𝗽𝗶 𝗽𝗮𝘀𝘁𝗶.",
            "image_url": "https://i.postimg.cc/j2n1J7b9/jfuu.png",
	    "time": "15:08",
            "buttons": [
              {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "❗️𝐁𝐎𝐍𝐔𝐒 𝐌𝐄𝐋𝐈𝐌𝐏𝐀𝐇❗️ 𝐃𝐚𝐟𝐭𝐚𝐫 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐛𝐨𝐧𝐮𝐬 𝐚𝐰𝐚𝐥!",
            "image_url": "https://i.postimg.cc/T2LncrPH/T2345R23.png",
	    "time": "18:45",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝗕𝘂𝗸𝗮𝗻 𝘀𝗼𝗮𝗹 𝘀𝗲𝗯𝗲𝗿𝗮𝗽𝗮 𝘀𝗲𝗿𝗶𝗻𝗴 𝗺𝗮𝗶𝗻, 𝘁𝗮𝗽𝗶 𝘀𝗲𝗯𝗲𝗿𝗮𝗽𝗮 𝗵𝗼𝗸𝗶 𝗸𝗮𝗺𝘂 𝗵𝗮𝗿𝗶 𝗶𝗻𝗶!",
            "image_url": "https://i.postimg.cc/GmvPMW5y/MTRYRT.png",
	    "time": "23:50",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "❗𝐁𝐎𝐍𝐔𝐒 𝐌𝐄𝐋𝐈𝐌𝐏𝐀𝐇❗ 𝐃𝐚𝐟𝐭𝐚𝐫 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐛𝐨𝐧𝐮𝐬 𝐚𝐰𝐚𝐥!",
        "image_url": "https://i.postimg.cc/MHRSJ4vv/KJJ.png",
        "time": "10:02",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "⚡️𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐊𝐈𝐋𝐀𝐓 𝐕𝐈𝐀 𝐐𝐑𝐈𝐒! 𝐂𝐮𝐤𝐮𝐩 𝐬𝐜𝐚𝐧 → 𝐬𝐚𝐥𝐝𝐨 𝐦𝐚𝐬𝐮𝐤 → 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐦𝐚𝐢𝐧! 𝐂𝐞𝐩𝐚𝐭, 𝐚𝐦𝐚𝐧, 𝐭𝐚𝐧𝐩𝐚 𝐫𝐢𝐛𝐞𝐭!",
            "image_url": "https://i.postimg.cc/26gDJmjs/QBWBQ.png",
	    "time": "15:08",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐖𝐀𝐉𝐈𝐁 𝐂𝐔𝐀𝐍 𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖.",
            "image_url": "https://i.postimg.cc/N0s0Pwkj/by54.png",
	    "time": "18:45",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
         {
        "channel_id": -1002336758098,
            "text": "𝐆𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐀𝐗𝐖𝐈𝐍 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈, 𝐇𝐀𝐍𝐘𝐀 𝟐𝟎𝐑𝐈𝐁𝐔 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐌𝐀𝐈𝐍 𝐃𝐈𝐒𝐈𝐍𝐈💸",
            "image_url": "https://i.postimg.cc/76h2ydmX/GREGE.png",
	    "time": "23:50",
            "buttons": [
       {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 HOKI -1002262328897 =====
    {
        "channel_id": -1002262328897,
       "text": "❗𝐁𝐎𝐍𝐔𝐒 𝐌𝐄𝐋𝐈𝐌𝐏𝐀𝐇❗ 𝐃𝐚𝐟𝐭𝐚𝐫 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐝𝐚𝐩𝐚𝐭 𝐛𝐨𝐧𝐮𝐬 𝐚𝐰𝐚𝐥!",
        "image_url": "https://i.postimg.cc/MHRSJ4vv/KJJ.png",
        "time": "10:02",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "⚡️𝐃𝐄𝐏𝐎𝐒𝐈𝐓 𝐊𝐈𝐋𝐀𝐓 𝐕𝐈𝐀 𝐐𝐑𝐈𝐒! 𝐂𝐮𝐤𝐮𝐩 𝐬𝐜𝐚𝐧 → 𝐬𝐚𝐥𝐝𝐨 𝐦𝐚𝐬𝐮𝐤 → 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐦𝐚𝐢𝐧! 𝐂𝐞𝐩𝐚𝐭, 𝐚𝐦𝐚𝐧, 𝐭𝐚𝐧𝐩𝐚 𝐫𝐢𝐛𝐞𝐭!",
            "image_url": "https://i.postimg.cc/26gDJmjs/QBWBQ.png",
	    "time": "15:08",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐆𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐀𝐗𝐖𝐈𝐍 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈, 𝐇𝐀𝐍𝐘𝐀 𝟐𝟎𝐑𝐈𝐁𝐔 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐌𝐀𝐈𝐍 𝐃𝐈𝐒𝐈𝐍𝐈💸",
            "image_url": "https://i.postimg.cc/N0s0Pwkj/by54.png",
	    "time": "18:45",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
     {
        "channel_id": -1002262328897,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/tTcVRkcb/MVMV.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    }
],

"friday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "𝐑𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐦𝐚𝐢𝐧 𝐲𝐚𝐧𝐠 𝐬𝐞𝐫𝐮, 𝐟𝐢𝐭𝐮𝐫 𝐥𝐞𝐧𝐠𝐤𝐚𝐩, 𝐝𝐚𝐧 𝐩𝐞𝐥𝐮𝐚𝐧𝐠 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢!",
        "image_url": "https://i.postimg.cc/v8qmMX3t/NRETER.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "🚀 𝐒𝐈𝐀𝐏𝐊𝐀𝐍 𝐃𝐈𝐑𝐈 𝐔𝐍𝐓𝐔𝐊 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐏𝐄𝐑𝐓𝐀𝐌𝐀𝐌𝐔! 🚀",
        "image_url": "https://i.postimg.cc/R07FBBDW/wqbeqw.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐁𝐄𝐓 𝐑𝐄𝐂𝐄𝐇 𝐁𝐈𝐒𝐀 𝐃𝐀𝐏𝐀𝐓 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒!!! ",
        "image_url": "https://i.imgur.com/sAc4RrP.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
        {
        "channel_id": -1002312224443,
        "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.imgur.com/uJTrJMe.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
    {
        "channel_id": -1002432716701,
        "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.postimg.cc/v8qmMX3t/NRETER.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐁𝐄𝐓 𝐑𝐄𝐂𝐄𝐇 𝐁𝐈𝐒𝐀 𝐃𝐀𝐏𝐀𝐓 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒!!! ",
        "image_url": "https://i.postimg.cc/R07FBBDW/wqbeqw.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
         "text": "🚀 𝐒𝐈𝐀𝐏𝐊𝐀𝐍 𝐃𝐈𝐑𝐈 𝐔𝐍𝐓𝐔𝐊 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐏𝐄𝐑𝐓𝐀𝐌𝐀𝐌𝐔! 🚀",
        "image_url": "https://i.imgur.com/sAc4RrP.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
  {
        "channel_id": -1002432716701,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/uJTrJMe.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "🎰 𝐂𝐚𝐫𝐢 𝐩𝐥𝐚𝐭𝐟𝐨𝐫𝐦 𝐬𝐥𝐨𝐭 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐡𝐚𝐬𝐢𝐥 𝐦𝐚𝐤𝐬𝐢𝐦𝐚𝐥?𝐋𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐚𝐣𝐚 𝐃𝐈 𝐀𝐏𝐈𝟖𝟖 𝐒𝐈𝐓𝐔𝐒 𝐒𝐋𝐎𝐓 𝐏𝐀𝐋𝐈𝐍𝐆 𝐁𝐀𝐍𝐘𝐀𝐊 𝐃𝐈𝐂𝐀𝐑𝐈 𝐃𝐈 𝐀𝐒𝐈𝐀, 𝐭𝐞𝐦𝐩𝐚𝐭𝐧𝐲𝐚 𝐩𝐚𝐫𝐚 𝐩𝐞𝐧𝐜𝐚𝐫𝐢 𝐜𝐮𝐚𝐧 𝐬𝐞𝐣𝐚𝐭𝐢!",
        "image_url": "https://i.imgur.com/EFAmcrI.jpeg",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
 {
        "channel_id": -4820852926,
        "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    # ===== Channel 3 APINAGA -1002373443980 =====
    {
        "channel_id": -1002373443980,
        "text": "𝐌𝐎𝐃𝐀𝐋 𝟏𝟎𝐑𝐁 𝐁𝐈𝐒𝐀 𝐉𝐀𝐃𝐈 𝐉𝐔𝐓𝐀𝐖𝐀𝐍, 𝐑𝐄𝐊𝐎𝐌𝐄𝐍𝐃𝐀𝐒𝐈 𝐏𝐀𝐋𝐈𝐍𝐆 𝐆𝐀𝐂𝐎𝐑 𝟐𝟎𝟐𝟓! 𝐂𝐎𝐁𝐀𝐈𝐍 𝐘𝐔𝐊 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀",
        "image_url": "https://i.postimg.cc/h45KNvtC/YYTR65.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
            "image_url": "https://i.postimg.cc/2S4mqxFJ/BQWEBQW.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "𝐊𝐄𝐒𝐄𝐑𝐈𝐍𝐆𝐀𝐍 𝐌𝐀𝐈𝐍 𝐃𝐈 𝐀𝐏𝐈𝐍𝐀𝐆𝐀, 𝐃𝐀𝐏𝐀𝐓𝐈𝐍 𝐂𝐔𝐀𝐍 𝐌𝐀𝐊𝐒𝐈𝐌𝐀𝐋 𝐃𝐄𝐍𝐆𝐀𝐍 𝐌𝐎𝐃𝐀𝐋 𝟏𝟎𝐑𝐈𝐁𝐔🔥",
            "image_url": "https://i.imgur.com/KQwZgNm.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
          {
        "channel_id": -1002373443980,
            "text": "𝐊𝐞𝐦𝐞𝐧𝐚𝐧𝐠𝐚𝐧 𝐛𝐞𝐬𝐚𝐫 𝐛𝐮𝐤𝐚𝐧 𝐜𝐮𝐦𝐚 𝐛𝐮𝐚𝐭 𝐩𝐞𝐦𝐚𝐢𝐧 𝐥𝐚𝐦𝐚, 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐩𝐞𝐦𝐮𝐥𝐚 𝐩𝐮𝐧 𝐛𝐢𝐬𝐚 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐖𝐃 𝐝𝐚𝐥𝐚𝐦 𝐡𝐢𝐭𝐮𝐧𝐠𝐚𝐧 𝐦𝐞𝐧𝐢𝐭! 𝐑𝐚𝐡𝐚𝐬𝐢𝐚𝐧𝐲𝐚? 𝐌𝐚𝐢𝐧 𝐝𝐢 𝐬𝐢𝐭𝐮𝐬 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐲𝐚𝐧𝐠 𝐮𝐝𝐚𝐡 𝐭𝐞𝐫𝐛𝐮𝐤𝐭𝐢 𝐠𝐚𝐜𝐨𝐫. 🎊",
            "image_url": "https://i.imgur.com/uIZf7et.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
                          # ===== Channel 3 BOSKU33 -1002568434905 =====
    {
        "channel_id": -1002568434905,
        "text": "𝗣𝗥𝗢𝗩𝗜𝗗𝗘𝗥 𝗣𝗔𝗟𝗜𝗡𝗚 𝗟𝗘𝗡𝗚𝗞𝗔𝗣 𝗗𝗔𝗡 𝗧𝗘𝗥𝗣𝗘𝗥𝗖𝗔𝗬𝗔, 𝗖𝗢𝗕𝗔𝗜𝗡 𝗬𝗨𝗞 𝗦𝗘𝗞𝗔𝗥𝗔𝗡𝗚!",
        "image_url": "https://i.postimg.cc/bwHcYwqf/ebqeqw.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐢𝐚𝐩𝐤𝐚𝐧 𝐝𝐢𝐫𝐢𝐦𝐮 𝐬𝐚𝐦𝐛𝐮𝐭 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨 𝐫𝐢𝐧𝐠𝐚𝐧!",
            "image_url": "https://i.postimg.cc/kMzdfHTz/5n648.png",
	    "time": "14:50",
            "buttons": [
              {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐞𝐤𝐚𝐥𝐢 𝐦𝐞𝐧𝐚𝐧𝐠, 𝐬𝐮𝐬𝐚𝐡 𝐛𝐞𝐫𝐡𝐞𝐧𝐭𝐢. 𝐤𝐞𝐭𝐚𝐠𝐢𝐡𝐚𝐧 𝐜𝐮𝐚𝐧!",
            "image_url": "https://i.imgur.com/Tm5vaWB.png",
	    "time": "18:40",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝐌𝐞𝐧𝐝𝐚𝐝𝐚𝐤 𝐣𝐚𝐝𝐢 𝐣𝐮𝐭𝐚𝐰𝐚𝐧, 𝐠𝐚𝐫𝐚𝟐 𝐬𝐚𝐭𝐮 𝐤𝐚𝐥𝐢 𝐬𝐩𝐢𝐧. 𝐁𝐮𝐫𝐮𝐚𝐧 𝐠𝐚𝐬, 𝐬𝐞𝐛𝐞𝐥𝐮𝐦 𝐝𝐢𝐬𝐢𝐤𝐚𝐭 𝐨𝐫𝐚𝐧𝐠 𝐥𝐚𝐢𝐧!",
            "image_url": "https://i.imgur.com/FJwfEhl.png",
	    "time": "23:50",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "𝐊𝐞𝐦𝐞𝐧𝐚𝐧𝐠𝐚𝐧 𝐛𝐞𝐬𝐚𝐫 𝐛𝐮𝐤𝐚𝐧 𝐜𝐮𝐦𝐚 𝐛𝐮𝐚𝐭 𝐩𝐞𝐦𝐚𝐢𝐧 𝐥𝐚𝐦𝐚, 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐩𝐞𝐦𝐮𝐥𝐚 𝐩𝐮𝐧 𝐛𝐢𝐬𝐚 𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐖𝐃 𝐝𝐚𝐥𝐚𝐦 𝐡𝐢𝐭𝐮𝐧𝐠𝐚𝐧 𝐦𝐞𝐧𝐢𝐭! 𝐑𝐚𝐡𝐚𝐬𝐢𝐚𝐧𝐲𝐚? 𝐌𝐚𝐢𝐧 𝐝𝐢 𝐬𝐢𝐭𝐮𝐬 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐲𝐚𝐧𝐠 𝐮𝐝𝐚𝐡 𝐭𝐞𝐫𝐛𝐮𝐤𝐭𝐢 𝐠𝐚𝐜𝐨𝐫. 🎊",
        "image_url": "https://i.postimg.cc/q7jPnDtm/nqwewq.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐒𝐎𝐋𝐔𝐒𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈𝐍𝐘𝐀!",
            "image_url": "https://i.postimg.cc/3Jy9Z8N5/EWTFDS.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 𝐡𝐚𝐧𝐲𝐚 𝐝𝐢 𝐇𝐎𝐊𝐈𝟏𝟕𝟖! 🚀",
            "image_url": "https://i.imgur.com/nuXjIhl.png",
	    "time": "18:40",
            "buttons": [
           {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
   {
        "channel_id": -1002336758098,
            "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈.",
            "image_url": "https://i.imgur.com/CGwGELH.png",
	    "time": "23:50",
            "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 HOKI -1002262328897 =====
    {
        "channel_id": -1002262328897,
        "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 𝐡𝐚𝐧𝐲𝐚 𝐝𝐢 𝐇𝐎𝐊𝐈𝟏𝟕𝟖! 🚀",
        "image_url": "https://i.postimg.cc/q7jPnDtm/nqwewq.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "𝐌𝐀𝐈𝐍𝐊𝐀𝐍 𝐃𝐄𝐍𝐆𝐀𝐍 𝐑𝐓𝐏 𝐓𝐄𝐑𝐈𝐍𝐆𝐆𝐈 𝐃𝐀𝐍 𝐀𝐊𝐔𝐑𝐀𝐓 𝐔𝐍𝐓𝐔𝐊 𝐇𝐀𝐑𝐈 𝐈𝐍𝐈.",
            "image_url": "https://i.postimg.cc/3Jy9Z8N5/EWTFDS.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 𝐡𝐚𝐧𝐲𝐚 𝐝𝐢 𝐇𝐎𝐊𝐈𝟏𝟕𝟖! 🚀",
            "image_url": "https://i.imgur.com/nuXjIhl.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
     {
        "channel_id": -1002262328897,
            "text": "𝐏𝐄𝐒𝐓𝐀 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐊𝐇𝐔𝐒𝐔𝐒 𝐏𝐄𝐍𝐃𝐀𝐓𝐀𝐍𝐆 𝐁𝐀𝐑𝐔. 𝐃𝐈𝐉𝐀𝐌𝐈𝐍 𝐀𝐍𝐓𝐈 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!",
            "image_url": "https://i.imgur.com/CGwGELH.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    }
],

"saturday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
        "image_url": "https://i.postimg.cc/2jbtjt75/JTRYU.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.postimg.cc/3wWKn668/twqtq.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐑𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐦𝐚𝐢𝐧 𝐲𝐚𝐧𝐠 𝐬𝐞𝐫𝐮, 𝐟𝐢𝐭𝐮𝐫 𝐥𝐞𝐧𝐠𝐤𝐚𝐩, 𝐝𝐚𝐧 𝐩𝐞𝐥𝐮𝐚𝐧𝐠 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢!",
        "image_url": "https://i.postimg.cc/rF5YxtbX/NRTEER.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
     {
        "channel_id": -1002312224443,
        "text": "𝐁𝐄𝐓 𝐑𝐄𝐂𝐄𝐇 𝐁𝐈𝐒𝐀 𝐃𝐀𝐏𝐀𝐓 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒!!! ",
        "image_url": "https://i.postimg.cc/K8FpN8SK/wvqvq.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
    {
        "channel_id": -1002432716701,
        "text": "𝐁𝐄𝐓 𝐑𝐄𝐂𝐄𝐇 𝐁𝐈𝐒𝐀 𝐃𝐀𝐏𝐀𝐓 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒!!! ",
        "image_url": "https://i.postimg.cc/2jbtjt75/JTRYU.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐑𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐦𝐚𝐢𝐧 𝐲𝐚𝐧𝐠 𝐬𝐞𝐫𝐮, 𝐟𝐢𝐭𝐮𝐫 𝐥𝐞𝐧𝐠𝐤𝐚𝐩, 𝐝𝐚𝐧 𝐩𝐞𝐥𝐮𝐚𝐧𝐠 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢!",
        "image_url": "https://i.postimg.cc/3wWKn668/twqtq.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.postimg.cc/rF5YxtbX/NRTEER.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
{
        "channel_id": -1002432716701,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.postimg.cc/K8FpN8SK/wvqvq.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },


    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝟖𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.imgur.com/EFAmcrI.jpeg",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐂𝐀𝐑𝐈 𝐒𝐋𝐎𝐓 𝐆𝐀𝐂𝐎𝐑? 𝐃𝐈𝐒𝐈𝐍𝐈 𝐓𝐄𝐌𝐏𝐀𝐓𝐍𝐘𝐀. 𝐌𝐔𝐃𝐀𝐇 𝐏𝐄𝐑𝐊𝐀𝐋𝐈𝐀𝐍,𝐌𝐔𝐃𝐀𝐇 𝐒𝐂𝐀𝐓𝐓𝐄𝐑, 𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆𝐍𝐘𝐀",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
{
        "channel_id": -4820852926,
        "text": "𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 𝐒𝐥𝐨𝐭 𝐆𝐚𝐜𝐨𝐫 𝐒𝐞𝐭𝐢𝐚𝐩 𝐇𝐚𝐫𝐢. 𝐌𝐚𝐢𝐧𝐤𝐚𝐧 𝐒𝐥𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐑𝐓𝐏 𝐓𝐞𝐫𝐭𝐢𝐧𝐠𝐠𝐢 𝐇𝐚𝐧𝐲𝐚 𝐝𝐢 𝐀𝐏𝐈𝟖𝟖. 𝐒𝐥𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 𝐆𝐚𝐦𝐩𝐚𝐧𝐠 𝐌𝐚𝐱𝐰𝐢𝐧🥇",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    # ===== Channel 3 APINAGA -1002373443980 =====
    {
        "channel_id": -1002373443980,
        "text": "𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 𝐒𝐥𝐨𝐭 𝐆𝐚𝐜𝐨𝐫 𝐒𝐞𝐭𝐢𝐚𝐩 𝐇𝐚𝐫𝐢. 𝐌𝐚𝐢𝐧𝐤𝐚𝐧 𝐒𝐥𝐨𝐭 𝐝𝐞𝐧𝐠𝐚𝐧 𝐑𝐓𝐏 𝐓𝐞𝐫𝐭𝐢𝐧𝐠𝐠𝐢 𝐇𝐚𝐧𝐲𝐚 𝐝𝐢 𝐀𝐏𝐈𝐍𝐀𝐆𝐀. 𝐒𝐥𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 𝐆𝐚𝐦𝐩𝐚𝐧𝐠 𝐌𝐚𝐱𝐰𝐢𝐧🥇",
        "image_url": "https://i.postimg.cc/g2Y4ht88/9-9.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐂𝐀𝐑𝐈 𝐒𝐋𝐎𝐓 𝐆𝐀𝐂𝐎𝐑? 𝐃𝐈𝐒𝐈𝐍𝐈 𝐓𝐄𝐌𝐏𝐀𝐓𝐍𝐘𝐀. 𝐌𝐔𝐃𝐀𝐇 𝐏𝐄𝐑𝐊𝐀𝐋𝐈𝐀𝐍,𝐌𝐔𝐃𝐀𝐇 𝐒𝐂𝐀𝐓𝐓𝐄𝐑, 𝐌𝐔𝐃𝐀𝐇 𝐌𝐄𝐍𝐀𝐍𝐆𝐍𝐘𝐀",
            "image_url": "https://i.postimg.cc/xCrWM4VF/J5679.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/NjpDk8kV/BGTT.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
         {
        "channel_id": -1002373443980,
            "text": "𝐒𝐄𝐍𝐒𝐀𝐓𝐈𝐎𝐍𝐀𝐋 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒, 𝐏𝐀𝐒𝐓𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐏𝐀𝐒𝐓𝐈 𝐖𝐈𝐓𝐇𝐃𝐑𝐀𝐖. 𝐂𝐔𝐀𝐍 𝐓𝐄𝐑𝐔𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈 💸",
            "image_url": "https://i.postimg.cc/Zqnc79fq/N4ET.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
                      # ===== Channel 3 BOSKU33 -1002568434905 =====
    {
        "channel_id": -1002568434905,
        "text": "𝐃𝐀𝐅𝐓𝐀𝐑 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 – 𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆 𝐆𝐀𝐂𝐎𝐑🔥",
        "image_url": "https://i.postimg.cc/Y06fGQSd/JHJU.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐢𝐚𝐩𝐤𝐚𝐧 𝐝𝐢𝐫𝐢𝐦𝐮 𝐬𝐚𝐦𝐛𝐮𝐭 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨 𝐫𝐢𝐧𝐠𝐚𝐧!",
            "image_url": "https://i.postimg.cc/1tZjfVDk/B546Y.png",
	    "time": "14:50",
            "buttons": [
              {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
            "image_url": "https://i.postimg.cc/pTnBvwMb/BQWEQW.png",
	    "time": "18:40",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
            "image_url": "https://i.postimg.cc/tgczLXfN/GHUYT.png",
	    "time": "23:50",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "𝐁𝐄𝐑𝐇𝐄𝐍𝐓𝐈 𝐁𝐔𝐊𝐀𝐍 𝐒𝐎𝐋𝐔𝐒𝐈, 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈!! ",
        "image_url": "https://i.postimg.cc/MZ7yYbWD/VWE.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐊𝐄𝐒𝐄𝐑𝐈𝐍𝐆𝐀𝐍 𝐌𝐀𝐈𝐍 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖, 𝐃𝐀𝐏𝐀𝐓𝐈𝐍 𝐂𝐔𝐀𝐍 𝐌𝐀𝐊𝐒𝐈𝐌𝐀𝐋 𝐃𝐄𝐍𝐆𝐀𝐍 𝐌𝐎𝐃𝐀𝐋 𝟏𝟎𝐑𝐈𝐁𝐔🔥🔥",
            "image_url": "https://i.postimg.cc/dQ6xV13f/V34WER.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
            "image_url": "https://i.postimg.cc/YCsgSd3p/VWAB.png",
	    "time": "18:40",
            "buttons": [
           {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
 {
        "channel_id": -1002336758098,
            "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
            "image_url": "https://i.postimg.cc/d0ZCZGHG/hreh.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 HOKI -1002262328897 =====
    {
        "channel_id": -1002262328897,
       "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
        "image_url": "https://i.postimg.cc/MZ7yYbWD/VWE.png",
        "time": "10:32",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
            "image_url": "https://i.postimg.cc/dQ6xV13f/V34WER.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
            "image_url": "https://i.postimg.cc/YCsgSd3p/VWAB.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
      {
        "channel_id": -1002262328897,
            "text": "𝐁𝐄𝐑𝐇𝐄𝐍𝐓𝐈 𝐁𝐔𝐊𝐀𝐍 𝐒𝐎𝐋𝐔𝐒𝐈, 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈!! ",
            "image_url": "https://i.postimg.cc/d0ZCZGHG/hreh.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    }
],

"sunday": [
    # ===== Channel 1 API288 -1002312224443 =====
    {
        "channel_id": -1002312224443,
        "text": "𝐋𝐀𝐍𝐆𝐆𝐀𝐍𝐀𝐍 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑. 𝐑𝐀𝐉𝐈𝐍 𝐍𝐘𝐄𝐏𝐈𝐍 𝐃𝐈𝐊𝐀𝐒𝐈𝐇 𝐌𝐀𝐗𝐖𝐈𝐍, 𝐃𝐈𝐌𝐀𝐍𝐀 𝐋𝐀𝐆𝐈 𝐊𝐀𝐋𝐀𝐔 𝐁𝐔𝐊𝐀𝐍 𝐃𝐈  𝐀𝐏𝐈𝟐𝟖𝟖 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!",
        "image_url": "https://i.postimg.cc/d1xjZN1q/FGSHYER.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐒𝐢𝐭𝐮𝐬 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝟐𝟎𝟐𝟓 𝐦𝐞𝐧𝐠𝐡𝐚𝐝𝐢𝐫𝐤𝐚𝐧 𝐬𝐥𝐨𝐭-𝐬𝐥𝐨𝐭 𝐠𝐚𝐜𝐨𝐫 𝐝𝐚𝐫𝐢 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐫 𝐭𝐞𝐫𝐧𝐚𝐦𝐚 𝐬𝐞𝐩𝐞𝐫𝐭𝐢 𝐏𝐫𝐚𝐠𝐦𝐚𝐭𝐢𝐜 𝐏𝐥𝐚𝐲, 𝐇𝐚𝐛𝐚𝐧𝐞𝐫𝐨, 𝐝𝐚𝐧 𝐏𝐆 𝐒𝐨𝐟𝐭. 𝐃𝐞𝐧𝐠𝐚𝐧 𝐬𝐚𝐭𝐮 𝐚𝐤𝐮𝐧 𝐕𝐈𝐏, 𝐤𝐚𝐦𝐮 𝐛𝐢𝐬𝐚 𝐚𝐤𝐬𝐞𝐬 𝐬𝐞𝐦𝐮𝐚 𝐬𝐥𝐨𝐭 𝐠𝐚𝐜𝐨𝐫 𝐟𝐚𝐯𝐨𝐫𝐢𝐭𝐦𝐮!",
        "image_url": "https://i.postimg.cc/QCKkQg9c/yiuit7.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "🎰 𝐂𝐚𝐫𝐢 𝐩𝐥𝐚𝐭𝐟𝐨𝐫𝐦 𝐬𝐥𝐨𝐭 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐡𝐚𝐬𝐢𝐥 𝐦𝐚𝐤𝐬𝐢𝐦𝐚𝐥?𝐋𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐚𝐣𝐚 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖 𝐒𝐈𝐓𝐔𝐒 𝐒𝐋𝐎𝐓 𝐏𝐀𝐋𝐈𝐍𝐆 𝐁𝐀𝐍𝐘𝐀𝐊 𝐃𝐈𝐂𝐀𝐑𝐈 𝐃𝐈 𝐀𝐒𝐈𝐀, 𝐭𝐞𝐦𝐩𝐚𝐭𝐧𝐲𝐚 𝐩𝐚𝐫𝐚 𝐩𝐞𝐧𝐜𝐚𝐫𝐢 𝐜𝐮𝐚𝐧 𝐬𝐞𝐣𝐚𝐭𝐢!",
        "image_url": "https://i.imgur.com/evg6ThL.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002312224443,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.imgur.com/ygMOQMr.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 # ===== Grup 1 API288 -1002432716701 =====
    {
        "channel_id": -1002432716701,
        "text": "🎰 𝐂𝐚𝐫𝐢 𝐩𝐥𝐚𝐭𝐟𝐨𝐫𝐦 𝐬𝐥𝐨𝐭 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐡𝐚𝐬𝐢𝐥 𝐦𝐚𝐤𝐬𝐢𝐦𝐚𝐥?𝐋𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐚𝐣𝐚 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖 𝐒𝐈𝐓𝐔𝐒 𝐒𝐋𝐎𝐓 𝐏𝐀𝐋𝐈𝐍𝐆 𝐁𝐀𝐍𝐘𝐀𝐊 𝐃𝐈𝐂𝐀𝐑𝐈 𝐃𝐈 𝐀𝐒𝐈𝐀, 𝐭𝐞𝐦𝐩𝐚𝐭𝐧𝐲𝐚 𝐩𝐚𝐫𝐚 𝐩𝐞𝐧𝐜𝐚𝐫𝐢 𝐜𝐮𝐚𝐧 𝐬𝐞𝐣𝐚𝐭𝐢!",
        "image_url": "https://i.postimg.cc/d1xjZN1q/FGSHYER.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐒𝐢𝐭𝐮𝐬 𝐭𝐞𝐫𝐩𝐞𝐫𝐜𝐚𝐲𝐚 𝟐𝟎𝟐𝟓 𝐦𝐞𝐧𝐠𝐡𝐚𝐝𝐢𝐫𝐤𝐚𝐧 𝐬𝐥𝐨𝐭-𝐬𝐥𝐨𝐭 𝐠𝐚𝐜𝐨𝐫 𝐝𝐚𝐫𝐢 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐫 𝐭𝐞𝐫𝐧𝐚𝐦𝐚 𝐬𝐞𝐩𝐞𝐫𝐭𝐢 𝐏𝐫𝐚𝐠𝐦𝐚𝐭𝐢𝐜 𝐏𝐥𝐚𝐲, 𝐇𝐚𝐛𝐚𝐧𝐞𝐫𝐨, 𝐝𝐚𝐧 𝐏𝐆 𝐒𝐨𝐟𝐭. 𝐃𝐞𝐧𝐠𝐚𝐧 𝐬𝐚𝐭𝐮 𝐚𝐤𝐮𝐧 𝐕𝐈𝐏, 𝐤𝐚𝐦𝐮 𝐛𝐢𝐬𝐚 𝐚𝐤𝐬𝐞𝐬 𝐬𝐞𝐦𝐮𝐚 𝐬𝐥𝐨𝐭 𝐠𝐚𝐜𝐨𝐫 𝐟𝐚𝐯𝐨𝐫𝐢𝐭𝐦𝐮!",
        "image_url": "https://i.postimg.cc/QCKkQg9c/yiuit7.png",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
    {
        "channel_id": -1002432716701,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝟐𝟖𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.imgur.com/evg6ThL.png",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },
 {
        "channel_id": -1002432716701,
        "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 ",
        "image_url": "https://i.imgur.com/ygMOQMr.png",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi288"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api288.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api288.pages.dev/"}
        ]
    },

    # ===== Channel 2 API88 -4820852926 =====
    {
        "channel_id": -4820852926,
        "text": "𝐥𝐚𝐧𝐠𝐬𝐮𝐧𝐠 𝐜𝐨𝐛𝐚 𝐩𝐨𝐥𝐚 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐚𝐧 𝐫𝐚𝐬𝐚𝐤𝐚𝐧 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐀𝐗𝐖𝐈𝐍!𝐆𝐚𝐛𝐮𝐧𝐠 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐝𝐚𝐧 𝐧𝐢𝐤𝐦𝐚𝐭𝐢 𝐞𝐯𝐞𝐧𝐭 𝐛𝐨𝐧𝐮𝐬 𝐡𝐚𝐫𝐢𝐚𝐧 𝐬𝐞𝐫𝐭𝐚 𝐣𝐚𝐜𝐤𝐩𝐨𝐭 𝐭𝐞𝐫𝐛𝐞𝐬𝐚𝐫 ",
        "image_url": "https://i.imgur.com/EFAmcrI.jpeg",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
        "image_url": "https://i.imgur.com/VliJaOa.jpeg",
        "time": "14:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    {
        "channel_id": -4820852926,
        "text": "𝐒𝐓𝐎𝐏 𝐑𝐔𝐍𝐆𝐊𝐀𝐃!! 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍 𝐀𝐍𝐃𝐀 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "18:40",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
  {
        "channel_id": -4820852926,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐀𝐏𝐈𝟖𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.imgur.com/7mMiWca.jpeg",
        "time": "23:50",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/loginapi88"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/API288/api88.apk"},
            {"text": "💸 Bukti Jackpot Lunas", "url": "https://jackpot-api88.pages.dev/"}
        ]
    },
    # ===== Channel 3 APINAGA -1002373443980 =====
    {
        "channel_id": -1002373443980,
        "text": "𝐒𝐎𝐋𝐔𝐒𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈𝐍𝐘𝐀!",
        "image_url": "https://i.postimg.cc/PxwQZz8Y/GWEGW.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
          	  {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
        ]
    },
    {
        "channel_id": -1002373443980,
            "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
            "image_url": "https://i.postimg.cc/Kjhr5knV/BZSEBE.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}
	]
     },

    {
        "channel_id": -1002373443980,
            "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟏𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
            "image_url": "https://i.imgur.com/xLkjflB.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
{
        "channel_id": -1002373443980,
            "text": "𝐒𝐩𝐢𝐧 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠. 𝐊𝐚𝐫𝐞𝐧𝐚 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧 𝐛𝐞𝐬𝐚𝐫 𝐭𝐚𝐤 𝐦𝐞𝐧𝐮𝐧𝐠𝐠𝐮 𝐥𝐚𝐦𝐚.🔥",
            "image_url": "https://i.imgur.com/zXrl6RG.png",
	    "time": "23:50",
            "buttons": [
           {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/APINAGA/apinaga.apk"},
            {"text": "⚡️ Link RTP", "url": "https://best-rtp-apinaga.store/"}

 ]
        },
                          # ===== Channel 3 BOSKU33 -1002568434905 =====
    {
        "channel_id": -1002568434905,
        "text": "𝐑𝐚𝐢𝐡 𝐬𝐞𝐧𝐬𝐚𝐬𝐢 𝐌𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢! 𝐒𝐥𝐨𝐭 𝐠𝐚𝐜𝐨𝐫, 𝐜𝐮𝐚𝐧 𝐦𝐚𝐤𝐬𝐢𝐦𝐚𝐥, 𝐛𝐮𝐤𝐭𝐢 𝐧𝐲𝐚𝐭𝐚!",
        "image_url": "https://i.postimg.cc/g0fvYXBJ/HR.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
        ]
    },
    {
        "channel_id": -1002568434905,
            "text": "𝐒𝐢𝐚𝐩𝐤𝐚𝐧 𝐝𝐢𝐫𝐢𝐦𝐮 𝐬𝐚𝐦𝐛𝐮𝐭 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧 𝐡𝐚𝐫𝐢 𝐢𝐧𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨 𝐫𝐢𝐧𝐠𝐚𝐧!",
            "image_url": "https://i.postimg.cc/G2Gv9LZj/GWGQ.png",
	    "time": "14:50",
            "buttons": [
              {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}
	]
     },

    {
        "channel_id": -1002568434905,
            "text": "🎰 𝐆𝐚𝐤 𝐡𝐚𝐫𝐮𝐬 𝐦𝐨𝐝𝐚𝐥 𝐛𝐞𝐬𝐚𝐫, 𝐤𝐞𝐜𝐢𝐥 𝐤𝐞𝐜𝐢𝐥𝐚𝐧 𝐛𝐢𝐬𝐚 𝐝𝐚𝐩𝐚𝐭 𝐣𝐮𝐭𝐚𝐚𝐧 𝐫𝐮𝐩𝐢𝐚𝐡",
            "image_url": "https://i.imgur.com/6I9IHM3.png",
	    "time": "18:40",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
         {
        "channel_id": -1002568434905,
            "text": "𝐖𝐔𝐉𝐔𝐃𝐊𝐀𝐍 𝐈𝐌𝐏𝐈𝐀𝐍𝐌𝐔 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐃𝐀𝐍 𝐑𝐀𝐈𝐇 𝐊𝐄𝐌𝐄𝐍𝐀𝐍𝐆𝐀𝐍𝐍𝐘𝐀 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆 𝐉𝐔𝐆𝐀!!",
            "image_url": "https://i.imgur.com/LhwK0uY.png",
	    "time": "23:50",
            "buttons": [
          {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/bosku33utama"},
            {"text": "📱 Unduh APK", "url": "https://storetn.in/BOSKU33/bosku33.apk"},
            {"text": "⚡️ Link RTP", "url": "https://rtpbosku33.online/"}

 ]
        },
 # ===== Grup 3 Hoki -1002336758098 =====
    {
        "channel_id": -1002336758098,
        "text": "𝐏𝐚𝐬𝐭𝐢 𝐩𝐫𝐨𝐟𝐢𝐭 𝐬𝐞𝐭𝐢𝐚𝐩 𝐡𝐚𝐫𝐢, 𝐭𝐚𝐧𝐩𝐚 𝐩𝐨𝐥𝐚 𝐝𝐚𝐧 𝐣𝐚𝐦 𝐠𝐚𝐜𝐨𝐫 𝐛𝐢𝐬𝐚 𝐦𝐚𝐱𝐰𝐢𝐧 𝐡𝐚𝐧𝐲𝐚 𝐝𝐞𝐧𝐠𝐚𝐧 𝐝𝐞𝐩𝐨𝐬𝐢𝐭 𝟐𝟎.𝟎𝟎𝟎. 𝐣𝐞𝐦𝐩𝐮𝐭 𝐡𝐨𝐤𝐢𝐦𝐮 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠 𝐣𝐮𝐠𝐚!!",
        "image_url": "https://i.postimg.cc/HWt7NhHj/mrtu.png",
        "time": "10:00",
        "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
          	  {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            	{"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
        ]
    },
    {
        "channel_id": -1002336758098,
            "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
            "image_url": "https://i.postimg.cc/zvpbRVpT/hdrher.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
	]
     },

    {
        "channel_id": -1002336758098,
            "text": "𝐌𝐚𝐢𝐧 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐣𝐞𝐦𝐩𝐮𝐭 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧𝐦𝐮⚡️",
            "image_url": "https://i.imgur.com/RCej5K0.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
        {
        "channel_id": -1002336758098,
            "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
            "image_url": "https://i.imgur.com/ppb86wb.png",
	    "time": "23:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/apinagautama"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

 ]
        },
    # ===== Channel 4 HOKI -1002262328897 =====
    {
        "channel_id": -1002262328897,
        "text": "𝐌𝐀𝐈𝐍 𝐓𝐀𝐍𝐏𝐀 𝐏𝐎𝐋𝐀 𝐁𝐈𝐒𝐀 𝐁𝐔𝐀𝐓 𝐊𝐀𝐌𝐔 𝐌𝐄𝐍𝐀𝐍𝐆 𝐁𝐄𝐒𝐀𝐑 𝐂𝐔𝐌𝐀 𝐃𝐈 𝐇𝐎𝐊𝐈𝟏𝟕𝟖, 𝐂𝐎𝐁𝐀𝐈𝐍 𝐒𝐄𝐊𝐀𝐑𝐀𝐍𝐆!!",
        "image_url": "https://i.postimg.cc/HWt7NhHj/mrtu.png",
        "time": "10:00",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    },
    {
        "channel_id": -1002262328897,
            "text": "𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐁𝐑𝐀𝐏𝐀𝐏𝐔𝐍 𝐏𝐀𝐒𝐓𝐈 𝐃𝐈 𝐁𝐀𝐘𝐀𝐑 𝐊𝐎𝐍𝐓𝐀𝐍 !",
            "image_url": "https://i.postimg.cc/zvpbRVpT/hdrher.png",
	    "time": "14:50",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}

	]
     },

    {
        "channel_id": -1002262328897,
            "text": "𝐌𝐚𝐢𝐧 𝐬𝐞𝐤𝐚𝐫𝐚𝐧𝐠, 𝐣𝐞𝐦𝐩𝐮𝐭 𝐤𝐞𝐛𝐞𝐫𝐮𝐧𝐭𝐮𝐧𝐠𝐚𝐧𝐦𝐮⚡️",
            "image_url": "https://i.imgur.com/RCej5K0.png",
	    "time": "18:40",
            "buttons": [
            {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
     ]
        },
        {
        "channel_id": -1002262328897,
       "text": "𝐒𝐎𝐋𝐔𝐒𝐈 𝐌𝐄𝐍𝐀𝐍𝐆 𝐀𝐃𝐀 𝐃𝐈𝐒𝐈𝐍𝐈, 𝐉𝐀𝐂𝐊𝐏𝐎𝐓 𝐓𝐀𝐍𝐏𝐀 𝐁𝐀𝐓𝐀𝐒 𝐒𝐄𝐓𝐈𝐀𝐏 𝐇𝐀𝐑𝐈𝐍𝐘𝐀!",
        "image_url": "https://i.imgur.com/ppb86wb.png",
        "time": "23:50",
        "buttons": [
             {"text": "🔗 Gabung Sekarang", "url": "https://cutt.ly/utamahoki178"},
            {"text": "📱 Unduh APK", "url": "https://apk-depot.s3.ap-northeast-1.amazonaws.com/hoki178.apk"},
            {"text": "⚡️ Link RTP", "url": "https://hoki178tyrtp.site/"}
 	]

    }
    ]  # <- TIDAK ADA koma di sini jika ini adalah elemen terakhir
}






slot_times = ["09:02","10:00", "15:08", "18:45", "23:50"]          # ← sesuaikan kalau mau 17:33

async def send_scheduled_post(slot_index):
    today = datetime.now().strftime("%A").lower()
    target_time = slot_times[slot_index]           # “waktu yang dicari”
    posts_today = weekly_posts.get(today, [])

    matched_posts = [p for p in posts_today if p.get("time") == target_time]

    if not matched_posts:
        print(f"⚠️ Tidak ada postingan cocok untuk jam {target_time} hari {today}")
        return

    for post in matched_posts:
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(btn["text"], url=btn["url"])] for btn in post["buttons"]]
            
        )
        try:
            photo = post.get("image_path") or post.get("image_url")
            await bot.send_photo(
                chat_id=post["channel_id"],
                photo=photo,
                caption=post["text"],
                reply_markup=keyboard,
                parse_mode=ParseMode.HTML
            )
            print(f"✅ Terkirim ke {post['channel_id']} - {post['text']} [{target_time}]")
        except Exception as e:
            print(f"❌ Gagal kirim ke {post['channel_id']} - {post['text']} error: {e}")

            


    else:
        print(f"⚠️ Tidak ada post untuk hari {today} di slot {slot_index}")

# ⬇️ Letakkan ini sebelum main()
async def schedule_post(slot_index):
    await send_scheduled_post(slot_index)



async def main():
    scheduler = AsyncIOScheduler()
    # Jadwal pengiriman per slot (slot_index 0 = pagi, 1 = siang, 2 = malam)
    scheduler.add_job(schedule_post, 'cron', day_of_week='mon-sun', hour=9, minute=2, args=[0], misfire_grace_time=60)
    scheduler.add_job(schedule_post, 'cron', day_of_week='mon-sun',hour=10, minute=0, args=[1],misfire_grace_time=60)   # Pagi
    scheduler.add_job(schedule_post, 'cron', day_of_week='mon-sun',hour=15, minute=8, args=[2],misfire_grace_time=60)  # Test saat ini
    scheduler.add_job(schedule_post, 'cron', day_of_week='mon-sun',hour=18, minute=45, args=[3],misfire_grace_time=60)  # Malam
    scheduler.add_job(schedule_post, 'cron', day_of_week='mon-sun', hour=23,minute=50, args=[4], misfire_grace_time=60)  # Tengah malam
    scheduler.start()

    print("🤖 Bot aktif dan menjadwalkan postingan otomatis setiap hari.")
    while True:
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())