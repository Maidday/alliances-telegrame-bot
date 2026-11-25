import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from variables import Systemvariables

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("root").setLevel(logging.INFO)
logger = logging.getLogger(__name__)

sysVars = Systemvariables()

if __name__ == "__main__":
    logger.info("Start bot")
    application = Application.builder().token(sysVars.getToken()).build()
