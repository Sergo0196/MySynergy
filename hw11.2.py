import collections

years_mod = ""
pet_type_key = "Вид питомца"
pet_age_key = "Возраст питомца"
pet_owner_key = "Имя владельца"
pets = {1: {"Мухтар": {pet_type_key: "Собака", pet_age_key: 9, pet_owner_key: "Павел"}}}




def create():
    last = collections.deque(pets, maxlen=1)[
        0]  

    print('Введите данные птомца для создания записи:')
    pet_name = input('Введите кличку питомца: ')
    pet_type = input('Введите вид питомца: ')
    pet_age = int(input('Введите возраст питомца: '))
    pet_owner = input('Введите имя владельца питомца: ')

    pet_opt = {pet_type_key: pet_type, pet_age_key: pet_age, pet_owner_key: pet_owner}
    pet = {pet_name: pet_opt}
    pets[last + 1] = pet

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False  

def get_suffix(age):
    
    if age % 10 == 1 and age != 11:
        return ' год'
    elif 11 <= age % 100 <= 14:
        return ' лет'
    elif 2 <= age % 10 <= 4:
        return ' года' 
    else:
        return ' лет'
    

def pet_list():
    if len(pets) != 0:
        for k in pets.keys():  
            print(f'Карточка №{k}: {pets[k]}')
    else:
        print('База питомцев пуста')

def read():
    print('Библиотека записей:')
    print(list(pets.keys()))
    target_pet_id = int(input('Укажите номер записи, которую вы хотите просмотреть: '))
    pet = get_pet(target_pet_id)
    if not pet:  
        print(f'{target_pet_id} не существует в словаре с питомцами')
    else:
        pet_name = collections.deque(pet, maxlen=1)[0]  
        pet_opt = pet[pet_name]  
        pet_type = pet_opt[pet_type_key]
        pet_age = pet_opt[pet_age_key]
        suffix = get_suffix(pet_age)
        pet_owner = pet_opt[pet_owner_key]
        print(
            f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age}{suffix}. Имя владельца: {pet_owner}')  # ты уже, вроде использовал f-строку так что через неё, ей проще формировать)

def update():
    print('Выберите номер записи для изменения данных:')
    pet_list()
    pet_id = int(input('Введите номер записи для введения новых данных: '))
    pet = get_pet(pet_id)
    if not pet:
        print('Указанного номера записи не существует')
    else:
        old_pet_name = collections.deque(pet, maxlen=1)[0]  
        pet_opt = pet[old_pet_name]  
        par = input('Введите параметр, который вы хотите изменить (кличка/вид/возраст/имя владельца): ')
        if par.lower() == 'кличка':
            new_pet_name = input('Введите кличку питомца: ')
            pets[pet_id] = {new_pet_name: pet_opt}
            del pet[old_pet_name]
        elif par.lower() == 'вид':
            pet_type = input('Введите вид питомца: ')
            pet_opt[pet_type_key] = pet_type
        elif par.lower() == 'возраст':
            pet_age = int(input('Введите возраст питомца: '))
            pet_opt[pet_age_key] = pet_age
        elif par.lower() == 'имя владельца':
            pet_owner = input('Введите имя владельца питомца: ')
            pet_opt[pet_owner_key] = pet_owner

def delete():
    print("Библиотека записей")
    pet_list()
    pet_id = int(input("Введите номер записи, которую хотите удалить: "))
    pet = get_pet(pet_id)
    if not pet:
        print('Такой записи не существует')
        return
    print(f'Пдтвердите удаление записи №{pet_id}:')
    qwest = input('Введите да или нет: ')
    if qwest.lower() == 'да':
        del pets[pet_id]
    elif qwest.lower() == 'нет':
        print("Операция удаления отменена")
    else:
        print("Некорректный ввод")

    if len(pets) == 0:
        print('База клиники пуста, создайте запись')

print("Введите команду для взаимодействия с базой данных \n" \
      "1 - Создание новой записи;\n2 - Вывод информации о питомце;\n3 - Внесение изменений в карту питомца;\n" \
      "4 - Удаление карты питомца\n'stop'- Завершение работы с базой питомцев")

while True:
    command = input("Введите команду: ")
    if command == '1':
        create()
        continue
    elif command == '2':
        read()
        continue
    elif command == "3":
        update()
        continue
    elif command == '4':
        delete()
        continue
    elif command == 'stop':
        print('Работа с базой карт пациентов завершена')
        break
