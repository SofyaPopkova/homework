# Классы
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ave_grades = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in self.courses_in_progress or course in self.finished_courses:
                if course in lecturer.ratings and 1 <= grade <= 10:
                    lecturer.ratings[course] += [grade]
                else:
                    lecturer.ratings[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        for val in self.grades.values():
            self.ave_grades = sum(val) / len(val)
        return self.ave_grades

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Не входит в список студентов')
            return
        else:
            return self.ave_grades > other.ave_grades

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.ave_grades}\n'\
               f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ratings = {}
        self.ave_ratings = []

    def add_ratings(self, rating, course):
        self.ratings[course].append(rating)

    def average_rating(self):
        for value in self.ratings:
            self.ave_ratings = sum(value) / len(value)
        return self.ave_ratings

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не входит в список преподавателей')
            return
        else:
            return self.ave_ratings > other.ave_ratings

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ave_ratings}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.review = {}

    def add_grades(self, grade, course):
        self.review[course].append(grade)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades and 1 <= grade <= 10:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Экземпляры классов


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java', 'Go']

worst_student = Student('Vasya', 'Pupkina', 'female')
worst_student.courses_in_progress += ['Python', 'Java']
worst_student.finished_courses += ['HTML', 'Go']

some_lecturer = Lecturer('Funny', 'Man')
best_student.rate_lecturer(some_lecturer, 'Java', 8)
worst_student.rate_lecturer(some_lecturer, 'Java', 6)
some_lecturer.ratings = {'Python': 10, 'Java': 8, 'Go': 6}
some_lecturer.courses_attached += ['Java']

other_lecturer = Lecturer('Cool', 'Person')
best_student.rate_lecturer(other_lecturer, 'HTML', 8)
worst_student.rate_lecturer(other_lecturer, 'HTML', 9)
other_lecturer.ratings = {'Python': 9, 'Go': 6}
other_lecturer.courses_attached += ['HTML']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(worst_student, 'Python', 4)

simple_mentor = Reviewer('Funny', 'Guy')
simple_mentor.courses_attached += ['Go']
simple_mentor.rate_hw(best_student, 'Go', 8)
simple_mentor.rate_hw(worst_student, 'Go', 5)


# Функции подсчета среднего значения:


def ave_course(students_list, course_name):
    for student in students_list:
        for key, value in student.grades.items():
            if key == course_name:
                if course_name in student.finished_courses or course_name in student.courses_in_progress:
                    ave_course_grade = sum(value) / len(students_list)
                    return ave_course_grade


def ave_classes(mentors_list, course_name):
    for mentor in mentors_list:
        for key, value in mentor.ratings.items():
            if key == course_name:
                if course_name in mentor.courses_attached:
                    ave_classes_grade = sum(value) / len(mentors_list)
                    return ave_classes_grade


print('Итоговая информация:')
print('------')
print(best_student)
print('------')
print(worst_student)
print('------')
print(some_lecturer)
print('------')
print(other_lecturer)
print('------')
print(cool_mentor)
print('------')
print(simple_mentor)
print('------')
print('Средние оценки:')
print(ave_course(students_list=[best_student, worst_student], course_name='Python'))
print(ave_classes(mentors_list=[some_lecturer, other_lecturer], course_name='Python'))
