from common.utils import generate_random_student_data

if __name__ == '__main__':
    count = 100_000
    for student in generate_random_student_data(count):
        print(student)
