import csv, re


def read():
    """Читаем данные из файла"""
    with open("phonebook_raw.csv", encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def change(contacts_list):
    """Функция получает на вход список, где фамилия, имя и отчество могут находиться не в своих полях, а также номера телефонов
    записанные в различном формате, на выходе ФИО упорядочивается каждое по своему полю, а номера телефонов все приведены к шаблону
    +7(999)999-99-99
    """
    contacts_dict = {}
    key_contact = contacts_list.pop(0)
    # Проход по всем контактам
    for contact in contacts_list:
        # Создаем список с фамилией, именем и отчеством
        fio = [x.strip() for x in ' '.join(contact[:3]).split(' ', 2)]
        # Добавляем в список остальные данные
        new_contact = fio + contact[3:]
        # Создаем ключ на основе фамилии и имени
        key = ' '.join(fio[:2])
        # Создаем словарь с ключом фамилия + имя и пустыми значениями
        contacts_dict.setdefault(key, {i: None for i in key_contact})
        # Проходим по списку сотрудников, если данных еще нет, добавляем в словарь и заодно объединяем все данные по каждому сотреднику с разных записей в одну
        for index, value in enumerate(new_contact):
            if value and not contacts_dict[key][key_contact[index]]:
                contacts_dict[key][key_contact[index]] = value
            elif value and contacts_dict[key][key_contact[index]] != value:
                contacts_dict[key][key_contact[index]] += f';{value}'
        # Задаем шаблон для поиска всех телефонных номеров
        regex = r'(\+?\d{1})\s?\(*(\d{3})\)*(\s*|\-*)(\d{3})\-?(\d{2})\-?(\d{2}\s?)\(?((\w*\.)\s?(\d*)(\)?))?'
        # Задаем шаблон замены
        subst = r'+7(\2)\4-\5-\6\8\9'
        # Делаем подстановку
        contacts_dict[key]['phone'] = re.sub(regex, subst, contacts_dict[key]['phone'])
    # Создаем новый список с исправленной информацией
    new_contacts_list = [key_contact]
    for value in contacts_dict.values():
        new_contacts_list.append([value[i] for i in key_contact])
    return new_contacts_list


def write(new_contacts_list):
    """Записывает новые упорядоченные данные в файл"""
    with open("phonebook.csv", "w", encoding="utf-8") as filecsv:
        filewriter = csv.writer(filecsv, delimiter=",")
        filewriter.writerows(new_contacts_list)


contacts_list = read()
new_contact_list = change(contacts_list)
write(new_contact_list)

