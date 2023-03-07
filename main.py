import pandas as pd

# data edit
hotel_data = pd.read_csv('./bookings.csv', delimiter=';')
hotel_data.columns = hotel_data.columns.str.lower().str.replace(' ', '_')
hotel_data['total_kids'] = hotel_data.children + hotel_data.babies
hotel_data['has_kids'] = hotel_data.total_kids != 0


# data research
country_success_booking = hotel_data.query("is_canceled == 0") \
    .groupby('country', as_index=False) \
    .is_canceled.count() \
    .sort_values('is_canceled', ascending=False).head(5)

type_nights_mean = hotel_data.groupby('hotel', as_index=False) \
    .stays_total_nights \
    .mean().round(2)

booking_differ = len(hotel_data.query('assigned_room_type != reserved_room_type'))

month_success_booking = hotel_data \
    .groupby(['arrival_date_year'], as_index=False) \
    .arrival_date_month.agg(pd.Series.mode)

cancel_month = hotel_data \
    .query('hotel == "City Hotel"') \
    .groupby(['arrival_date_year', 'arrival_date_month']) \
    .is_canceled.sum() \
    .groupby(['arrival_date_year']).nlargest(1)

age_data = (hotel_data[['adults', 'children', 'babies']].mean()).nlargest(1)

hotel_type_kids = hotel_data \
    .groupby('hotel') \
    .total_kids.mean()

churn_rate = hotel_data.groupby("has_kids").is_canceled.value_counts(normalize=True)
has_kid_churn = round(churn_rate.loc[False, 1] * 100, 2)
no_kid_churn = round(churn_rate.loc[True, 1] * 100, 2)


# data representation

