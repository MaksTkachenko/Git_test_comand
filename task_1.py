
def index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Спроба доступу до неіснуючого індексу
    except IndexError:
        print("Помилка: Неправильний індекс списку")
