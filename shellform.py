from meetings.models import *
# import xlsxwriter
# list = Student.objects.all()
# workbook = xlsxwriter.Workbook("hello.xlsx")
# worksheet = workbook.add_worksheet()
# worksheet.write(0, 0, "Firstname")
# worksheet.write(0, 1, "Lastname")
# worksheet.write(0, 2, "Email")
# worksheet.write(0, 3, "Major")
# x =1
# for i in list:
#     if "GBM 2 Fall 2024" in i.events:
#         worksheet.write(x, 0, i.firstname)
#         worksheet.write(x, 1, i.lastname)
#         worksheet.write(x, 2, i.email)
#         worksheet.write(x, 3, i.major)
#         x+=1
# workbook.close()

list = Student.objects.all()
for i in list:
    if "GBM 2 Fall 2024" in i.events:
        i.events = i.events.replace("GBM 2 Fall 2024", "GBM 2 F24")
        i.save()
# exec(open("shellform.py").read())