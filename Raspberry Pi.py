import time
from random import choice
import time
time_date =time.strftime("%Y%m%d%H%M%S",time.localtime())

def input_key_number():
    key_numbers = input('please input the Key numbers that you want test : ')
    while True :
      if key_numbers.isdigit() and (int (key_numbers) in range(1,7)) :
         return int (key_numbers)
         break
      else:
          print('the date you input is out of range. the Maximum of key numbers is 6')
          key_numbers = input('please input the Key numbers that you want test : ')


def input_key_times():
    key_times = input('please input the duration of each click :')
    while True:
     if key_times.isdigit() and (int (key_times) in range(1, 5)) :
        return int (key_times)
        break
     else:
        print('the date you input is out of range. the Maximum of key numbers is 4 second')
        key_times = input('please input the duration of each click : ')


def input_key_clicks():
    key_clicks = input('please input the times of click keys: ')
    while True:
        if key_clicks.isdigit() and (int (key_clicks)>0) :
            return int(key_clicks)
            break
        else:
            print('the date you input is out of range. it must be digit')
            key_clicks = input('please input the duration of each click : ')


key_number = input_key_number()
key_times = input_key_times()
key_clicks = input_key_clicks()

