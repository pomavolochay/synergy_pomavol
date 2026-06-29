"""Task 1: Collect and print basic pet information for a vet clinic form."""

pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
pet_name = input("Введите кличку питомца: ")

if 11 <= pet_age % 100 <= 14:
    suffix = "лет"
elif pet_age % 10 == 1:
    suffix = "год"
elif 2 <= pet_age % 10 <= 4:
    suffix = "года"
else:
    suffix = "лет"

print(f'Это {pet_type} по кличке "{pet_name}". Возраст: {pet_age} {suffix}.')
