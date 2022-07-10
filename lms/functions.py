def date_time():
    """Returns current date and time as a string. Also combines the date and time to give unique file name"""
    from datetime import datetime
    date = datetime.now().strftime('%d-%m-%Y')
    time = datetime.now().strftime('%I:%M:%S %p')
    unique = datetime.now().strftime('%y%m%d%I%M%S')
    return date, time, unique

#Declaring as global variables
date, time, unique = date_time()
