from collections import OrderedDict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
damages_float = []

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# ordered dictionary placeholders
full_list = OrderedDict()
date_list = OrderedDict()
winds_list = OrderedDict()
damages_list = OrderedDict()




## MISC FUNCTIONS ##
    #Convert strings in damages to float
def string_to_float(string_list):
    arr = []
    for i in string_list:
        if (i != "Damages not recorded"):
            if (i[-1] == "M"):
                arr.append(float(i[:-1]) * 10 ** 6)
            elif (i[-1] == "B"):
                arr.append(float(i[:-1]) * 10 ** 9)
        else:
            arr.append(0)
    return arr

damages_float = string_to_float(damages)
# print(damages_float)




## DICTIONARY CREATION FUNCTIONS ##
    #Create main dictionary that houses all stats
def main_dictionary(name, month, year, max_winds, areas, damage, death):
    for i in range(len(name)):
        full_list[name[i]] = OrderedDict([("Month", month[i]),("Year", year[i]),("Maximum winds", max_winds[i]),("Areas affected", areas[i]),("Damages", damage[i]),("Deaths", death[i])])
    return full_list


    #Create function for hurricane dates
def list_of_dates(name, month, year):
    for i in range(len(name)):
        date_list[name[i]] = OrderedDict([("Month", month[i]),("Year" , year[i])])
    return full_list

def list_of_stats(name, list, stat, string):
    for i in range(len(name)):
        list[name[i]] = OrderedDict([(string, stat[i])])
    return list


    #Execute functions above
main_dictionary(names, months,years, max_sustained_winds, areas_affected, damages, deaths)
list_of_dates(names, months, years)
list_of_stats(names, winds_list, max_sustained_winds, "Maximum Winds")
list_of_stats(names, damages_list, damages_float, "Damages in USD")


# print(full_list)
# print(date_list)
# print(winds_list)
# print(damages_list)




## SORT HURRICANES ##
winds_list_sort = OrderedDict(sorted(winds_list.items(), key=lambda x : x[1], reverse=True))
damages_list_sort = OrderedDict(sorted(damages_list.items(), key=lambda x : x[1], reverse=True))

# print(winds_list_sort)
# print(damages_list_sort)

## LIST MILESTONE HURRICANES ##
    # Fund a specific hurricane and list dates for it
    # Will be used to print the earliest and latest hurricane on list
def date_hurricane(list,x):
    key = list.keys()[x]
    month = list.values()[x].values()[0]
    year = list.values()[x].values()[1]
    return [key, month, year]

def top_hurricane(list):
    key = list.keys()[0]
    value = list.values()[0].values()[0]
    return [key, value]

    # Store and execute the fuctions above
earliest_hurricane = date_hurricane(date_list,0)
latest_hurricane = date_hurricane(date_list,-1)
maximum_winds = top_hurricane(winds_list_sort)
maximum_damage = top_hurricane(damages_list_sort)







## PRINT FUNCTIONS ##
    #Print a list of dates
def print_dates(list,string):
    print("\n\n\n\n\n" + str(string) + "\n------------------------------------------------------------------")
    count = 40
    for key, value in list.items():
        while len(key) < count:
            key += " "
        print(str(key) + str(value.values()[0]) + ", " + str(value.values()[1]))
    print("------------------------------------------------------------------")

def print_stat(list,string):
    print("\n\n\n\n\n" + str(string) + "\n------------------------------------------------------------------")
    count = 40
    for key, value in list.items():
        while len(key) < count:
            key += " "
        print(str(key) + str(value.values()[0]))
    print("------------------------------------------------------------------")






### PRINT DATA TO CONSOLE ###
    #Print top hurricanes for each category
print("Earliest hurricane: " + str(earliest_hurricane[0]) + " - " + str(earliest_hurricane[2]) + ", " + str(earliest_hurricane[1]))
print("Latest hurricane  : " + str(latest_hurricane[0]) + " - " + str(latest_hurricane[2]) + ", " + str(latest_hurricane[1]))
print("Maximum winds     : " + str(maximum_winds[0]) + " - " + str(maximum_winds[1]))
print("Most damage       : " + str(maximum_damage[0] + " - " + str(maximum_damage[1])))

    #Print lists
print_dates(date_list, "DATES")
print_stat(winds_list_sort, "MAXIMUM WINDS")
print_stat(damages_list_sort, "DAMAGES IN USD (0 MEANS NOT RECORDED)")
