from collections import defaultdict, OrderedDict

# struktura do przewchowywania projektów
projects = OrderedDict()

def create_task_structure():
    return defaultdict(list)

def add_project(project_name):
    if project_name not in projects:
        projects[project_name] = create_task_structure()
    else:
        print('Project name already exists')

def add_task(project_name, task_name, status='to do'):
    if project_name in projects:
        projects[project_name][status].append(task_name)
    else:
        print('Project name does not exist')

def change_task_status(project_name, task_name, new_status):
    if project_name in projects:
        for status, tasks in projects[project_name].items():
            if task_name in tasks:
                tasks.remove(task_name)
                projects[project_name][new_status].append(task_name)
        print(f'Task {task_name} does not exist')
    else:
        print('Project name does not exist')

def display_tasks(project_name):
    if project_name in projects:
        print(f'Zadania w projekcie {project_name}')
        for status, tasks in projects[project_name].items():
            print(f'Status: {status}')
            for task in tasks:
                print(f'\t{task}')
    else:
        print(f'projekt {project_name} does not exist')

add_project('Altkom')
add_project('Kowalski')
add_task('Kowalski', 'review')
add_task('Kowalski', 'obiad', 'in progress')
add_task('Kowalski', 'analiza', 'in progress')
add_task('Altkom', 'python', 'in progress')
add_task('Altkom', 'C++')
display_tasks('Altkom')
display_tasks('Kowalski')

change_task_status('Kowalski', 'obiad', 'done')
change_task_status('Kowalski', 'python', 'in progress')
display_tasks('Kowalski')
display_tasks('Altkom')