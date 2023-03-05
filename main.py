import pandas as pd


# data edit
hotel_data = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', delimiter=';')
hotel_data.columns = hotel_data.columns.str.lower().str.replace(' ', '_')

# data research
country_success_booking = hotel_data.query("is_canceled == 0")\
    .groupby('country', as_index=False)\
    .is_canceled.count()\
    .sort_values('is_canceled', ascending=False).head(5)

type_nights_mean = hotel_data.groupby('hotel', as_index=False)\
    .stays_total_nights\
    .mean().round(2)

booking_differ = len(hotel_data.query('assigned_room_type != reserved_room_type'))

month_success_booking = hotel_data\
    .groupby(['arrival_date_year'], as_index=False)\
    .arrival_date_month.agg(pd.Series.mode)

cancel_month = hotel_data\
    .query('hotel == "City Hotel"')\
    .groupby(['arrival_date_year', 'arrival_date_month'])\
    .is_canceled.sum()\
    .groupby(['arrival_date_year']).nlargest(1)

print(cancel_month)





