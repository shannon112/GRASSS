def sell_all_at_once(df, mystock):
    the_date_price = df.loc[df.index[0]]["Open"]
    benefit = (the_date_price - mystock.price) * mystock.quantity + mystock.dividend
    benefit_percentage = benefit / mystock.cost
    return benefit_percentage
