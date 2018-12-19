#List 는 시퀀스형 자료형, 여러 데이터들의 집합
#List의 특징 1. 인덱싱(주소값)을 가진다

colors = ['red', 'blue', 'green']
print(colors[0])

#List의 특징2, 슬라이싱 - List의 값들을 잘라서 쓰는 것
cities = ['강릉', '타슈켄트', '키갈리', '넬슨', '피닉스', '오클랜드', '히바']
print(cities[::2]) #0번째에서 두 칸 뒤의 데이터들만ㄴ 출력됨
print(cities[::-1]) #마지막 데이터부터 거꾸로 출력


#List의 덧셈 연산
color = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color + color2)
print(len(color)) #리스트의 길이
print(len(color+color2))
color[2] = 'Yellow' #리스트 내 특정 값의 데이터 변경 가능
print(color[2])
total_color = color+color2 #새로운 변수에 두 리스트를 더함
print(len(total_color))


#append 로 리스트에 데이터 추가하기
color.append('red') #color 리스트의 맨 뒤에 red가 추가된다
print(color)

#extend
color.extend(color2) #extend는 뒷 리스트를 앞 리스트에 붙임
print(color)

#insert
color.insert(0, 'suwan') #insert는 특정 주소에 데이터를 넣는 함수
print(color)

#del
del color[0] #0번째 값을 지워라
print(color)

#remove
color.remove('red') #'red' 라는 이름으로 데이터를 지움
print(color)


#파이썬은 동적할당 언어이므로 한 List에 여라가지 타입의 데이터를 넣을 수 있다.
a = ['color', 1, 0.2]
print(type(a[0]))
#파이썬의 리스트는 리스트의 주소값이 생성될 때 다양한 데이터 타입을 삽입 가능


#패킹과 언패킹
t = [1,2,3] #1,2,3을 변수 t에 패킹
a,b,c = t #t에 있는값을 변수 a,b,c에 언패킹

print(a)

#이차원 리스트
kor = [20,40,60]
eng = [69,38,56]
rus = [44,66,77]
midterm = [kor, eng, rus]
print(midterm)
print(midterm[0][2])