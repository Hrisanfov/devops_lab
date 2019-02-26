import schedule
import time
import psutil
import json
import datetime


class metric:
    "My custom class"
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.disk_usage('/')
    vram = psutil.virtual_memory()
    iops = psutil.disk_io_counters(perdisk=False)
    net = psutil.net_io_counters(pernic=True)


i = 0
txt = "txt"
f = open("conf.ini")
data = f.readlines()
d1 = data[1].split()
d2 = data[2].split()
extent = d1[2]
interval = int(d2[2])
outfile = "output."
output = outfile + extent
test = str(metric.cpu) + str(metric.ram) + str(metric.vram) + str(metric.iops) + str(metric.net)


def job():
    time = datetime.datetime.now()
    if extent == txt:
        with open(output, "a") as file:
            print("SNAPSHOT {}: TIMESTAMP{}:\n".format(i + 1, time), test, file=file)
    else:
        with open(output, 'a') as fl:
            print(json.dump(test, fl, ensure_ascii=False))


schedule.every(interval).minutes.do(job)
schedule.every().hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
