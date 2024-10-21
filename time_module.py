from datetime import datetime,date


def get_time():
    now = datetime.now()

    current_time = now.strftime("%I:%M %p")
    return current_time



def get_date():
    return str(date.today())

