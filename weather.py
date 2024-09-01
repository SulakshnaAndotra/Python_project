import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass
from datetime import datetime

def convert_date(iso_string):
    dt = datetime.fromisoformat(iso_string)
    
    formatted_date = dt.strftime('%A %d %B %Y')
    
    return formatted_date

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    pass
    temp_in_celsius = round((float(temp_in_fahrenheit) - 32) * 5/9, 1) #round(x,1) is helping to round the decimal to 1
    return temp_in_celsius
    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    numeric_weather_data = []   #creating a new list to work on 
    for item in weather_data:
        try:
            numeric_weather_data.append(float(item))   #moving all the elements into the new list as a float
        except ValueError:
            print(F"Non-Numeric data has been found and skipedz: {item}")  # if not numeric data
    if not numeric_weather_data:                  # if the lis is empty 
        return None
    list_mean = float(sum(numeric_weather_data)/ len(numeric_weather_data))
    return list_mean
       
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    new_list=[]
    
    with open(csv_file) as data:
     reader = csv.reader(data)
     next(reader)   #skipping header in data
     
     for items in reader:
        if items:
         formatted_row = [items[0]] + [int(x) for x in items[1:]]    # read the first element as it is
         new_list.append(formatted_row)                              # added both lists as lists can be added

    return new_list
    

 

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    numeric_weather_data = []
    for item in weather_data:
        try:
            numeric_weather_data.append(float(item))
        except ValueError:
            print(F"Non-Numeric data has been found and skipedz: {item}")
    if not weather_data:
        return ()
    min_value = min(numeric_weather_data)
    min_index_last = numeric_weather_data[::-1].index(min_value)   #index of the last lowest element in reverse.
    min_index = len(numeric_weather_data)-1-min_index_last       # calculation to find the index of the last element 
    return (min_value, min_index)
    


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    numeric_weather_data = []
    for item in weather_data:
        try:
            numeric_weather_data.append(float(item))
        except ValueError:
            print(F"Non-Numeric data has been found and skipedz: {item}")
    if not weather_data:
        return ()
    max_value = max(numeric_weather_data)
    min_index_last = numeric_weather_data[::-1].index(max_value)
    min_index = len(numeric_weather_data)-1-min_index_last
    return (max_value, min_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
    weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
    A string containing the summary information.
    """
    list_length= len(weather_data)  #gives the length of the lisy 
    min_temp=[]
    max_temp=[]
    for row in weather_data:
        min_temp.append(convert_f_to_c(row[1]))   #converting into celcius and saving the min temp in this list 
        max_temp.append(convert_f_to_c(row[2])) # saving the max temp into a new list after converting into celcius

    min_overall_temp= min(min_temp)   # saves the lowest temp from the list
    max_overall_temp= max(max_temp) #saves the hight temp from the list

    index_min= min_temp.index(min(min_temp))  #gives the index of the min temp 
    date_min = convert_date(weather_data[index_min][0])  #with the help of index, date has been found 
    index_max = max_temp.index(max(max_temp))
    date_max = convert_date(weather_data[index_max][0])
    avg_min= round(calculate_mean(min_temp),1)   
    avg_max= round(calculate_mean(max_temp),1)

    return f"{list_length} Day Overview\n  The lowest temperature will be {min_overall_temp}{DEGREE_SYMBOL}, and will occur on {date_min}.\n  The highest temperature will be {max_overall_temp}{DEGREE_SYMBOL}, and will occur on {date_max}.\n  The average low this week is {avg_min}{DEGREE_SYMBOL}.\n  The average high this week is {avg_max}{DEGREE_SYMBOL}.\n"



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary=""
    for row in weather_data:
        day_data= (row[0])
        min_temp= convert_f_to_c(float(row[1]))
        max_temp= convert_f_to_c(float(row[2]))
        summary += (f"---- {convert_date(day_data)} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n")
    return summary
    
