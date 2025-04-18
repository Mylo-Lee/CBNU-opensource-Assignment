##########################
#프로그램명: 성적 관리 프로그램
#작성자: 2022041005 이호기
#작성일: 2025-04-13
#프로그램 설명:학생의 성적을 입력받고 추가,삭제,검색,출력 하는 프로그램
#시작시 1을 입력해 5명의 학생을 연달아 추가하는걸 추천.
###########################
class Student:# 학생 클래스스
    def __init__(self, stdnum, stdname, engscore, clengscore, pyscore):# 생성자
        self.stdnum = stdnum
        self.stdname = stdname
        self.engscore = engscore
        self.clengscore = clengscore
        self.pyscore = pyscore
        self.total = 0
        self.avg = 0.0
        self.grade = ''

    def calculate_totals(self):# 총점과 평균을 계산하는 메서드
        self.total = self.engscore + self.clengscore + self.pyscore
        self.avg = self.total / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):# 학점을 계산하는 메서드
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        else:
            return 'F'


class StudentManager:# 학생 관리 클래스
    def __init__(self):# 생성자
        self.students = []

    def add_student(self, student):# 학생을 추가하는 메서드
        student.calculate_totals()
        self.students.append(student)

    def add_5_students(self):# 5명의 학생 정보를 입력받는 메서드
        for i in range(5):
            print(f"{i + 1}번째 학생의 정보를 입력하세요.")
            student = self.input_student_info()
            self.add_student(student)

    def input_student_info(self):# 학생 정보를 입력받는 메서드
        stdnum = input("학번: ")
        stdname = input("이름: ")
        engscore = int(input("영어: "))
        clengscore = int(input("C언어: "))
        pyscore = int(input("파이썬: "))
        return Student(stdnum, stdname, engscore, clengscore, pyscore)

    def find_student(self):# 학생 정보를 검색하는 메서드
        stdnum = input("학번을 입력하세요: ")
        for student in self.students:
            if student.stdnum == stdnum:
                self.display_student(student)
                return
        print("해당 학생이 없습니다.")

    def delete_student(self):# 학생 정보를 삭제하는 메서드
        stdnum = input("삭제할 학생의 학번을 입력하세요: ")
        for student in self.students:
            if student.stdnum == stdnum:
                self.students.remove(student)
                print(f"학생 {stdnum}이 삭제되었습니다.")
                return
        print("해당 학생이 없습니다.")

    def display_students(self):# 학생 정보를 출력하는 메서드
        print("\t\t\t성적관리 프로그램")
        print("===============================================================")
        print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점")
        print("===============================================================")
        for student in sorted(self.students, key=lambda x: x.total, reverse=True):
            self.display_student(student)
        print(f"80점 이상 학생 수: {self.count_high_scores()}명")

    def display_student(self, student):# 학생 정보를 출력하는 메서드
        print(f"{student.stdnum}\t{student.stdname}\t{student.engscore}\t"
              f"{student.clengscore}\t{student.pyscore}\t{student.total}\t"
              f"{student.avg:.2f}\t{student.grade}")

    def count_high_scores(self):# 80점 이상 학생 수를 세는 메서드
        return sum(1 for student in self.students if student.avg >= 80)


def main():# 메인 함수
    manager = StudentManager()# 학생 관리 객체 생성
    while True:
        print("------------------")
        print("|1. 학생 정보 입력|")
        print("|2. 학생 정보 검색|")
        print("|3. 학생 정보 삭제|")
        print("|4. 학생 정보 출력|")
        print("|5. 학생 추가 입력|")
        print("|9. 종료          |")
        print("------------------")

        choice = int(input("메뉴를 선택하세요: "))

        if choice == 1:
            manager.add_5_students()
        elif choice == 2:
            manager.find_student()
        elif choice == 3:
            manager.delete_student()
        elif choice == 4:
            manager.display_students()
        elif choice == 5:
            student = manager.input_student_info()
            manager.add_student(student)
        elif choice == 9:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":# 메인 함수 실행
    main()