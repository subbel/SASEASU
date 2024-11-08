from meetings.models import *
import xlsxwriter
from django.shortcuts import get_object_or_404
list = Student.objects.all()
# FOR EVERY GBM 1 BY 1
# workbook = xlsxwriter.Workbook("Students.xlsx")
# worksheet3 = workbook.add_worksheet()
# worksheet3.write(0, 0, "Firstname")
# worksheet3.write(0, 1, "Lastname")
# worksheet3.write(0, 2, "Email")
# worksheet3.write(0, 3, "Major")
# worksheet3.write(0, 4, "Social 1")
# x =1
# for i in list:
#     if "Industry 2 F24" in i.events:
#         if i.major != "":
#             worksheet3.write(x, 0, i.firstname)
#             worksheet3.write(x, 1, i.lastname)
#             worksheet3.write(x, 2, i.email)
#             worksheet3.write(x, 3, i.major)
#             x+=1

# #
# workbook.close()
f = open("data.txt", "r")
car = f.readlines()
event = get_object_or_404(Event, title = "GBM 4 F24")
for i in car:
    email = i[:-1]
    student = get_object_or_404(Student, email = email)
    student.GBM +=1
    student.events += event.title + " , "
    event.attendance +=1
    student.save()
    event.save()
    print(email + " " + student.firstname)


f.close()

# exec(open("shellform.py").read())