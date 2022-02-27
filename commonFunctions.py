#
from datetime import datetime
from pytz import common_timezones, country_timezones

#
def getAllTimezones():

    #
    all_timezones = []

    #
    for current_timezone in common_timezones:

        #
        all_timezones.append(current_timezone)

    #
    return all_timezones

#
def getCountry():

    #
    return "TODO"

#
def getCountryCodeOfTimezone(timezone):

    #
    timezones_list = country_timezones

    #
    timezone_index = -1

    #
    keys_from_timezones_list = list(timezones_list.keys())
    values_from_timezones_list = list(timezones_list.values())

    #
    for current_timezone_array in values_from_timezones_list:

        #
        if timezone in current_timezone_array:

            #
            timezone_index = values_from_timezones_list.index(current_timezone_array)

    #
    return keys_from_timezones_list[timezone_index]