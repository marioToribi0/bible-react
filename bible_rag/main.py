from interface.interface import interface_assistant
import asyncio
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")


async def main():
    await interface_assistant()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
