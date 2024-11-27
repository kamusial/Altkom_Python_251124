from collections import deque

high_prio = deque()
medium_prio = deque()
low_prio = deque()

def add_task(task, priority='medium'):
    if priority.lower()[0] == 'h':
        high_prio.append(task)
    elif priority.lower()[0] == 'm':
        medium_prio.append(task)
    elif priority.lower()[0] == 'l':
        low_prio.append(task)
    else:
        ValueError('Nieznany priorytet: {}'.format(priority))

def process_task():
    if high_prio:
        task = high_prio.popleft()
        print(f'Przetwarzam zadanie o wysokim prio: {task}')
    elif medium_prio:
        task = medium_prio.popleft()
        print(f'Przetwarzam zadanie o srednim prio: {task}')
    elif low_prio:
        task = low_prio.popleft()
        print(f'Przetwarzam zadanie o niskim prio: {task}')
    else:
        print('Brak zadan')

def display_queues():
    print(f'Wysoki prio: {list(high_prio)}')
    print(f'Średni prio: {list(medium_prio)}')
    print(f'Niski prio: {list(low_prio)}')

add_task('Zadanie 1', 'high')
add_task('Zadanie 2')
add_task('Zadanie 3')
add_task('Zadanie 4', 'low')
add_task('Zadanie 5', 'high')

display_queues()

process_task()
process_task()
process_task()
display_queues()