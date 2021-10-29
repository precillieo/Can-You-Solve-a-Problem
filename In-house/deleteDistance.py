# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:52:52 2021

@author: DeleLinus
"""
def deletionDistance(str1,str2):
    """
    finds the minimum number of characters you need to delete in the two strings in 
    order to get the same strings.
    
    Params:
        str1 (String) - the first string THAT DOES NOT CONTAIN A REPEATING CHARACTER'
        str2 (String) - the second string THAT DOES NOT CONTAIN A REPEATING CHARACTER''
    
    Returns:
        distance (int): the minimum number of characters you need to delete in the two strings in order to get the same strings.
    
    Examples:
        >>> distance = deletionDistance("dog","frog")
        >>>print(distance)
        3
        
        >>> distance = deletionDistance("some","some")
        >>>print(distance)
        0
        
        >>> distance = deletionDistance("some","thing")
        >>>print(distance)
        9
    
    """
    str_comb = str1 + str2
    str_list = [char for char in str_comb]
    str_list_len= len(str_list)
    str_set_len = len(set(str_list))
    distance = str_list_len-(2*(str_list_len - str_set_len))
    return  distance
	
	
 
	
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
gap = deletionDistance(str1,str2)
print (gap)
