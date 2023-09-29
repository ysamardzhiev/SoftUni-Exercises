hour_exam = int(input())
minutes_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

time_exam_in_min = (hour_exam * 60) + minutes_exam
time_arrival_in_min = (arrival_hour * 60) + arrival_minutes
thirty_min_early = time_exam_in_min - 30
diff_min = abs(time_arrival_in_min - time_exam_in_min)

if time_arrival_in_min > time_exam_in_min:
    print('Late')
    if diff_min >= 60:
        hours = diff_min // 60
        minutes = diff_min % 60
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif thirty_min_early <= time_arrival_in_min <= time_exam_in_min:
    print('On Time')
    if diff_min > 0:
        print(f"{diff_min} minutes before the start")
elif thirty_min_early > time_arrival_in_min:
    print('Early')
    if diff_min >= 60:
        hours = diff_min // 60
        minutes = diff_min % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")