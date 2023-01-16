import time
import pandas as pd
import numpy as np
import re
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    flag = 0
    while flag == 0:
        city = input('Would you like to see the data for Chicago, New York, Washington? \n').lower()
        MorD = input('Would you like to Filter data by month, day, both or not at all?\n').lower()
        if MorD == 'month':
            month = input('Which month January, Febuary, March, April, May or June?\n').lower()
            day = None
        elif MorD == 'day':
            day = input('Which day M, Tu, W, Th, F, Sa or Su ?\n').lower()
            month = None
        elif MorD == 'both':
            month = input('Which month January, Febuary, March, April, May or June?\n').lower()
            day = input('Which day M, Tu, W, Th, F, Sa or Su ?\n').lower()
        elif MorD == 'not':
            month = None
            day = None
        else:
            print('\nPlease enter correct answers!!!')
            continue
        
        try:
            check_city = re.match(r'chicago|new york|washington', city)
            check_MorD = re.match(r'month|day|both|not', MorD)
            check_month = re.match(r'january|febuary|march|april|may|june', month)
            check_day = re.match(r'm|tu|w|th|f|sa|su', day)
            if check_city == None or check_month == None or check_day == None or check_MorD == None :
                print('Please enter correct answers!!!')
                flag = 0
            else:
                flag = 1
        except:
            flag = 1
    


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
    if month == None:
        df = pd.read_csv(CITY_DATA[city])
    else:
        if month == 'january':
            month = 1
        elif month == 'febuary':
            month = 2
        elif month == 'march':
            month = 3
        elif month == 'april':
            month = 4
        elif month == 'may':
            month = 5
        elif month == 'june':
            month = 6
        dataF = pd.read_csv(CITY_DATA[city])
        dataF['Start Time'] = pd.to_datetime(dataF['Start Time'])
        df = dataF[dataF['Start Time'].dt.month == month]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    print('Most common month is : ', list(df['Start Time'].dt.month.mode())[0])


    # display the most common day of week
    print('Most common day of week is : ', list(df['Start Time'].dt.strftime('%A').mode())[0])


    # display the most common start hour
    print('Most common hour : ', list(df['Start Time'].dt.hour.mode())[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station is : ', list(df['Start Station'].mode())[0])

    # display most commonly used end station
    print('Most common end station is : ', list(df['End Station'].mode())[0])

    # display most frequent combination of start station and end station trip
    print('Popualr Trip is : ', list(('From ' + df['Start Station'] + ' To ' + df['End Station']).mode())[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total duration : ', df['Trip Duration'].sum())

    # display mean travel time
    print('Average Time : ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types : ', df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('Genders : ', df['Gender'].value_counts())
        print('Earliest year of birth : ', df['Birth Year'].min())
        print('Most recent year of birth : ', df['Birth Year'].max())
        print('Most common year of birth : ',list(df['Birth Year'].mode())[0])
    except:
           print("This data has not Gender and Birth year!!!") 

    # Display earliest, most recent, and most common year of birth
    check = input('Would you like to see 5 rows from data (yes or no): ')
    if check.lower() == 'yes':
        i = 0
        j = 5
        print(df[i:j])
        
        while True:
            new_check = input('Would you like to see next 5 rows (yes or no): ')
            if new_check.lower() == 'yes':
                i += 5
                j += 5
                print(df[i:j])
            else :
                break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
