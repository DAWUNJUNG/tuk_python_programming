# ==, != 연산
A = {'apple', 'banana', 'grape'}
B = {'apple', 'banana', 'grape', 'kiwi'}

if A == B:
    print('A와 B는 같습니다.')
else:
    print('A와 B는 같지 않습니다.')

# 합집합
C = A | B

# 교집합
C = A & B

# 차집합
C = A - B