"""
Name: Kevin Wander
Email: kevin.wander30@myhunter.cuny.edu
Resources:  My notes
"""

def make_dictionary(data, kind = "min"):
    """
    key: the remote unit ID + turnstile unit number.
    dictionary will store the minimum entry(as an integer)
    the maximum entry number seen (as an integer),
    or the station name (as a string).
    Returns the resulting dictionary.

    Keyword arguments:
    kind -- kind of dictionary to be created:  min, max, station
    """
    new_dict = {}

    with open(data) as md:
        min = 0
        max = 0
        station_name = ""
        for line in md:
            splitup = line.split(",")

            if kind == "min":
                new_dict["min"] = min(data)
            elif kind == "max":
                new_dict["max"] = max(data)
            elif kind == "station":
                for item in data:
                    if "station" in item:
                        new_dict[item["station"]] = item["entry_number"]

    return new_dict
    

    #Placeholder-- replace with your code


def get_turnstiles(station_dict, stations = None):
    """
    If stations is None, returns the names of all the turnstiles stored as keys
    in the inputted dictionary.
    If non-null, returns the keys which have value from station in the inputed dictionary.
    Returns a list.

    Keyword arguments:
    stations -- None or list of station names.   
    """

    #Placeholder-- replace with your code
    lst = []
    return lst

def compute_ridership(min_dict,max_dict,turnstiles = None):
    """
    Takes as input two dictionaries and a list, possibly empty, of turnstiles.
    If no value is passed for turnstile, the default value of None is used
    (that is, the total ridership for every station in the dictionaries).
    Returns the ridership (the difference between the minimum and maximum values)
    across all turnstiles specified.

    Keyword arguments:
    turnstiles -- None or list of turnstile names    
    """

    #Placeholder-- replace with your code
    total = 0
    return total

def main():
    kind = "min"
    new_dict = {}
    min = 0
    max = 0
    station_name = ""
    with open("turnstile_220611.txt") as md:
        counter = 0
        for line in md:
            splitup = line.split(",")
            if counter == 1:
                min = 1337
            if kind == "min":
                new_dict["min"] = min(md)
            elif kind == "max":
                new_dict["max"] = max(md)
            elif kind == "station":
                for item in md:
                    if "station" in item:
                        new_dict[item["station"]] = item["entry_number"]


    """
    Opens a data file and computes ridership, using functions above.
    """
    """
    file_name = 'turnstile_220611.txt'
    #Store the file contents in data:
    with open(file_name,encoding='UTF-8') as file_d:
        lines = file_d.readlines()
    #Discard first line with headers:
    data = lines[1:]

    #Set up the three dictionaries:
    min_dict = make_dictionary(data, kind = "min")
    max_dict = make_dictionary(data, kind = "max")
    station_dict = make_dictionary(data, kind = "station")

    #Print out the station names, alphabetically, without duplicates:
    print(f'All stations: {sorted(list(set(station_dict.values())))}')

    #All the turnstiles from the data:
    print(f'All turnstiles: {get_turnstiles(station_dict)}')
    #Only those for Hunter & Roosevelt Island stations:
    print(get_turnstiles(station_dict, stations = ['68ST-HUNTER CO','ROOSEVELT ISLND']))

    #Checking the ridership for a single turnstile
    ridership = compute_ridership(min_dict,max_dict,turnstiles=["R051,02-00-00"])
    print(f'Ridership for turnstile, R051,02-00-00:  {ridership}.')

    #Checking the ridership for a station
    hunter_turns = get_turnstiles(station_dict, stations = ['68ST-HUNTER CO'])
    ridership = compute_ridership(min_dict,max_dict,turnstiles=hunter_turns)
    print(f'Ridership for Hunter College: {ridership}.')
    """

if __name__ == "__main__":
    main()
