def student_total_score(*scores, **student_data):
    total = 0
    for score in scores:
        total += score
    average_score = total / len(scores)
    print(f'Szanowny Pan {student_data['name']} {student_data['surname']}'
          f' ma średnia z ocen {average_score:.2f}')

student_total_score(4, 4.5, 5, 3.5, name='Kamil', surname='Santos')