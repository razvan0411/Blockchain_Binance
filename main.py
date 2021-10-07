import asyncio
import json

from binance import AsyncClient


async def main():
    client = await AsyncClient.create()

    # fetch exchange info
    # res = await client.get_exchange_info()
    # res = await client.get_recent_trades(symbol="BNBBTC")
    res = await client.get_symbol_ticker(symbol='ETHBUSD')
    print(json.dumps(res, indent=2))
    await client.close_connection()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
