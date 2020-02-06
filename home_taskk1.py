time_in_sec = int(input(" Введите время в секундах: "))
minutes = time_in_sec // 60
hours = minutes // 60

print("%02d:%02d:%02d" % (hours, minutes % 60, time_in_sec % 60))

