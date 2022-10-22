# Сайт, посвященный музыкальной группе Sabaton
На информационном сайте представлено несколько разделов - общая информация о группе, участники и т.д.

![image](https://user-images.githubusercontent.com/78861235/187300378-3ad36733-34e5-4d6b-8d77-b9dcec36fcdf.png)

## Запуск проекта

Для запуска проекта с тестовым сервером на http://localhost:8000 необходимо выполнить следующий набор команд (в примере командная строка Windows 10):
```
C:\...> git clone https://github.com/musicgroup/sabaton
C:\...> cd sabaton
C:\...\sabaton> python -m venv venv
C:\...\sabaton> venv\Scripts\activate
C:\...\sabaton> pip install -r requirments.txt
```
И сам запуск:

```
C:\...\sabaton> python manage.py runserver
```
