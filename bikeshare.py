import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Allowed input for city, month and day
citys = ['chicago', 'new york city', 'washington']              
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_input = False     # Variable to act in dependence if input is valid or not
    
    city = ''
    while not valid_input:
        try:
            city = input("Please choose a city (chicago, new york city, washington):").lower()
            if city in citys:
                valid_input = True
                print(f"The data will be filtered by City: {city}")
            else: print("Your input was invalid, please try again.")    # valid_input remain False
        except: print("Your input was invalid, please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = ''
    valid_input = False
    while not valid_input:
        try:
            month = input("If you want to filter the data by month, please choose the name of the month, or choose 'all' for no month-filter: ").lower()
            if month in months:
                valid_input = True
                print(f"The data will be filtered by Month: {month}")
            else: print("Your input was invalid, please try again.")
        except: print("Your input was invalid, please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = ''
    valid_input = False
    while not valid_input:
        try:
            day = input("If you want to filter the data by day, please choose a day of the week (Monday, Tuesday, ...), or choose 'all' for no day-filter: ").lower()
            if day in days:
                    valid_input = True
                    print(f"The data will be filtered by Day: {day}")
            else: print("Your input was invalid, please try again.")
        except: print("Your input was invalid, please try again.")
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print(f"The data will be filtered by: City: {city}, Month: {month}, Day: {day}")
    try:
        df = pd.read_csv(CITY_DATA[city])

        df['Start Time'] = pd.to_datetime(df['Start Time'])         # convert content of 'Start Time' to date time
        df['Month'] = df['Start Time'].dt.month_name()              # grab the name of the month of the (date time) 'Start Time'
        df['Day Of Week'] = df['Start Time'].dt.day_name()          # grab the name of the day of the week of the (date time) 'Start Time'

        if month != 'all':                                          # if month is 'all' - no filtering is needed
            df = df[df['Month']==month.title()]                     # filter data by choosen month

        if day != 'all':                                            # if day is 'all' - no filtering is needed
            df = df[df['Day Of Week']==day.title()]                 # filter data by choosen day
    except:
        print("Something went wrong with loading the data")

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # TO DO: display the most common month
        print(f"The most common month for bikesharing was: {df['Month'].mode()[0]}")        # take first entry of mode (value that appears most often)

        # TO DO: display the most common day of week
        print(f"The most common day for bikesharing was: {df['Day Of Week'].mode()[0]}")    # take first entry of mode (value that appears most often)

        # TO DO: display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour                                               # add column 'Hour' in order to calculate the most commen start hour
        print(f"The most common hour for starting bikesharing was: {df['Hour'].dropna().astype('int').mode()[0]} o'clock")  # don't use NaN values, the rest convert into int and then grab the first entry of mode (value that appears most often)

    except:
        print("Something went wrong with calculate the time statistics")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:
        # TO DO: display most commonly used start station
        print(f"The most common start station for bikesharing was: {df['Start Station'].mode()[0]}")    # take first entry of mode (value that appears most often)

        # TO DO: display most commonly used end station
        print(f"The most common end station for bikesharing was: {df['End Station'].mode()[0]}")        # take first entry of mode (value that appears most often)

        # TO DO: display most frequent combination of start station and end station trip
        df['Trip'] = df['Start Station'].add(' to ').add(df['End Station'])                             # add a column 'Trip' in which the values from Start Station and End Station are combined with 'to' 
        print(f"The most common trip for bikesharing was: {df['Trip'].mode()[0]}")                      # take first entry of mode (value that appears most often)

    except:
        print("Something went wrong with calculate the station statistics")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    try:
        # TO DO: display total travel time
        print(f"The total travel time was approximately: {int(df['Trip Duration'].sum()/60/60)} hours ({int(df['Trip Duration'].sum()/60)} minutes or {df['Trip Duration'].sum()} seconds)")

        # TO DO: display mean travel time
        print(f"The mean travel time was approximately: {int(df['Trip Duration'].mean()/60)} minutes ({round(float((df['Trip Duration'].mean()/60/60)),2)} hours or {df['Trip Duration'].mean()} seconds)")

    except:
        print("Something went wrong with calculate the trip duration statistics")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # TO DO: Display counts of user types
        print(f"The following counts of user types was registered:\n\n{df['User Type'].value_counts()}\n\n")    # count the values for each user type

        # TO DO: Display counts of gender
        if 'Gender' in df.columns:
            print(f"The following counts of gender was registered:\n\n{df['Gender'].value_counts()}\n\n")       # count the values for each gender type
        else: print("No Gender Information in the filtering")                                                   # give Feedback for washington/no Gender Data

        # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            print(f"The earliest year of birth was: {df['Birth Year'].min().astype('int')}")                    # no need of dropna() here
            print(f"The most recent year of birth was: {df['Birth Year'].max().astype('int')}")                 # no need of dropna() here
            print(f"The most common year of birth was: {df['Birth Year'].dropna().astype('int').mode()[0]}")    # use all data, that are not NaNs, convert them into int and grab the value that occur most 
        else: print("No Birth Year Information in the filtering")                                               # give Feedback for washington/no Gender Data

    except:
        print("Something went wrong with calculate the user statistics")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Display raw data if this is wanted"""

    try:
        whish_for_more = input(f"\nActual data set has {len(df)} rows of raw data.\nDo you want to see the first 5 rows of raw data? Please insert yes or no: ").lower()    # initial question if first rows of raw data is wanted
        if whish_for_more == 'yes':
            print(df.head())                                                                                                                                                # df.head() shows the first 5 rows
        else: return                                                                                                                                                        # leave function if no data shall be shown
        for i in range(5, len(df), 5):                                                                                                                                      # repeat the question if more data shall be shown (starts with row 6 and covers 5 rows every cycle) and stop if end of data is reached or used don't want to see more data
            whish_for_more = input(f"\nThere are {len(df) - i} more rows of raw data.\nDo you want to see 5 more rows of raw data? Please insert yes or no: ").lower()
            if whish_for_more == 'yes':
                    print(df[i:i+5])                                                                                                                                        # show next 5 rows, if it is whished
            else: break                                                                                                                                                     # leave, if no more data shall be shown
    except:
        print("Something went wrong with put out the raw_data")
    
            
        

'''
#print(get_filters())
city, month, day = get_filters()
print(load_data(city, month, day))
print(time_stats(load_data(city, month, day)))
print(station_stats(load_data(city, month, day)))
print(trip_duration_stats(load_data(city, month, day)))
print(user_stats(load_data(city, month, day)))
'''

def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        # in case of an exception give another try, but also the possibility to end the program, so no endless loop happens
        except:
            print("Something went wrong - please check your input and try again")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()