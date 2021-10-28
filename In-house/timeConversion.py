# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:29:55 2021

@author: DeleLinus
"""
def timeConversion(s):
    """
    converts time from 12-hour format to military (24-hour) time
    :param string s - a time in 12-hour format (i.e hh:mm:ssAM or i.e hh:mm:ssPM)

    Params:
        s (string) - the time in 24-hour format
    
    Returns:
        military_time (string): the time in 24-hour time
    
    Examples:
        >>> military_time = timeConversion("12:01:00PM")
        >>>print(military_time)
        12:01:00
        
        >>> military_time = timeConversion("12:01:00AM")
        >>>print(military_time)
        00:01:00
    
    """
    time_list = time.split(":")
    period = time_list[2][2:]
    hour = int(time_list[0])
    minute = time_list[1]
    sec = time_list[2][:2]
    
    if period=="AM" and int(hour)< 12:
        military_time = "0" + str(hour) + ":" + str(minute) + ":" + str(sec)
        
    elif period=="AM" and hour==12:
        military_time = "00" + ":" + str(minute) + ":" + str(sec)
        
    elif period=="PM" and hour== 12:
        military_time = str(12) + ":" + str(minute) + ":" + str(sec)
        
    else:
        military_time = str(hour+12) + ":" + str(minute) + ":" + str(sec)
        
    return military_time


time = input("Enter the time in 12-hour format: ")
military_time = timeConversion(time)
print(military_time)
