class Person:
    def __init__(self, name, age, passport_id):
        self.name = name
        self.age = age
        self.__passport_id = passport_id

    @property
    def passport_id(self):
        return self.__passport_id

    def info(self):
        return f"ФИО: {self.name}, Возраст: {self.age}, Паспорт: {self.__passport_id}"


class Student(Person):
    def __init__(self, name, age, passport_id, student_id, group):
        super().__init__(name, age, passport_id)

        self.student_id = student_id
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        if 2 <= grade <= 5:
            self.grades.append(grade)
        else:
            print("Ошибка: Оценка должна быть от 2 до 5.")

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        base_info = super().info()
        avg_grade = self.get_average_grade()
        return (f"{base_info}\n"
                f"Роль: Студент\nID: {self.student_id}\nГруппа: {self.group}\n"
                f"Средний балл: {avg_grade:.2f}")


class Teacher(Person):
    def __init__(self, name, age, passport_id, employee_id, department_name):
        super().__init__(name, age, passport_id)

        self.employee_id = employee_id
        self.department_name = department_name
        self.salary = 0

    def set_salary(self, amount):
        if amount > 0:
            self.salary = amount
        else:
            print("Зарплата не может быть отрицательной.")

    def info(self):
        base_info = super().info()
        return (f"{base_info}\n"
                f"Роль: Преподаватель\nID: {self.employee_id}\n"
                f"Кафедра: {self.department_name}\nЗарплата: {self.salary} руб.")


class Department:
    def __init__(self, name, faculty_name):
        self.name = name
        self.faculty_name = faculty_name
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Преподаватель {teacher.name} закреплен за кафедрой {self.name}.")

    def add_student(self, student):
        self.students.append(student)
        print(f"Студент {student.name} из группы {student.group} добавлен на кафедру {self.name}.")

    def show_staff(self):
        print(f"Сотрудники кафедры {self.name} ({self.faculty_name})")
        for t in self.teachers:
            print(t.info())
            print("-" * 30)

    def show_students(self):
        print(f"Студенты кафедры {self.name}")
        for s in self.students:
            print(s.info())
            print("-" * 30)


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def show_structure(self):
        print(f"\n=== Структура факультета: {self.name} ===")
        for dept in self.departments:
            print(f"Кафедра: {dept.name}")

if __name__ == "__main__":
    fit_faculty = Faculty("Факультет Информационных Технологий")

    cs_dept = Department("Кафедра Программной Инженерии", fit_faculty.name)
    is_dept = Department("Кафедра Информационных Систем", fit_faculty.name)

    fit_faculty.add_department(cs_dept)
    fit_faculty.add_department(is_dept)

    fit_faculty.show_structure()

    teacher1 = Teacher("Иванов И.И.", 45, "1234567890", "T-001", cs_dept.name)
    teacher1.set_salary(85000)

    teacher2 = Teacher("Петрова А.С.", 38, "0987654321", "T-002", is_dept.name)
    teacher2.set_salary(78000)

    student1 = Student("Бирюков Н.А.", 20, "1122334455", "01", "бИЦ-241")
    student1.add_grade(5)
    student1.add_grade(4)
    student1.add_grade(5)

    student2 = Student("Иванова А.А.", 20, "5566778899", "02", "бГСХ-232")
    student2.add_grade(4)
    student2.add_grade(3)

    cs_dept.add_teacher(teacher1)
    is_dept.add_teacher(teacher2)

    cs_dept.add_student(student1)
    is_dept.add_student(student2)

    cs_dept.show_staff()
    cs_dept.show_students()

    is_dept.show_staff()
    is_dept.show_students()