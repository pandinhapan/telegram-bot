bot.py

import telebot

# Substitua pelo token do seu bot
TOKEN = "8000475061:AAEWVAtLD0WIwyMggNP10c-J8VM4P6awaP"
bot = telebot.TeleBot(TOKEN)

# Comando para exibir os planos VIP
@bot.message_handler(commands=["planos"])
def enviar_planos(message):
    texto = """
📢 *Planos de Assinatura VIP* 💎

📅 *7 dias* → [PAGAMENTO BRASIL](https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808496006dfa01960148fbc40063) | [PAGAMENTO INTERNACIONAL](https://buy.stripe.com/5kAcNcdXOg1g8N2144)

📅 *1 mês* → [PAGAMENTO BRASIL](https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808496006df201960148637f0055) | [PAGAMENTO INTERNACIONAL](https://buy.stripe.com/9AQ00q2f64iy8N29AE)

📅 *3 meses (-10%)* → [PAGAMENTO BRASIL](https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808496006df201960147f2090054) | [PAGAMENTO INTERNACIONAL](https://buy.stripe.com/3cs28y5ri4iygfu9AD)

📅 *6 meses (-15%)* → [PAGAMENTO BRASIL](https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808496006df20196014768740053) | [PAGAMENTO INTERNACIONAL](https://buy.stripe.com/aEUbJ806Y9CS1kA4gi)

📅 *1 ano (-20%)* → [PAGAMENTO BRASIL](https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=2c93808496006dfa01960146878e0062) | [PAGAMENTO INTERNACIONAL](https://buy.stripe.com/9AQdRg7zqcP4e7maEF)

💡 Após o pagamento, envie o comprovante para liberar seu acesso VIP.
    """
    bot.send_message(message.chat.id, texto, parse_mode="Markdown")

# Iniciar o bot
bot.polling()
