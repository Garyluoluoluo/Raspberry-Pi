import time
from time import strftime
from random import choice
import csv
import RPi.GPIO as GPIO    



# 输入按键个数范围 1到6个按键
def input_key_number():
    key_numbers = input('please input the Key numbers that you want test : ')
    while True :
      if key_numbers.isdigit() and (int (key_numbers) in range(1,7)) :
         return int (key_numbers)
         break
      else:
          print('the date you input is out of range. the Maximum of key numbers is 6')
          key_numbers = input('please input the Key numbers that you want test : ')

#输入单次点按时间 时常1到4秒
def input_key_times():
    key_times = input('please input the duration of each click :')
    while True:
     if key_times.isdigit() and (int (key_times) in range(1, 5)) :
        return int (key_times)
        break
     else:
        print('the date you input is out of range. the Maximum of key numbers is 4 second')
        key_times = input('please input the duration of each click : ')

#输入点按次数至少1次
def input_key_clicks():
    key_clicks = input('please input the times of click keys: ')
    while True:
        if key_clicks.isdigit() and (int (key_clicks)>0) :
            return int(key_clicks)
            break
        else:
            print('the date you input is out of range. it must be digit')
            key_clicks = input('please input the duration of each click : ')

#生成指令列表
def get_cmdlist (key_number,key_clicks):
    scripts_cmd = []
    for i in range(key_clicks) :
        get_cmd = choice(range(key_number))+1
        scripts_cmd.append(get_cmd)
    return scripts_cmd

#打印执行日志
def wirte_log(cmd_list_str):
    filename = 'ScriptLog'+ strftime("%Y%m%d%H%M")
    print('writing Log,please waiting ')
    with open(filename+'.csv','w',newline='') as write_cmd:
        write_step = csv.writer(write_cmd)
        write_step.writerows(cmd_list_str)
    print('write Log successfully')

#init GPIO
def init_GPIO():
    GPIO.setwarnings(False)
    # BOARD编号方式，基于插座引脚编号    
    GPIO.setmode(GPIO.BOARD)    
    # 输出模式
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    #set to low 
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW) 
def key_mapping(cmd,out_status=''):
    if out_status is 'GPIO.HIGH'or 'GPIO.LOW':
        if cmd is 1 :
            GPIO.output(3,out_status)
        elif cmd is 2:
            GPIO.output(5,out_status)
        elif cmd is 3:
            GPIO.output(7,out_status)
        elif cmd is 4:
            GPIO.output(11,out_status)
        elif cmd is 5:
            GPIO.output(13,out_status)
        elif cmd is 6:
            GPIO.output(15,out_status)
        else:
            print('something wrong')
#——————————————————下面是主函数————————————————
key_number = input_key_number()
key_times = input_key_times()
key_clicks = input_key_clicks()
init_GPIO()
input('if the DUT is fixed ,please press ENTER ')
 
list_count = 0


for test_count in range(1,(key_number+1)):
    input('test the Key'+str(test_count)+'#,please check')
    key_mapping(test_count,GPIO.HIGH)
    time.sleep(1)
    key_mapping(test_count,GPIO.LOW)
print('AutoMachine will be activated after 10 s,please make sure the DUT is fixed')

for i in range(10):
    x = str(10 - i)
    print(x +'s')
    time.sleep(1)
cmd_list = get_cmdlist(key_number,key_clicks)
cmd_list_str=[str(i) for i in cmd_list]
print('cmd is running ,please waiting .............')
print('Program is running , press ctrl + c to stop')

filename = 'ScriptLog' + strftime("%Y%m%d%H%M")
with open(filename + '.csv', 'a', newline='') as write_cmd:
    write_step = csv.writer(write_cmd)
    write_step.writerow(['cmd', 'time'])
    write_cmd.close()

for cmd in cmd_list:
    list_count += 1
    time_current = strftime("%Y%m%d-%H:%M:%S")
    if cmd is 1:
        GPIO.output(3, GPIO.HIGH)
        time.sleep(key_times)
        GPIO.output(3, GPIO.LOW)
    elif cmd is 2:
        GPIO.output(5, GPIO.HIGH)
        time.sleep(key_times)
        GPIO.output(5, GPIO.LOW)
    elif cmd is 3:
        GPIO.output(7, GPIO.HIGH)
        time.sleep(key_times)
        GPIO.output(7, GPIO.LOW)
    elif cmd is 4:
        GPIO.output(11, GPIO.HIGH)
        time.sleep(key_times)
        GPIO.output(11, GPIO.LOW)
    elif cmd is 5:
        GPIO.output(13, GPIO.HIGH)
        time.sleep(key_times)
        GPIO.output(13, GPIO.LOW)
    elif cmd is 6:
        GPIO.output(15, GPIO.HIGH)
        time.sleep(key_times)
        GPIO.output(15, GPIO.LOW)
    else:
        print('something wrong')
        break
    time.sleep(0.2)
    log = [str(cmd),time_current] 
    with open(filename + '.csv', 'a', newline='') as write_cmd:
        write_step = csv.writer(write_cmd)
        write_step = csv.writer(write_cmd)
        write_step.writerow(log)
        write_cmd.close()

if list_count == len(cmd_list):
    print('Program run successfully')

#wirte_log(cmd_list_str)



