
date = input().split("/")


Month = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
print(f'{Month[int(date[1])-1]} {date[0]} {date[2]}')

#12/1/2019
#31/12/2020