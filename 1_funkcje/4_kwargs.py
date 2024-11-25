def new_employee_account_preparation(**user_data):
    for key, value in user_data.items():
        print(f'{key}: {value}')
    mail = user_data['name']+'.'+user_data['surname']+'@company.com'
    login = user_data['name'][:3]+user_data['surname'][:3]+'WRO'
    return mail, login

print(new_employee_account_preparation(name='Kamil', surname='Smith', level=3))
