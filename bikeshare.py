import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city_input = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        except (TypeError, ValueError):
            print('That\'s not a valid city name!\n')
        except KeyboardInterrupt:
            try:
                response = input('\nAre you trying to quit the program? (yes or no)? ').lower()
                if response == 'yes' or response == 'y':
                    print('\nOk. Bye-bye. Exiting the program....')
                    exit()
                elif response == 'no' or response == 'n':
                    print('\nTry entering the city name again. Chigaco, New York City, or Washington. ')
                else:
                    print('\nI don\'t understand your response. Try entering the City name again. ')
            except KeyboardInterrupt:
                print('\nI think your really want to quit the program. Exiting the program now...')
                exit()
        else:
            if city_input.lower() not in ['chicago', 'new york city', 'washington']:
                print('The city name has to be Chicago, New Yokr City, or Washington only!\n')
            else:
                city = CITY_DATA[city_input.lower()]
                print('We will analyze {} data, then!'.format(city_input.title()))
                print('\n')
                break


    while True:
        try:
            # getting user choice on how the dataframe is going to be filtered
            filter_choice = input('Would you like to filter the data by month, day, both, or none? \n').lower()
        except (TypeError, ValueError):
            print('That\'s not a valid choice!\n')
        except KeyboardInterrupt:
            print('Perhaps you want to exit the program, but I want you to answer your filter choise.\n')
        else:
            if filter_choice == 'month':
                # TO DO: get user input for month (january, february, ... , june)
                try:
                    month = input('Which month - January, February, March, April, May, or June? ').lower()
                except (TypeError, ValueError):
                    print('That is not a valid month name!\n')
                except KeyboardInterrupt:
                    try:
                        response = input('\nAre you trying to quit the program? (yes or no)? ').lower()
                        if response == 'yes' or response == 'y':
                            print('\nOk. Bye-bye. Exiting the program....')
                            exit()
                        elif response == 'no' or response == 'n':
                            print('\nLet\'t try asking your choices again.\n')
                        else:
                            print('\nI don\'t understand your response. Let\'t try asking your choices again.\n')
                    except KeyboardInterrupt:
                        print('\nI think you really want to quit the program. Exiting the program now...')
                        exit()
                else:
                    if month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                        print('Enter a month name (spelled out) January through June.\n')
                        pass
                    else:
                        day = 'all'
                        all_done = 'yes'
                        break


            elif filter_choice == 'day':
                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while True:
                    try:
                        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
                    except (TypeError, ValueError):
                        print('That is not an acceptable day of the week! Try again.\n')
                    except KeyboardInterrupt:
                        try:
                            response = input('\nAre you trying to quit the program? (yes or no)? ').lower()
                            if response == 'yes' or response == 'y':
                                print('\nOk. Bye-bye. Exiting the program....')
                                exit()
                            elif response == 'no' or response == 'n':
                                print('\nLet\'t try asking your choices again.\n')
                            else:
                                print('\nI don\'t understand your response. Let\'t try asking your choices again.\n')
                        except KeyboardInterrupt:
                            print('\nI think you really want to quit the program. Exiting the program now...')
                            exit()
                    else:
                        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                            print('Enter day of the week (e.g. Thursday) not an abbreviation, a random word, or a list.\n')
                            pass
                        else:
                            # all months are going to be included
                            month = 'all'
                            all_done = 'yes'
                            break


            elif filter_choice == 'both':
                # Both month and day need to be specified by the user
                while True:
                    try:
                        month = input('Which month - January, February, March, April, May, or June? ').lower()
                    except (TypeError, ValueError):
                        print('That is not a valid month name!\n')
                    except KeyboardInterrupt:
                        try:
                            response = input('\nAre you trying to quit the program? (yes or no)? ').lower()
                            if response == 'yes' or response == 'y':
                                print('\nOk. Bye-bye. Exiting the program....')
                                exit()
                            elif response == 'no' or response == 'n':
                                print('\nLet\'t try asking your choices again.\n')
                            else:
                                print('\nI don\'t understand your response. Let\'t try asking your choices again.\n')
                        except KeyboardInterrupt:
                            print('I think you really want to quit the program. Exiting the program now...')
                            exit()
                    else:
                        if month not in ['january', 'february', 'march', 'april', 'may', 'june']:
                            print('Name the month name January through June.\n')
                        else:
                            all_done = 'yes'
                            break
                while True:
                    try:
                        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
                    except (TypeError, ValueError):
                        print('That is not a valid month name!\n')
                    except KeyboardInterrupt:
                        try:
                            response = input('\nAre you trying to quit the program? (yes or no)? ').lower()
                            if response == 'yes' or response == 'y':
                                print('\nOk. Bye-bye. Exiting the program....')
                                exit()
                            elif response == 'no' or response == 'n':
                                print('\nLet\'t try asking your choices again.\n')
                            else:
                                print('\nI don\'t understand your response. Let\'t try asking your choices again.\n')
                        except KeyboardInterrupt:
                            print('I think you really want to quit the program. Exiting the program now...')
                            exit()
                    else:
                        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                            print('Spell out the day of week completely. (e.g. Thursday)\n')
                        else:
                            all_done = 'yes'
                            break


            elif filter_choice == 'none':
                # if no filter is applied, all months and days will be in the data
                month = 'all'
                day = 'all'
                all_done = 'yes'
                print('\n')
                break

            else:
                print('That\'s not a valid choice. Type month, day, both, or none.')
                all_done = 'no'

        if all_done == 'yes':
            break
        elif all_done == 'no':
            continue





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
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month (from 1 to 12)
    popular_month = df['month'].value_counts().idxmax()
    pop_month_count = max(df['month'].value_counts())
    print('Most common month is {} with the count of {}.'.format(popular_month, pop_month_count))



    # TO DO: display the most common day of week

    # extract day of the week from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most common day of the week (from Monday to Sunday)
    popular_day_of_week = df['day_of_week'].value_counts().idxmax()
    pop_day_count = max(df['day_of_week'].value_counts())
    print('Most frequent start day of the week is {} with the count of {}.'.format(popular_day_of_week, pop_day_count))

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()
    pop_hour_count = max(df['hour'].value_counts())
    print('Most frequent start hour is {} with {} starts.'.format(popular_hour, pop_hour_count))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station and the number of time used
    popular_start_station = df['Start Station'].value_counts().idxmax()
    pop_start_count = max(df['Start Station'].value_counts())
    print('Most popular start station is {} with a count of {}.'.format(popular_start_station, pop_start_count))

    # TO DO: display most commonly used end station and the number of times used
    popular_end_station = df['End Station'].value_counts().idxmax()
    pop_end_count = max(df['End Station'].value_counts())
    print('Most popular end station is {} with a count of {}.'.format(popular_end_station, pop_end_count))

    # TO DO: display most frequent combination of start station and end station trip and the count of the trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep = ' and ')
    popular_trip = df['trip'].value_counts().idxmax()
    pop_trip_count = max(df['trip'].value_counts())
    print('Most popular trip is between {} with a count of {} trips.'.format(popular_trip, pop_trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = pd.to_timedelta(df['Trip Duration'].sum(), unit = 's')
    print('Total combined travel time is {} days, {} hours, {} minutes, and {} seconds.'.format(tot_travel_time.days, tot_travel_time.seconds//3600, tot_travel_time.seconds % 3600//60, tot_travel_time.seconds % 60))

    # TO DO: display mean travel time
    avg_travel_time = pd.to_timedelta(df['Trip Duration'].mean(), unit = 's')
    print('An average trip lasted {} minutes and {} seconds.'.format(avg_travel_time.seconds//60, avg_travel_time.seconds % 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print('\n')

    # TO DO: Display counts of gender
    try:
        gender_breakdown = df['Gender'].value_counts()
        print(gender_breakdown)
    except KeyError:
        print('This dataframe does not contain gender data, so no results are returned.')

    # TO DO: Display earliest, most recent, and most common year of birth
    # Also the count for the most common year will be included
    try:
        oldest_birth_year = min(df['Birth Year'])
        print('\nThe oldest birth year is {}'.format(int(oldest_birth_year)))
        youngest_birth_year = max(df['Birth Year'])
        print('The youngest birth year is {}'.format(int(youngest_birth_year)))
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        common_count = max(df['Birth Year'].value_counts())
        print('The most common birth year is {}, and the count is {}.'.format(int(common_birth_year), common_count))
    except KeyError:
        print('\nThis dataframe does not contain birth year data, so no results are returned.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def chunker(df, size):
    """
#    Takes a dataframe and returns the specified number of entries(size) at a time until
#    it reaches the end of the iterable.
#    """
    for i in range(0, len(df), size):
        yield df.iloc[i:i+size]



def main():
    """
    This is the main part of the program, and for each block displayed, user input will be asked.
    The user has a choice on whether to display the statistical summaries/restart the program.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        while True:
            #first choice for statistical data display
            try:
                want_time_stats = input('Do you want to see statistical data on bicycle usage time? (yes or no): ').lower()
                if want_time_stats == 'yes' or want_time_stats == 'y':
                    time_stats(df)
                    break
                elif want_time_stats == 'no' or want_time_stats == 'n':
                    print('\n')
                    break
                else:
                    print('Only yes/y or no/n are allowed as choice. \n')
            except:
                print('Not a valid choice.\n')

        while True:
            # Choice of stations statistics display
            try:
                want_station_stats = input('Do you want to see statistical data on trip stations used? (yes or no): ').lower()
                if want_station_stats == 'yes' or want_station_stats == 'y':
                    station_stats(df)
                    break
                elif want_station_stats == 'no' or want_station_stats == 'n':
                    print('\n')
                    break
                else:
                    print('Only yes/y or no/n are allowed as choice. \n')
            except:
                print('Not a valid choice.\n')

        while True:
            # Choice of trip duration stats display
            try:
                want_trip_stats = input('Do you want to see statistical data on trip duration? (yes or no): ').lower()
                if want_trip_stats == 'yes' or want_trip_stats == 'y':
                    trip_duration_stats(df)
                    break
                elif want_trip_stats == 'no' or want_trip_stats == 'n':
                    print('\n')
                    break
                else:
                    print('Only yes/y or no/n are allowed as choice. \n')
            except:
                print('Not a valid choice.\n')

        while True:
            # Choice of user data analysis display
            try:
                want_user_stats = input('Do you want to see statistical user data? (yes or no): ').lower()
                if want_user_stats == 'yes' or want_user_stats == 'y':
                    user_stats(df)
                    break
                elif want_user_stats == 'no' or want_user_stats == 'n':
                    print('\n')
                    break
                else:
                    print('Only yes/y or no/n are allowed as choice. \n')
            except:
                print('Not a valid choice.\n')


            # option to show raw data 5 rows at a time if the user wants

        while True:
            try:
                for display in chunker(df, 5):
                    show_raw_data = input('Do you want to see more raw data? (yes or no): ').lower()
                    if show_raw_data == 'yes' or show_raw_data == 'y':
                        print(display)
                    elif show_raw_data == 'no' or show_raw_data == 'n':
                        print('\n')
                        break
                    else:
                        print('I don\'t understand your answer. Try again')
            except KeyboardInterrupt:
                print('\nExiting program...')
                exit()
            except Exception as err:
                print('\nSomething went wrong. Exception {} occurred.\n'.format(err))
            break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
