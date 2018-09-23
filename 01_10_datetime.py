import datetime
# print(dir(datetime))
# print(help(datetime.date))

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)


mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)

print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))


launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 7, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 7, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

now = datetime.datetime.today()
print(now)
print(now.microsecond)

moon_landing = "7/20/1969"

moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)