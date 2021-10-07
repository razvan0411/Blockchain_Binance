import asyncio
from binance import AsyncClient, BinanceSocketManager
from datetime import datetime

# Exercise 1


async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.trade_socket('ETHBUSD')
    # then start receiving messages
    start_time = 0
    wait_time = 1 * 60 * 60 * 1000  # time is in milliseconds ( 1h * 60m * 60s * 1000ms)
    wait_time = 2000
    with open('price_for_' + str(int(wait_time/1000)) + 's.csv', 'w') as d:
        d.write(f'EVENT TIME, PRICE\n')
        async with ts as tscm:
            while True:
                res = await tscm.recv()
                if start_time == 0:
                    # E = Event time; T = Trade time;
                    start_time = res['E']
                if res['E'] > start_time + wait_time:
                    break
                print(res)
                event_time = datetime.fromtimestamp(res['E']/1000.0).strftime("%Y-%m-%d %H:%M:%S.%f")
                # print(event_time)
                d.write(f'{event_time}, {res["p"]}\n')
                # print(res['p'])
        await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    # help(BinanceSocketManager)
