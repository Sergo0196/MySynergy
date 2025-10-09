import collections
# 
# pets = {1: 
#         {'Кличка питомца': None, "Характеристики": {"Вид питомца": None, "Возраст питомца": None, "Имя владельца": None
#         }
#     }
# }
pets = {}
pets_opt = {"Характеристики": {"Вид питомца": "str", "Возраст питомца": 0, "Имя владельца": "str"}}
pets_set = {'Кличка питомца': 'str', "Характеристики": pets_opt}
years_mod = ""
last = 0

def create():
    last = collections.deque(pets, maxlen=1)
    print('Введите данные птомца для создания записи:')
    name_pet = input('Введите кличку питомца: ')
    type_pet = input('Введите вид питомца: ')
    age_pet = int(input('Введите возраст питомца: '))
    get_suffix(age_pet)
    man_name = input('Введите имя владельца питомца: ')
    pets_opt = {"Вид питомца": type_pet, "Возраст питомца": years_mod, "Имя владельца": man_name}
    pets_set = {'Кличка питомца': name_pet, "Характеристики": pets_opt}
    pets[last + 1] = pets_set
    # if len(pets) == 0:
    #     last = collections.deque(pets.keys(), maxlen=1)[0]
    #     new_id = last + 1
    # else:
    #     new_id = 1
    #     pets[new_id] = {"Кличка питомца": name_pet, "Вид питомца": type_pet, "Возраст питомца": age_pet, "Имя владельца": man_name}

def get_suffix(age):
    global years_mod
    if age % 10 == 1 or age != 11:
        years_mod = str(age) + 'год'
    elif 11 <= age % 100 <= 14:
        years_mod = str(age) + 'лет'
    elif 2 <= age % 10 <= 4:
        years_mod = str(age) + 'года'
    else:
        years_mod = str(age) + 'лет'

def get_pet(ID):
        if ID in pets.keys():
            return pets[ID]
        else:
            print('Указанного номера записи не существует')

def pet_list():
    if len(pets) != 0:
        for k in pets:
            print(f'Карточка №{k}: {pets[k]}')
    else:
        print('База пациентов пуста')

def read():
    print('Библиотека записей:')
    print(pets.keys())
    id_p = int(input('Укажите номер записи, которую вы хотите просмотреть: '))
    id_p = get_pet(ID=id_p)
    print ("Это", pets[id_p]["Вид питомца"], 'по кличке', '"{}".'.format(pets[id_p]["Кличка питомца"]), 
           'Возраст питомца:', pets[id_p]["Возраст питомца"], '. Имя владельца: ', pets[id_p]["Имя владельца"])
    
def update():
    print('Выберите номер записи для изменения данных:')
    pet_list()
    id_p = int(input('Введите номер записи для введения новых данных: '))
    id_p = get_pet(ID=id_p)
    if id_p in pets.keys():
        par = input('Введите параметр, который вы хотите изменить (кличка/вид/возраст/имя владельца): ')
        if par == 'кличка':
            name_pet = input('Введите кличку питомца: ')
            pets[id_p] = {'Кличка питомца': name_pet}
        elif par == 'вид':
            type_pet = input('Введите вид питомца: ')
            pets[id_p]["Характеристики"] = {"Вид питомца": type_pet}
        elif par == 'возраст':
            age_pet = int(input('Введите возраст питомца: '))
            get_suffix(age_pet)
            pets[id_p]["Характеристики"] = {"Возраст питомца": years_mod}
        elif par == 'имя владельца':
            man_name = input('Введите имя владельца питомца: ')
            pets[id_p]["Характеристики"] = {"Имя владельца": man_name}
    else:
        print('Указанного номера записи не существует')

def delete():
    print("Библиотека записей")
    pet_list()
    id_p = int(input("Введите номер записи, которую хотите удалить: "))
    id_p = get_pet(ID=id_p)
    print(f'Пдтвердите удаление записи №{id_p}:')
    qwest = input('Введите да или нет: ')
    if qwest == 'да':
        pets.pop(id_p)
    elif qwest == 'нет':
        print("Операция удаления отменена")
    else:
        print("Некорректный ввод")

    if len(pets) == 0:
        print('База клиники пуста, создайте запись') 

print("Введите команду для взаимодействия с базой данных \n" \
"1 - Создание новой записи;\n2 - Вывод информации о пациенте;\n3 - Внесение изменений в карту пациента;\n" \
"4 - Удаление карты пациента\n'stop'- Завершение работы с базой пациентов")

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


     
