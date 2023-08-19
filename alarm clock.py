from datetime import datetime

alarm_time = input('enter your time(hh:mm:ss)\n')
alarm_houre = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_second = alarm_time[6:8]
while True:
    now = datetime.now()
    if alarm_houre == now.strftime('%H'):
        if  alarm_min == now.strftime('%M'):
            if alarm_second == now.strftime('%S'):
                with open("C:/Users/bidmajnoon\Downloads/AAllliii.txt", "w") as alarm_file:
                    alarm_file.write("hi ali how are you ")
                break

