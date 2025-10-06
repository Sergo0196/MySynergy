pets = {}

name_pet = input("Кличка животного: ")
type_animal = input('Вид питомца: ').lower()
age_animal = int(input('Возраст питомца: '))
name_human = input("Имя владельца: ")
pets[name_pet] = {'Вид питомца': type_animal, 'Возраст питомца': age_animal, 'Имя владельца': name_human}
name_pet_k = list(pets.keys())
if age_animal % 10 == 1 and age_animal != 11:
    print(f"""Это {pets[name_pet]['Вид питомца']} по кличке "{name_pet_k[0]}". Возраст питомца: {pets[name_pet]['Возраст питомца']} год. Имя владельца: {pets[name_pet]['Имя владельца']}""")   
elif 11 <= age_animal % 100 <= 14:
    print(f"""Это {pets[name_pet]['Вид питомца']} по кличке "{name_pet_k[0]}". Возраст питомца: {pets[name_pet]['Возраст питомца']} лет. Имя владельца: {pets[name_pet]['Имя владельца']}""")
elif 2 <= age_animal % 10 <= 4:
    print(f"""Это {pets[name_pet]['Вид питомца']} по кличке "{name_pet_k[0]}". Возраст питомца: {pets[name_pet]['Возраст питомца']} года. Имя владельца: {pets[name_pet]['Имя владельца']}""")
else:
    print(f"""Это {pets[name_pet]['Вид питомца']} по кличке "{name_pet_k[0]}". Возраст питомца: {pets[name_pet]['Возраст питомца']} лет. Имя владельца: {pets[name_pet]['Имя владельца']}""")