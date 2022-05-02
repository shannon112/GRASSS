def sell_all_at_once(df, mystock):
    the_date_price = df.loc[df.index[0]]["Open"]
    benefit = (the_date_price - mystock.price) * mystock.quantity + mystock.dividends
    benefit_percentage = benefit / mystock.cost
    print(f"{df.index[0]} selling {mystock.str_info()} at {the_date_price}")
    return benefit_percentage
