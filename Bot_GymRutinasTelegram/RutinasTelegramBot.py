import os
from telegram import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler
from archivotron import busca_arreglo

load_dotenv()
token_telegram = os.environ['token']


# Función para responder al comando /start
async def start(update: Update, context: CallbackContext):
    botones = [
        [KeyboardButton("Pecho"), KeyboardButton("Espalda")],
        [KeyboardButton("Piernas"), KeyboardButton("Biceps")],
        [KeyboardButton("Triceps"), KeyboardButton("Hombros")]
    ]

    markup = ReplyKeyboardMarkup(botones, resize_keyboard=True)

    await update.message.reply_text(
        "💪 ¡Hola! Soy tu bot de rutinas de gym.\nSelecciona un grupo muscular: Pecho, Espalda, Piernas, Biceps, Triceps o Hombros",
        reply_markup=markup
    )

# Función para el comando /rutina
async def rutina(update: Update, context: CallbackContext):
    if context.args:
        grupo = " ".join(context.args).lower()
        value_return = busca_arreglo(grupo)
        await update.message.reply_text(value_return)
    else:
        await update.message.reply_text("Por favor, indica un grupo muscular. Ejemplo: /rutina pecho")

# Función de Echo: Responde con el mismo mensaje que recibe
async def echo(update: Update, context: CallbackContext):
    user_text = update.message.text
    value_return = busca_arreglo(user_text)
    await update.message.reply_text(value_return)

# Configuración del bot
app = Application.builder().token(token_telegram).build()

# Agregar manejadores (Handlers)
app.add_handler(CommandHandler("start", start))           # /start
app.add_handler(CommandHandler("rutina", rutina))         # /rutina pecho
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # texto común

# Iniciar el bot
print("🤖 Bot de rutinas de gym iniciado...")
app.run_polling()
