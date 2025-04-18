import requests
import time
import telebot
import threading

TOKEN = 'SEU_TOKEN_AQUI'
GROUP_ID = -1002656045672
USERNAME_STRIPCHAT = 'BabyPandinha'  # Apenas o nome do perfil

bot = telebot.TeleBot(TOKEN)
live_ativa = False

def esta_ao_vivo():
    url = f"https://br.stripchat.com/{USERNAME_STRIPCHAT}"
    response = requests.get(url)
    return 'isLive":true' in response.text

def checar_live():
    global live_ativa
    while True:
        try:
            if esta_ao_vivo():
                if not live_ativa:
                    mensagem = f"🚨 A Pandinha está AO VIVO agora! 🐼\n👉 https://br.stripchat.com/{USERNAME_STRIPCHAT}"
                    bot.send_message(GROUP_ID, mensagem)
                    live_ativa = True
            else:
                live_ativa = False
            time.sleep(60)
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(60)

@bot.message_handler(commands=['status'])
def responder_status(message):
    try:
        if esta_ao_vivo():
            bot.reply_to(message, f"Sim! A Pandinha está AO VIVO agora 🐼✨\n👉 https://br.stripchat.com/{USERNAME_STRIPCHAT}")
        else:
            bot.reply_to(message, "Não, a Pandinha não está ao vivo no momento 😴💤")
    except Exception as e:
        bot.reply_to(message, f"Ocorreu um erro ao verificar: {e}")

# Roda a checagem de live em uma thread separada
threading.Thread(target=checar_live).start()

# Inicia o bot para responder comandos como /status
bot.polling()
