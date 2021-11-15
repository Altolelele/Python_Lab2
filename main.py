import argparse
from Validator import Validator

parser = argparse.ArgumentParser("")
parser.add_argument("-input", type=str, default="31.txt",
                    help="Путь к исходному файлу данных")
parser.add_argument("-output", type=str, default="result_31.txt",
                    help="Результат валидации данных")
pars = parser.parse_args()

data = Validator(pars.input)
valid_data = data.count_valid_data()
invalid_data = data.count_invalid_data()
lst_mistakes = data.count_invalid_arguments()
print("Статистика:")
print("Число валидных записей:", valid_data)
print("Общее число невалидных записей:", invalid_data)
print("Число невалидных записей по типу ошибки 'email': ", lst_mistakes[0])
print("Число невалидных записей по типу ошибки 'height': ", lst_mistakes[1])
print("Число невалидных записей по типу ошибки 'inn': ", lst_mistakes[2])
print("Число невалидных записей по типу ошибки 'passport_number': ", lst_mistakes[3])
print("Число невалидных записей по типу ошибки 'occupation': ", lst_mistakes[4])
print("Число невалидных записей по типу ошибки 'age': ", lst_mistakes[5])
print("Число невалидных записей по типу ошибки 'academic_degree': ", lst_mistakes[6])
print("Число невалидных записей по типу ошибки 'worldview': ", lst_mistakes[7])
print("Число невалидных записей по типу ошибки 'address': ", lst_mistakes[8])
