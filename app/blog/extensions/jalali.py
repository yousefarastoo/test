from .utils import *

def jalali_convertor(time):
    days_of_week  = ["فروردین","اردیبهشت","خرداد","تبر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
    year = time.year
    month = time.month
    day = time.day
    res = Gregorian(f"{year}-{month}-{day}").persian_tuple()
    res =  f"{persian_number(res[2])} {days_of_week[res[1]]} {persian_number(res[0])} ساعت {persian_number(time.minute)} : {persian_number(time.hour)}"
    return res


def persian_number(number):
    number = f"{number}"
    english_array_number = ["0","1","2","3","4","5","6","7","8","9"]
    persian_array_number = ["۰","۱","۲","۳","۴","۵","۶","۷","۸","۹"]
    res = ""
    for num in number:
        for i,n in enumerate(english_array_number):
            if num == n:    
                res+= persian_array_number[i]
    if len(res)<2:
        res = f"۰{res}"
    return res