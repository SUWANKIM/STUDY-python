print("태어난 년도를 입력하시오")
bornYear = int(input())

age = 2018 - bornYear + 1

if age <= 26 and age >=20:
    print("대학생")

elif age < 20 and age >= 17:
    print("고딩")