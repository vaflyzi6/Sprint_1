def sum_m(time_string):
    sum_m = 0
    for full_time_unit in time_string.split(","):
        for time_unit in full_time_unit.split():
            if "m" in time_unit:
                sum_m += int(time_unit[0:-1])
            if "h" in time_unit:
                sum_m += int(time_unit[0:-1]) * 60
            if "s" in time_unit:
                sum_m += int(time_unit[0:-1]) / 60
    print(sum_m)


string = "1h 45m,360s,25m,30m 120s,2h 60s"
sum_m(string)
