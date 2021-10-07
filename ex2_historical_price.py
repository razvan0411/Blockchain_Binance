import asyncio
import pandas as pd

# Exercise 2


from binance import AsyncClient


async def main():
    client = await AsyncClient.create()
    df = pd.DataFrame(await client.futures_historical_klines(
        symbol="ETHBUSD",
        interval="1d",
        start_str="2021-09-27",
        end_str="2021-09-28"
    ))
    # print(df)

    # crop unnecessary columns
    df = df.iloc[:, [0, 4]]
    # print(df)

    # ascribe names to columns
    df.columns = ['date', 'close']
    # convert timestamp to date format and ensure ohlcv are all numeric
    df['date'] = pd.to_datetime(df['date'], unit='ms')
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(df[col])
    print(df)

    await client.close_connection()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
