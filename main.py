class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def av_grade(self):
        sum_grades = 0
        count_grade = 0
        for i in self.grades.values():
            for k in i:
                sum_grades += k
                count_grade += 1
        try:
            av_grade = sum_grades / count_grade
        except:
            av_grade = sum_grades / 1
        return av_grade

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]   
            else:
                lecturer.grades[course] = [grade]    
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.av_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'Не студент'
        return self.av_grade() < other.av_grade()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grade(self):
        sum_grades = 0
        count_grade = 0
        for i in self.grades.values():
            for k in i:
                sum_grades += k
                count_grade += 1
        try:
            av_grade = sum_grades / count_grade
        except:
            av_grade = sum_grades / 1
        return av_grade
    
    def rate_hw(self, student, course, grade):
        print('Лекторы не могут выставлять оценки')

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade()}'
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Не лектор'
        return self.av_grade() < other.av_grade()

class Reviewer(Mentor):
    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student_1 = Student('Alex', 'Black', 'male')
student_1.courses_in_progress = ['Python', 'Java']
student_1.finished_courses = ['Fullstack']


student_2 = Student('Jeniffer', 'White', 'female')
student_2.courses_in_progress = ['Go', 'PHP', 'Python']
student_2.finished_courses = ['Linux']

lecturer_1 = Lecturer('Bob', 'Taller')
lecturer_1.courses_attached = ['Python', 'PHP']


lecturer_2 = Lecturer('Bill', 'Whatson')
lecturer_2.courses_attached = ['Go', 'Java', 'Python']

reviewer_1 = Reviewer('Dany', 'Adams')
reviewer_1.courses_attached = ['Go', 'Java', 'Python']

reviewer_2 = Reviewer('Mike', 'Jones')
reviewer_2.courses_attached = ['PHP', 'Python']


student_1.rate_lc(lecturer_1, 'Python', 5)
student_1.rate_lc(lecturer_2, 'Java', 7)
student_2.rate_lc(lecturer_1, 'PHP', 5)
student_1.rate_lc(lecturer_2, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Go', 8)
reviewer_2.rate_hw(student_2, 'PHP', 7)

print(str(student_1))
print(str(student_2))
print(str(lecturer_1))
print(str(lecturer_2))
print(str(reviewer_1))
print(str(reviewer_2))
print(str(student_2 < student_1))
print(str(lecturer_1 < lecturer_2))

def av_grade_students(list_students, course):
    sum_grades = 0
    count = 0
    for st in list_students:
        if course in st.grades.keys():
            for grade in st.grades[course]:
                sum_grades += grade
                count += 1
    try: 
        av_grade = sum_grades / count
    except:
        return f'У студентов нет оцценок на этом курсе'
    return av_grade

def av_grade_lecturers(list_lecturers, course):
    sum_grades = 0
    count = 0
    for lc in list_lecturers:

        if course in lc.grades.keys():
            for grade in lc.grades[course]:
                sum_grades += grade
                count += 1
    try: 
        av_grade = sum_grades / count
    except:
        return f'У лекторов нет оценок на этом курсе'
    return av_grade

print(av_grade_lecturers([lecturer_1, lecturer_2], 'Python'))
print(av_grade_lecturers([student_1, student_2], 'Python'))