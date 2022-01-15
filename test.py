from student import Student, Grade

s1 = Student(
            firstname = "Marco",
            lastname = "Canedoli",
            birthdate = "1984-09-08T00:00:00.000",
            grades = [Grade(subject = "Math", grade = 25), Grade(subject = "Chemistry", grade = 27)]
            #grades = [{"Math": 25.0},{"Chemistry": 27.0}]
        )

print(s1.firstname);
print(s1.lastname)
age = s1.calculateAge()
print(age)
avg_grade = s1.calculateAvgGrade()
print(avg_grade)