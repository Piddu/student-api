#classe student
import datetime
from uuid import UUID, uuid4
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from pydantic import BaseModel
from typing import Optional, List
import typing

class Grade(BaseModel):
    subject: str
    grade: float


class Student(BaseModel):
    id: Optional[UUID] = uuid4
    firstname: str
    lastname: str
    birthdate: str
    grades: Optional[List[Grade]]

    def calculateAge(self):
        now = datetime.datetime.now()
        birthdate_datetime = parse(self.birthdate)
        difference = relativedelta(now, birthdate_datetime)
        age = difference.years
        return age
    
    def calculateAvgGrade(self):
        grades_sum = 0
        avg_grade = float(0)
        for i in range(len(self.grades)):
            grades_sum = grades_sum + self.grades[i].grade
  
        if grades_sum > 0:
            avg_grade = grades_sum / len(self.grades)
            return avg_grade
        else:
            return avg_grade





    
