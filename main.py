import time
from time import strftime
from random import choice
import csv


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

#——————————————————下面是主函数————————————————
key_number = input_key_number()
key_times = input_key_times()
key_clicks = input_key_clicks()
input('if the DUT is fixed ,please press ENTER ')
for i in range(10):
    x = str(10 - i)
    print('AutoMachine will be activated after '+ x +'s,please make sure the DUT is fixed')
    time.sleep(1)
cmd_list = get_cmdlist(key_number,key_clicks)
cmd_list_str=[str(i) for i in cmd_list]
print('cmd is running ,please waiting .............')

filename = 'ScriptLog' + strftime("%Y%m%d%H%M")
with open(filename + '.csv', 'a', newline='') as write_cmd:
    write_step = csv.writer(write_cmd)
    write_step.writerow(['cmd', 'time'])
    write_cmd.close()

for cmd in cmd_list:
    time.sleep(key_times)
    time_current = strftime("%Y%m%d-%H:%M:%S")
    print('Program is running , press ctrl + c to stop')
    log = [str(cmd),time_current]
    with open(filename + '.csv', 'a', newline='') as write_cmd:
        write_step = csv.writer(write_cmd)
        write_step = csv.writer(write_cmd)
        write_step.writerow(log)
        write_cmd.close()



#wirte_log(cmd_list_str)



