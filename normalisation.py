import pandas as pd

pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)


table = [
    ['Rose Cottage', '3 Jan 2020', 'Mike Jones', 'Phone: 0555324176, arrive at 5pm'],
    ['The Manor', '10 - 12 Jan 2020', 'Ariah Carmichael', 'phone: 0555788766, arrive at 5.30pm, wants example_file_statistics late checkout'],
    ['Lake View', '16 Feb 2020', 'Gloria Rayo', 'No phone, arrive at 8pm'],
    ['Hilltop', '1 - 4 Feb', 'Ben Montgomery and Paul Johnson', 'Phone 0555333456, arrive unknown'],
    ['Serenity', '24 Feb 2020', 'Sue Davies + 3 kids', 'Phone 0555 998766, arrive 3pm'],
    ['Lake View', '6 - 7 Mar 2020', 'Conrad Palin', 'Phone: 0555 6555 434, arrival unknown, late checkout'],
    ['Lake View', '11 Mar 2020', 'Amber Langtree', 'Email amber@net.site, arrive at 6pm'],
    ['Rose Cottage', '10 Jan 2020', 'Mike Jones', 'Phone: 0555 324176, arrive at 4.30pm'],
    ['Hilltop', '1 Mar 2020', 'Sue Davies (no kids this time)', 'same phone, late checkout'],
    ['Rose Cottage', '17 Jan 2020', 'Mike and Melanie Jones', 'Phone: Mike usual phone, Melanie 0555 654769, arrive at 6 pm']
    ]

table_df = pd.DataFrame(table)

# mk: split up column 3 into guest_table.csv
guests_table = {0: 'first_name', 1: 'last_name', 2: '1', 3: '2', 4: '3', 5: '4'}
guests_df = table_df[2].str.split(pat=' ', expand=True).rename(mapper=guests_table, axis=1)
new = {
    'first_name': ['Mike', 'Melanie', 'Paul'],
    'last_name': ['Jones', 'Jones', 'Johnson']
}
new_guests = pd.DataFrame(new)
guests_df = guests_df.drop(['1', '2', '3', '4'], axis=1).reset_index(drop=True)
guests_df = pd.concat([guests_df, new_guests], keys=['first_name', 'first_name'], ignore_index=True, axis=0)
guests_df = guests_df.drop(9, axis=0, inplace=False)
guests_df = guests_df.reset_index(drop=True, inplace=False)
guests_df = guests_df.reset_index(drop=False, inplace=False)
guests_df = guests_df.rename({'index': 'guest_id'}, axis=1)
guests_df.to_csv('guests_table.csv')
# print(guests_df)

print(table_df)

# split up column 4

# mk: split into database tables:
#   - room_table
#   - guest_table 🗸
#   - booking_table
#   - guest_contact_details_table
