import time #Imports the time module

#Finds the time and puts it in a format
def time_finder():
    theirTime = time.localtime(time.time())
    formatTime = time.strftime("%Y-%m-%d %H:%M:%S", theirTime)
    return formatTime