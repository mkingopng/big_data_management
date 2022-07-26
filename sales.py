import pandas as pd

sales = "2543,4,4.34;5463,7,8.31;7765,10,1.23;9833,9,34.12;5056,4,5.67;7657,10,4.23;3343,7,2.98;3778,9,9.27;1118,5," \
        "8.23;3873,3,4.45;6588,2,5.67;5778,6,3.41;7765,11,2.23;9343,8,4.12;5057,5,4.67;7657,5,4.23;3356,7,4.98;3776," \
        "8,8.27;1228,5,7.23;3873,2,4.50"

# split on the ';'
data = sales.split(";")

# split on the ','
new_data = []
for item in data:
    new_item = item.split(",")
    new_data.append(new_item)

# convert example - file statistics list of lists to example - file statistics dataframe:
df = pd.DataFrame(new_data)
df.rename(columns={0: 'transaction_number', 1: 'quantity', 2: 'price_per_unit'}, inplace=True)
df['quantity'] = pd.to_numeric(df['quantity'])
df['price_per_unit'] = pd.to_numeric(df['price_per_unit'])
df['sale_value'] = df['quantity'] * df['price_per_unit']  # calculate the value of each sale

# sum the transaction column
total = df['sale_value'].sum()
print(total)
