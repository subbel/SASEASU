from meetings.models import *
import xlsxwriter
list = Student.objects.all()
# FOR EVERY GBM 1 BY 1
workbook = xlsxwriter.Workbook("Students.xlsx")
worksheet3 = workbook.add_worksheet()
worksheet3.write(0, 0, "Firstname")
worksheet3.write(0, 1, "Lastname")
worksheet3.write(0, 2, "Email")
worksheet3.write(0, 3, "Major")
worksheet3.write(0, 4, "Social 1")
x =1
for i in list:
    if "Social 1 F24" in i.events:
        if i.major != "":
            worksheet3.write(x, 0, i.firstname)
            worksheet3.write(x, 1, i.lastname)
            worksheet3.write(x, 2, i.email)
            worksheet3.write(x, 3, i.major)
            x+=1

#
workbook.close()

# exec(open("shellform.py").read())