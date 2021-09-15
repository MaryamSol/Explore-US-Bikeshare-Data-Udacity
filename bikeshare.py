import time
import pandas as pd
import numpy as np
import calendar

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
    print("\nHello! Let's explore some US bikeshare data!")

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities =["chicago", "new york city", "washington"]
        city = input("\nWhich City would you like to explore?"
                     "\nPlease choose one of the following cities: Chicago, New York City or Washington."
                     "\nEnter your choice: ").lower()
        if city not in cities:
            print("\nYou didn't provide a valid city name."
                  "\nPlease, choose one of the provided cities.")
            continue
        else:
            break

    # get user input to filter the type (month, day or both)
    while True:
        filters = ["month", "day", "both", "all"]
        filter = input("\nHow would you like to filter?"
                       "\nChoose on of the following options: month, day, both, all."
                       "\nEnter your choice: ").lower()
        if filter not in filters:
            print ("\nYou didn't provide a valid filter"
                   "\nPlease, choose one of the provided filters.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june"]
    if filter == "both" or filter == "month":
        while True:
            month = input("\n Which month you would like to see?"
                          "\nChoose from the following months: January, February, March, April, May or June"
                          "\n Enter your choice: ").lower()
            if month not in months:
                print("\nYou didn't provide a valid month"
                      "\nPlease, choose one of the provided months.")
                continue
            else:
                break
    else:
        month = "all"



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    if filter == "both" or filter == "day":
        while True:
            day = input("\nWhich day you would like to see?"
                    "\nChoose from the following months: Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday or Friday"
                    "\n Enter your choice: ").lower()
            if day not in days:
                print("\nYou didn't provide a valid day"
                      "\nPlease choose on of the provided days.")
                continue
            else:
                break
    else:
        day = "all"



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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name()

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    print("\nThe most common months is ", calendar.month_name[common_month])

    # display the most common day of week
    common_day = df["day"].mode()[0]
    print("\nThe most common day of the week is ", common_day)

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("\nThe most common start hour is ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("\nThe most used start station is ", common_start_station)

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("\nThe most used end station is ", common_end_station)

    # display most frequent combination of start station and end station trip
    start_to_end = df["Start Station"] + " to " + df["End Station"]
    common_trip = start_to_end.mode()[0]
    print("\nThe most used trip of start station and end station is", common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time: ", total_travel_time, "seconds"
          "\n = ", total_travel_time/60, " mins" 
          "\n = ", total_travel_time/3600, " hours")

    # display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    print("\nThe average travel time: ", avg_travel_time, "seconds"
          "\n = ", avg_travel_time / 60, " mins"
          "\n = ", avg_travel_time / 3600, " hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df["User Type"].value_counts()
    print("\nCounts of user type: ",user_type_count )

    # Display counts of gender
    if "Gender" in df:
        gender_count = df["Gender"].value_counts()
        print("\nCounts of gender:  ", gender_count )
    else:
        print("\nNo data found for 'gender' in this city")


    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        birth_year = df["Birth Year"]
        earliest_year = int(birth_year.min())
        recent_year = int(birth_year.max())
        common_year = int(birth_year.mode()[0])
        print ("\nThe earliest year of birth is ", earliest_year,
               "\nThe most recent year of birth is ", recent_year,
               "\nThe most common year of birth is ", common_year)
    else:
        print("\nNo data found for 'Birth year' in this ciy")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Asks if user wants to see 5 lines of raw data
        Display that data if the answer is 'yes',
        Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
        Stop the program when the user says 'no' or there is no more raw data to display.
    """
    raw = input("\nWould you like to display 5 raw data? enter Yes if you agree.\n").lower()
    count = 0
    while True:
        if raw != "yes":
            break
        print(df.iloc[count: count+5])
        count +=5
        check = input("Do you want to see another 5 raw data? enter Yes if you agree: ").lower()
        if check != "yes":
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
