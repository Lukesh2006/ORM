# Ex02 Django ORM Web Application
# Date:26.11.24
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books
# ER DIAGRAM :
![ER diagram](https://github.com/user-attachments/assets/bca5e02b-9b4d-4271-99fd-3723a9fc1ab1)



# PROGRAM 
```
admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)

models.py

from django.db import models
from django.contrib import admin
class Employee (models.Model):
    eid=models.CharField(max_length=20,help_text="Employee.ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','email')
```
# OUTPUT

![Screenshot 2024-12-12 185612](https://github.com/user-attachments/assets/6017fb2b-aa76-4376-a34a-aca335d5c0cb)
![Screenshot 2024-12-12 185735](https://github.com/user-attachments/assets/3f5bb618-1bf0-4786-ad48-447d5fb91d2c)




Include the screenshot of your admin page.

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
