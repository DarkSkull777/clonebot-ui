from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Buttons used

home_button = [

    [InlineKeyboardButton("🌏 Sumber", "source_btn"),

     InlineKeyboardButton("⬇️  Fr. Id", "from_btn"),

     InlineKeyboardButton("🌹 Creator", url="https://t.me/xskull7")],

    [InlineKeyboardButton("🎯 Target", "target_btn"),

     InlineKeyboardButton("⬆️  Untuk Id", "up_to_btn"),

     InlineKeyboardButton("Tipe  ➡", "types_btn")],

    [InlineKeyboardButton("Terlambat", "delay_btn"),

     InlineKeyboardButton("Keterangan", "caption_btn"),

     InlineKeyboardButton("FNAC", "f_caption_btn")],

    [InlineKeyboardButton("🔎️  Melihat", "view_btn"),

     InlineKeyboardButton("🚮  Setel ulang", "rst_btn"),

     InlineKeyboardButton("❌  Tutup", "close_btn")],

    [InlineKeyboardButton("🚦 Media Klon 🚦", "clone_btn")]

]

start_button = [

    [InlineKeyboardButton("🏅 Creator 🏅", url="https://t.me/xskull7"),

     InlineKeyboardButton("⚙️ Pengaturan ⚙", "start_btn")]

]

types_button = [

    [InlineKeyboardButton(" ⏺ Docs", "docs_btn"),

     InlineKeyboardButton(" ⏺ Video", "video_btn"),

     InlineKeyboardButton(" ⏺ Audio", "audio_btn")],

    [InlineKeyboardButton(" ⏺ Foto", "photo_btn"),

     InlineKeyboardButton(" ⏺ Suara", "voice_btn"),

     InlineKeyboardButton("⚙️ Melihat", "view_types")],

    [InlineKeyboardButton("⬅️ Kembali", "start_btn")]

]

stop_button = [

    [InlineKeyboardButton("🚫 STOP 🚫", "stop_clone")]

]

finished_button = [

    [InlineKeyboardButton("🏠  AWAL", "start_btn"),

     InlineKeyboardButton("❌  TUTUP", "close_btn")]

]

terminate_btn = [

    [InlineKeyboardButton("🧸 Channel", url="https://t.me/botdimasdoang"),

     InlineKeyboardButton("🌐 Website", url="https://darkskull7.my.to")],

    [InlineKeyboardButton("🚫 Mengakhiri", "terminate_btn"),

     InlineKeyboardButton("🏠 Awal", "start_btn")]

]

# markups used

reply_markup_stop = InlineKeyboardMarkup(stop_button)

reply_markup_home = InlineKeyboardMarkup(home_button)

reply_markup_start = InlineKeyboardMarkup(start_button)

reply_markup_terminate = InlineKeyboardMarkup(terminate_btn)

reply_markup_finished = InlineKeyboardMarkup(finished_button)

reply_markup_types_button = InlineKeyboardMarkup(types_button)
