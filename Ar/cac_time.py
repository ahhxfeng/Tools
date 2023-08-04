#coding=utf-8

"""
some function about time 
"""
# from datetime import datetime, timedelta
from datetime import date

# block_timestamp = 1690768298

# pre_block_timestamp = 1690768181

# dt1 = datetime.fromtimestamp(block_timestamp)
# print("dt1:", dt1)
# dt2 = datetime.fromtimestamp(pre_block_timestamp)
# print("dt2:", dt2)

# diff = dt2 - dt1

# print(diff)
# print(diff.min)
# print(diff.seconds)

def add_time_file(file:str):
    """
    auto add the curent time ahead the 
    givne file name 
    
    """

    date_now = date.today().isoformat()
    new_file_name = date_now + "-" +  file

    return new_file_name

