import math
student = [e for e in input().split()]
groups_count = int(input())
groups = math.ceil(len(student) / groups_count)

color_list = []
for i in range (0,groups):
    color = input()
    color_list += [color]* groups_count
student_color = [f for f in input().split()]
color_lists = []
for stu in student_color:
    index = student.index(stu)
    color_lists.append(color_list[index])

print(" ".join(color_lists))



