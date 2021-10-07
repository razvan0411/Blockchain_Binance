import asyncio
import pandas as pd
import matplotlib.pyplot as plt


# Exercise 3


from binance import AsyncClient


async def main():
    client = await AsyncClient.create()
    df = pd.DataFrame(await client.futures_historical_klines(
        symbol="ETHBUSD",
        interval="1m",
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
    df = df.set_index("date")

    df1 = df.rolling(10).mean().rename(columns={'close': 'rolling'}, inplace=False)
    ax = df1.plot()
    df2 = df.ewm(com=10).mean().rename(columns={'close': 'ewm'}, inplace=False)
    df2.plot(ax=ax)
    plt.show()

    await client.close_connection()


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
