def add_students(): # 학생의 정보를 입력하는 함수, 매개변수를 동치시키지 않아서 오류가 발생했음.>fixed
    stdnum = input("학번 :")
    stdname = input("이름 :")
    engscore = int(input("영어 :")) #input을 받자마자 int로 바로 변환이 가능하다.
    Clengscore = int(input("C언어 :"))
    Pyscore = int(input("파이썬 :"))

    # engscore = int(engscore) 이렇게 따로 int로 변환하는 것은 불필요하다.
    # Clengscore = int(Clengscore)
    # Pyscore = int(Pyscore)

    return [stdnum, stdname, engscore, Clengscore, Pyscore] #이 함수에서 매개변수 stdstat을 사용했었으나 불필요하다. return으로 바로 배열을 반환시키면 되기 때문. 

def totavg(stdstat):#총점과 평균을 구하는 함수
    total = stdstat[2] + stdstat[3] + stdstat[4]
    avg = total / 3 #avg
    stdstat.append(total) #.append는 리스트에 한번에 한개의 요소만 추가할 수 있다.
    stdstat.append(avg)
    return stdstat

def grade(score):#학점을 구하는 함수
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

def sortstd(stdstat):#총점을 기준으로 내림차순 정렬하는 함수
    return sorted(stdstat, key=lambda x: x[5], reverse=True)# 바로 반환이 가능하므로 간결화가 가능하다.
   #return 어쩌구..
        
students = []

for i in range(5):
  print(f"{i+1}번째 학생의 정보를 입력하세요.")
  student = add_students() #student[0]~[4]까지 학생의 정보를 입력받는다. 함수를 수정할때 매개변수가 들어가 있어야 할 괄호 를 빼먹지 않아야 한다.
  student = totavg(student) #student[5],[6]에 총점, 평균을 추가한다. <<totavg 함수 내에서 students 배열을 재구성했으니 .append가 아닌 =을 쓰는게 맞다.
  student.append(grade(student[6])) #student[7]에 학점을 추가한다. [-1]은 가장 마지막 요소를 가리킨다. 2차원 배열에서는 list[-1]일 경우 마지막 행 을 의미한다. 즉, students의 가장 최근 수정된 행 을 의미한다
  students.append(student) #students 배열에 student를 추가한다. ****이 줄 없이 students에 직접적으로 위의 세줄을 적용시키면 데이터는 당연히 처음 데이터밖에 없다!
  
students = sortstd(students) #총점을 기준으로 내림차순 정렬한다.

print("/t/t/t/t성적관리 프로그램\n")
print("========================================================================\n")
print("학번\t\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\n")
print("========================================================================\n")
for i in range(5):
  print(f"{students[i][0]}  {students[i][1]}\t{students[i][2]}\t{students[i][3]}\t{students[i][4]}\t{students[i][5]}\t{students[i][6]:.2f}\t{students[i][7]}\n")
