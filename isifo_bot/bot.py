import hikari
import tanjun
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")

def build_bot() -> hikari.GatewayBot:
    bot = hikari.GatewayBot(TOKEN)
    make_client(bot)

    return bot

def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    client = (
        tanjun.Client.from_gateway_bot(
            bot,
            mention_prefix=True,
            set_global_commands=1025502805601042533
        )
    ).add_prefix("!")

    client.load_modules("plugins.utilities")

    return client

