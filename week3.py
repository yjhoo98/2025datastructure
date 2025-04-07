import math
colors=['Red','Blue','Green','Black','Purple']
print(f'{colors[-1]}')
grades=[94,85,77,91]
sorted_grades=sorted(grades)
print(f'{sorted_grades}')
rsorted_grades=sorted(grades,reverse=True)
print(f'{rsorted_grades}')
courses=['Data Structure', 'Linear Algebra', 'Numerical Analysis', 'Object-oriented Programming']
apr_courses=list()
apr_courses.append(courses[0])
apr_courses.append(courses[3])
print(apr_courses)
napr_courses=courses[-3:-1]
print(napr_courses)
print(f'9^2={int(math.pow(9,2))}/10^2={int(math.pow(10,2))}')

