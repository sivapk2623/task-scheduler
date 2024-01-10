import schedule
import time
import datetime

def job():
    print("I'm working on scheduler...")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))

def job2():
    print("ready to prepare for scheduler")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) 


schedule.every(5).seconds.do(job)
schedule.every(3).seconds.do(job2)



print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
while True:
    schedule.run_pending()
    time.sleep(1)