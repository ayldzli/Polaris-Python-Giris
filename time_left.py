import datetime

def main():
    exam_year = int(input("Enter the exam year: "))
    exam_month = int(input("Enter the exam month: "))
    exam_day = int(input("Enter the exam day: "))
    exam_hour = float(input("Enter the exam hour in HH.MM format: "))
    remainingTime(exam_year, exam_month, exam_day, exam_hour)

def remainingTime(year, month, day, hour):
    now = datetime.datetime.now()
    new_now = datetime.datetime(now.year , now.month, now.day, now.hour, now.minute, 0, 0,)
    hr = int(hour)
    mn = int((hour - hr)*100) + 1
    rem = datetime.datetime(year, month, day, hr, mn)
    rem_time = rem - now
    days, seconds = rem_time.days, rem_time.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    print(f"Remaining time: {days} days, {hours} hours, {minutes} minutes.")
    
main()

