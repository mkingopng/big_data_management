import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)


table = [
    ['Rose Cottage', '3 Jan 2020', 'Mike Jones', 'Phone: 0555324176, arrive at 5pm'],
    ['The Manor', '10 - 12 Jan 2020', 'Ariah Carmichael', 'phone: 0555788766, arrive at 5.30pm, wants a late checkout'],
    ['Lake View', '16 Feb 2020', 'Gloria Rayo', 'No phone, arrive at 8pm'],
    ['Hilltop', '1 - 4 Feb', 'Ben Montgomery and Paul Johnson', 'Phone 0555333456, arrive unknown'],
    ['Serenity', '24 Feb 2020', 'Sue Davies + 3 kids', 'Phone 0555 998766, arrive 3pm'],
    ['Lake View', '6 - 7 Mar 2020', 'Conrad Palin', 'Phone: 0555 6555 434, arrival unknown, late checkout'],
    ['Lake View', '11 Mar 2020', 'Amber Langtree', 'Email amber@net.site, arrive at 6pm'],
    ['Rose Cottage', '10 Jan 2020', 'Mike Jones', 'Phone: 0555 324176, arrive at 4.30pm'],
    ['Hilltop', '1 Mar 2020', 'Sue Davies (no kids this time)', 'same phone, late checkout'],
    ['Rose Cottage', '17 Jan 2020', 'Mike and Melanie Jones', 'Phone: Mike usual phone, Melanie 0555 654769, arrive at 6 pm']
    ]

df = pd.DataFrame(table)

print(df)

# split into database tables

