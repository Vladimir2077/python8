def imp():
    with  open("phonebook.txt", "r" , encoding = "utf-8") as file:
        imp = input ("Введите фамилию для поиска: ")   
        for line in file:
            if imp in line:
                print(line)



def exp():
    f = open("phonebook.txt", "a" , encoding = "utf-8")
    imp = input ("Введите фамилию имя и телефон для записи: ")
    f.write(imp + "\n" + "\n")
    print(f"Новый контакт: {imp}")



print("Имеются две команды:\n"
          "1 Найти контакт\n"
          "2 Добавить контакт\n")
command = int(input("Выберите команду: "))

while command < 1 or command > 2:
        print("Неверная команда!")
        command = int(input("Введите действующую команду: "))

if command == 1:
        imp()
elif command == 2:
        exp()