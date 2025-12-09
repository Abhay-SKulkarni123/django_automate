from django.core.management.base import BaseCommand
from dataentry.models import Student

# Add some data to database using custom command
class Command(BaseCommand):
    help = 'It will insert data to the database'

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no':1002, 'name':'Sachin', 'age':18},
            {'roll_no':1003, 'name':'Abhi', 'age':19},
            {'roll_no':1004, 'name':'Abhay', 'age':18},
            {'roll_no':1006, 'name':'Abhishek', 'age':28},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists'))
        self.stdout.write(self.style.SUCCESS('Data Inserted Successfullly'))