my_list = [5, 0, 9, 8 ,7 , 5, 3, 2, 1, 0, 5]
mpv = max(set(my_list), key=my_list.count)
print(mpv)