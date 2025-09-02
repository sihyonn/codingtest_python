# list comprehension
# [변수활용 for 변수 in 반복대상 if 조건]

my_list = [1, 2, 3, 4, 5]
new_list = [f"{i}번째" for i in my_list if i >3]
print(new_list)

products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [p for p in products if p.startswith('SIRO')]
recal2 = [p + 'SE' for p in products]
recall3 = [p.lower() for p in products ]
recall4 = [p + '(최신형)' for p in products if p.endswith('2022')]
print(recall4)