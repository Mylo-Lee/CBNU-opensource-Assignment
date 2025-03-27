def add_5std(stdstat): #학생정보를 입력받을때 외부함수에서 다른 외부함수를 호출 가능,순서도 상관 X
        for i in range(5):#초기 학생정보 입력은 5명 입력하는걸로 fix
            print(f"{i+1}번째 학생의 정보를 입력하세요.")#배열의 길이를 이용하여 학생의 순서를 나타냄
            stdstats = add_students() 
            stdstats = totavg(stdstats) 
            stdstats.append(grade(stdstats[6])) 
            stdstat.append(stdstats) 
        return stdstat

def add_students(): 
    stdnum = input("학번 :")
    stdname = input("이름 :")
    engscore = int(input("영어 :")) 
    Clengscore = int(input("C언어 :"))
    Pyscore = int(input("파이썬 :"))

    return [stdnum, stdname, engscore, Clengscore, Pyscore] 

def totavg(stdstat):
    total = stdstat[2] + stdstat[3] + stdstat[4]
    avg = total / 3 
    stdstat.append(total) 
    stdstat.append(avg)
    return stdstat

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def findstd(stdnum):
    fndstdnum = input("학번을 입력하세요 : ")
    for i in range(len(stdnum)):
        if stdnum[i][0] == fndstdnum:
            return print(f"{stdnum[i][0]}  {stdnum[i][1]}\t{stdnum[i][2]}\t{stdnum[i][3]}\t{stdnum[i][4]}\t{stdnum[i][5]}\t{stdnum[i][6]:.2f}\t{stdnum[i][7]}")
    return print("해당 학생이 없습니다.")
        
def delstd(stdnum):
    delstdnum = input("학번을 입력하세요 : ")
    for i in range(len(stdnum)):
        if stdnum[i][0] == delstdnum:
            return stdnum.pop(i)
    return print("해당 학생이 없습니다.")
        
def cntstd(stdnum):
      count = 0

      for i in range(len(stdnum)):
          if stdnum[i][6] >= 80:
              count += 1
      return count

def addstd(stdnum):
    print(f"{len(stdnum)+1}번째 학생의 정보를 입력하세요.")
    student = add_students()
    student = totavg(student)
    student.append(grade(student[6]))
    return stdnum.append(student)

def outputstd(stdnum):
    stdnum = sortstd(stdnum)
    print("\t\t\t\t성적관리 프로그램\n")
    print("========================================================================\n")
    print("학번\t\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\n")
    print("========================================================================\n")
    for i in range(len(stdnum)):
        print(f"{stdnum[i][0]} \t\t {stdnum[i][1]}\t{stdnum[i][2]}\t{stdnum[i][3]}\t{stdnum[i][4]}\t{stdnum[i][5]}\t{stdnum[i][6]:.2f}\t{stdnum[i][7]}\n")
    print(f"80점 이상 학생 수 : {cntstd(stdnum)}명")

def sortstd(stdstat):
    return sorted(stdstat, key=lambda x: x[5], reverse=True)

students = []
i = 0

while i != 9:
    print("------------------")
    print("|1. 학생 정보 입력|")
    print("|2. 학생 정보 검색|")
    print("|3. 학생 정보 삭제|")
    print("|4. 학생 정보 출력|")
    print("|5. 학생 추가 입력|")
    print("|9. 종료          |")
    print("------------------")
    
    i = int(input("메뉴를 선택하세요 : "))
    
    if i == 1:
      add_5std(students)

    elif i == 2:
      findstd(students)

    elif i == 3:
      delstd(students)

    elif i == 4:
      outputstd(students)

    elif i == 5:
      addstd(students)

    elif i == 9:
        break
    else:
        print("잘못된 입력입니다.")
        continue

  

