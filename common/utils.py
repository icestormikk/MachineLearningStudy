import random
from typing import Any, Generator

import numpy as np

from numpy import ndarray, dtype


class Student:
    """
    Студент некоторой учебной организации
    """
    def __init__(self, name: str, age: int, email: str, average: float):
        self.student_id = id(self)
        self.name = name
        self.age = age
        self.email = email
        self.average = average

    def __str__(self):
        return f'id: {self.student_id}, name: {self.name}, age: {self.age}, email: {self.email}, average: {self.average}'


def generate_random_student_data(students_count: int) -> Generator[Student, Any, None] | None:
    """
    Создание случайного набора данных, представляющего из себя список студентов некоторой учебной организации
    :param students_count: Необходимое количество студентов
    :return: Объект класса Generator, позволяющий итерироваться по списку объектов класса Student
    """
    if students_count < 0:
        return None
    names = ['Pavel', 'Dasha', 'Petya', 'Vanya', 'Sasha', 'Viktoria', 'Jessica', 'Oleg']

    return (
        Student(random.choice(names), random.randint(18, 40), f'test{i}@test.com', random.uniform(1.0, 5.0))
        for i in range(students_count)
    )
