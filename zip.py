midterms = [80, 91, 8]
finals = [98, 89, 53]
students = ['Rizal', 'Ilham', 'Aulia', 'Sabri']

final_grade = [max(pair) for pair in zip(midterms, finals)]
print(final_grade)

final_grade2 = {t[0]: (t[1], t[2]) for t in zip(students, midterms, finals)}

print(final_grade2)

scores = map(
    lambda pair: max(pair), zip(midterms, finals)
)

print(list(scores))