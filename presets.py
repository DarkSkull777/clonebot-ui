# ----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#

class Presets(object):

    START_TEXT = """

Halo... {}

    """

    WELCOME_TEXT = "⭑⭑★✪ BANTUAN untuk info lebih lanjut: ✪★⭑⭑"

    MESSAGE_COUNT = """

𝙇𝙞𝙫𝙚: <code>{}\n{}\n{}</code>\n

𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐈𝐝 : <b>{}</b>

𝐍𝐨𝐰@         : <b>{}</b>

𝐄𝐧𝐝𝐢𝐧𝐠 𝐈𝐝   : <b>{}</b>

𝐂𝐥𝐨𝐧𝐞 𝐃𝐞𝐥𝐚𝐲                  : {}

𝐃𝐞𝐟𝐚𝐮𝐥𝐭 𝐂𝐚𝐩𝐭𝐢𝐨𝐧           : {}

𝐅𝐢𝐥𝐞 𝐧𝐚𝐦𝐞 𝐚𝐬 𝐂𝐚𝐩𝐭𝐢𝐨𝐧  : {}

𝕋𝕠𝕥𝕒𝕝 ℂ𝕠𝕡𝕚𝕖𝕕              : <b>{}</b>

𝕋𝕠𝕥𝕒𝕝 ℂ𝕠𝕞𝕡𝕝𝕖𝕥𝕖𝕕      : <b>{} %</b> 󠀥

📚 Dokumen             : <b>{}</b>

🎞 Video                     : <b>{}</b>

🔊 Audio                     : <b>{}</b>

📸 Foto                     : <b>{}</b>

🗣 Suara                        : <b>{}</b>

🧩 File duplikat       : <b>{}</b>

⏳ Waktu yang Diambil            : <b>{}</b>

🆙 Waktu aktif bot             : <b>{}</b>

📲 Klon dimulai pada    : <b>{}</b>

📌 Terakhir diperbarui saat   : <b>{}</b>

    """

    INFO_CHAT_TYPES = """

Anda dapat memasukkan jenis berikut::

Id           : 123456789 (-100 tidak minta.)

Invite Link  : https://t.me/joinchat

Publik Link : https://t.me/python

Username  : @python

    """

    SELECTED_TYPE = """

Anda telah memilih:

------------------------------

Dokumen : {}

Audio         : {}

Video         : {}

Foto         : {}

Suara          : {}

    """

    VIEW_CONF = """

Id Sumber : {}

Id Target : {}

Dari pesan id : {} | 𝐓𝐨 𝐦𝐬𝐠 𝐈𝐝 : {}

Terlambat : {} | 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 : {} | 𝐅𝐍 𝐂𝐚𝐩𝐭𝐢𝐨𝐧: {}

Tipe: 📚:{} | 🎞:{} | 🔊:{} | 📸:{} | 🗣:{}

    """

    FILE_TYPES = ["document", "video", "audio", "voice", "photo"]

    COPIED_MESSAGES = "<b><a href='https://github.com/DarkSkull777/Dim7'>Medias Copied</a></b>"

    IN_CORRECT_PERMISSIONS_MESSAGE_DEST_POSTING = "Akses ditolak\n\nPengguna bukan admin atau tidak memiliki hak posting di bagan yang diberikan\n" \

    USER_ABSENT_MSG = "Obrolan sesi tidak aktif target chat yang diberikan"

    CANCEL_CLONE = "Proses di stop... tunggu sebentar 🕚"

    CANCELLED_MSG = "⚠      Pengguna membatalkan kloning      ⚠"

    INITIAL_MESSAGE_TEXT = "Mencari media  🔎"

    WAIT_MSG = "Tunggu beberapa detik...."

    SOURCE_CONFIRM = """

𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞: {}

𝐂𝐡𝐚𝐭 𝐈𝐝: <code> {}</code>

𝐂𝐡𝐚𝐭 𝐓𝐲𝐩𝐞: {}

𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {}

𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {}

𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {}

\xad                                                              \xad

S̶o̶u̶r̶c̶e̶ C̶h̶a̶t̶ 𝐒𝐚𝐯𝐞𝐝  ✅

                     """

    DEST_CNF = """

𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞: {}

𝐂𝐡𝐚𝐭 𝐈𝐝: <code> {}</code>

𝐂𝐡𝐚𝐭 𝐓𝐲𝐩𝐞: {}

𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: {}

𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: {}

𝐌𝐞𝐦𝐛𝐞𝐫𝐬: {}

\xad                                                              \xad

T̶a̶r̶g̶e̶t̶ C̶h̶a̶t̶ 𝐒𝐚𝐯𝐞𝐝  ✅

               """

    SESSION_START_INFO = """

Sesi pengguna dimulai:

Tanggal     :  {}

Waktu    :  {}

Sesi pengguna dimulai di akun Anda, jika Anda tahu ini, biarkan bot ini tidak diblokir, Anda dapat Abaikan pesan ini, jika Anda merasa ingin mengacau, hentikan sesi ini dan blokir bot ini untuk menghindari penggunaan sesi Anda lagi, Anda dapat lihat pesan ini lagi ketika heroku free dynos restart

    """

    NOT_CONFIGURED = "𝙎𝙤𝙪𝙧𝙘𝙚 & 𝙏𝙖𝙧𝙜𝙚𝙩 𝙘𝙝𝙖𝙩𝙨 𝙣𝙤𝙩 𝙘𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚𝙙 ⚠"

    NOT_AUTH_TEXT = "𝙔𝙤𝙪 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙  ⚠ "

    BOT_BLOCKED_MSG = "Bot is blocked by the  session user !"

    NOT_CONFIGURED_CLONE = "𝙉𝙤 𝙘𝙝𝙖𝙩 𝙘𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙛𝙤𝙪𝙣𝙙 ⚠\n\n𝘾𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚 𝙩𝙝𝙚 𝙎𝙤𝙪𝙧𝙘𝙚 & 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙮𝙤𝙪 𝙘𝙡𝙤𝙣𝙚 🤷"

    FINISHED_TEXT = "𝘾𝙡𝙤𝙣𝙚  𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮  ✅"

    TERMINATED_MSG = "🚫 𝘽𝙤𝙩 𝙏𝙚𝙧𝙢𝙞𝙣𝙖𝙩𝙚𝙙 🚫\n𝘍𝘦𝘦𝘭𝘴 𝘴𝘰𝘮𝘦𝘵𝘩𝘪𝘯𝘨 𝘧𝘪𝘴𝘩𝘺? 𝘉𝘭𝘰𝘤𝘬 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 𝘵𝘰 𝘢𝘷𝘰𝘪𝘥 𝘵𝘩𝘦 𝘶𝘴𝘢𝘨𝘦 𝘰𝘧 𝘺𝘰𝘶𝘳 𝘴𝘦𝘴𝘴𝘪𝘰𝘯 𝘢𝘨𝘢𝘪𝘯 !"

    COPY_ERROR = "𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙬𝙚𝙣𝙩 𝙬𝙧𝙤𝙣𝙜 !\n\n𝘊𝘰𝘱𝘺𝘪𝘯𝘨 𝘢𝘣𝘰𝘳𝘵𝘦𝘥 𝘣𝘺 𝘵𝘩𝘦 𝘴𝘺𝘴𝘵𝘦𝘮\n𝘊𝘩𝘦𝘤𝘬 𝘢𝘭𝘭 𝘵𝘩𝘦 𝘶𝘴𝘦𝘳 𝘱𝘦𝘳𝘮𝘪𝘴𝘴𝘪𝘰𝘯𝘴."

    INVALID_CHAT_ID = "<u>𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙘𝙝𝙖𝙩 𝙥𝙖𝙧𝙖𝙢𝙚𝙩𝙚𝙧 𝙛𝙤𝙪𝙣𝙙</u>\n\n𝐂𝐚𝐮𝐬𝐞𝐬:\n1. 𝘚𝘦𝘴𝘴𝘪𝘰𝘯 𝘶𝘴𝘦𝘳 𝘯𝘰𝘵 𝘪𝘯 𝘗𝘳𝘪𝘷𝘢𝘵𝘦 𝘤𝘩𝘢𝘵\n" \

                      "2. 𝘍𝘰𝘳 𝘱𝘶𝘣𝘭𝘪𝘤 𝘤𝘩𝘢𝘵𝘴, 𝘶𝘴𝘦 '@𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦'\n𝘰𝘳 𝘭𝘪𝘯𝘬 𝘪𝘯𝘴𝘵𝘦𝘢𝘥 𝘰𝘧 '𝘪𝘥'"

    ASK_SOURCE = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙝𝙖𝙩 𝙞𝙣𝙛𝙤:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."

    ASK_DESTINATION = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩 𝙞𝙣𝙛𝙤:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."

    ASK_START_MSG_ID = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙨𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝙙:\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."

    ASK_END_MSG_ID = "𝙂𝙞𝙫𝙚 𝙩𝙝𝙚 𝙚𝙣𝙙 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙄𝙙\n𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 30𝑆𝑒𝑐 𝑡𝑜 𝑑𝑜 𝑡ℎ𝑖𝑠.."

    CHAT_DUPLICATED_MSG = "𝙎𝙤𝙪𝙧𝙘𝙚 & 𝘿𝙚𝙨𝙩𝙞𝙣𝙖𝙩𝙞𝙤𝙣 𝙘𝙝𝙖𝙩 𝙄𝙙𝙨 𝙘𝙖𝙣'𝙩 𝙗𝙚 𝙨𝙖𝙢𝙚 "

    FROM_MSG_ID_CNF = "𝐒𝐭𝐚𝐫𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐝:👉 <code>{}</code> 👈 𝐒𝐚𝐯𝐞𝐝  ✅"

    END_MSG_ID_CNF = "𝐄𝐧𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐝:👉 <code>{}</code> 👈 𝐒𝐚𝐯𝐞𝐝  ✅"

    INVALID_MSG_ID = "𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙞𝙙 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙖𝙣 𝙄𝙣𝙩𝙚𝙜𝙚𝙧 ❗️"

    INVALID_REPLY_MSG = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙧𝙚𝙥𝙡𝙖𝙮 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 ❗️"

    CNF_SOURCE_FIRST = "𝘾𝙤𝙣𝙛𝙞𝙜𝙪𝙧𝙚 𝙩𝙝𝙚 𝙨𝙤𝙪𝙧𝙘𝙚 𝙘𝙝𝙖𝙩 𝙛𝙞𝙧𝙨𝙩  ❗️"

    DELAY_OFF = "𝘿𝙚𝙡𝙖𝙮𝙚𝙙 𝙘𝙡𝙤𝙣𝙚 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"

    DELAY_ON = "𝘿𝙚𝙡𝙖𝙮𝙚𝙙 𝙘𝙡𝙤𝙣𝙚 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✅"

    ADD_DOC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 👈 𝙖𝙙𝙙𝙚𝙙"

    RM_DOC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "

    ADD_VID = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙞𝙙𝙚𝙤 👈 𝙖𝙙𝙙𝙚𝙙"

    RM_VID = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙞𝙙𝙚𝙤 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "

    ADD_AUD = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘼𝙪𝙙𝙞𝙤 👈 𝙖𝙙𝙙𝙚𝙙"

    RM_AUD = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝘼𝙪𝙙𝙞𝙤 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "

    ADD_PIC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙋𝙝𝙤𝙩𝙤 👈 𝙖𝙙𝙙𝙚𝙙"

    RM_PIC = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙋𝙝𝙤𝙩𝙤 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "

    ADD_VOI = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙤𝙞𝙘𝙚 👈 𝙖𝙙𝙙𝙚𝙙"

    RM_VOI = "𝙁𝙞𝙡𝙚 𝙩𝙮𝙥𝙚 👉 𝙑𝙤𝙞𝙘𝙚 👈 𝙞𝙜𝙣𝙤𝙧𝙚𝙙 "

    BLANK = "➖➖➖➖➖➖➖➖➖➖➖➖➖"

    BLOCK = "ᴘʀᴏɢʀᴇꜱꜱ ꜰᴀɪʟᴇᴅ ᴛᴏ ᴅɪꜱᴘʟᴀʏ :👉 ʜᴇʟᴘ"

    CAPTION_ON = "𝘾𝙖𝙥𝙩𝙞𝙤𝙣 𝙤𝙣 𝙛𝙞𝙡𝙚𝙨 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✅"

    CAPTION_OFF = "𝘾𝙖𝙥𝙩𝙞𝙤𝙣 𝙤𝙣 𝙛𝙞𝙡𝙚𝙨 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"

    FN_AS_CAPT_ON = "𝙁𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 : 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 ✅"

    FN_AS_CAPT_OFF = "𝙁𝙞𝙡𝙚 𝙣𝙖𝙢𝙚 𝙖𝙨 𝙘𝙖𝙥𝙩𝙞𝙤𝙣 : 𝘿𝙚𝙖𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 🚫"

    NOT_REQUIRED = "𝙏𝙝𝙞𝙨 𝙛𝙞𝙚𝙡𝙙 𝙞𝙨 𝙣𝙤𝙩 𝙈𝙖𝙙𝙖𝙩𝙤𝙧𝙮  ⚠"

    RST_MSG = "𝙍𝙚𝙨𝙚𝙩 𝙩𝙤 𝘽𝙤𝙩 𝙙𝙚𝙛𝙖𝙪𝙡𝙩𝙨 .. 𝘾𝙤𝙣𝙛𝙞𝙧𝙢𝙚𝙙 ✅"

    OVER_FLOW = "𝙈𝙖𝙭𝙞𝙢𝙪𝙢 𝙡𝙞𝙢𝙞𝙩 𝙞𝙨 𝙚𝙭𝙘𝙚𝙚𝙙𝙚𝙙 !\n𝘾𝙝𝙚𝙘𝙠 𝙩𝙝𝙚 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙡𝙞𝙢𝙞𝙩, 𝙏𝙧𝙮 𝙖𝙜𝙖𝙞𝙣 !"

    SELECT_TYPE = "👉 𝙎𝙚𝙡𝙚𝙘𝙩𝙞𝙤𝙣 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙩𝙤𝙜𝙜𝙡𝙚𝙙 𝙤𝙣 𝙩𝙖𝙥\n𝘈𝘭𝘭 𝘢𝘳𝘦 𝘴𝘦𝘭𝘦𝘤𝘵𝘦𝘥 𝘣𝘺 𝘥𝘦𝘧𝘢𝘶𝘭𝘵 !"
