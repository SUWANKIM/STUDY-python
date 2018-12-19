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