## Тестовое задание 

Стек:
Django, DRF.База данных, PostgreSQL или SQLite
Допускается использование вспомогательных библиотек и расширений на усмотрение кандидата.


## Цель задания:
 
Спроектировать REST API онлайн выставка котят:
                                                                       	
## API должно иметь следующие методы:
- Получение списка пород
- Получение списка всех котят
- Получение списка котят определенной породы по фильтру.
- Получение подробной информации о котенке.
- Добавление информации о котенке
- Изменение информации о котенке
- Удаление информации о котенке
- JWT Авторизация пользователей

       
## Запуск приложения


1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ArtyomBatmanov/test_task_workmate
   ```

2. Перейдите в корневую папку и запустите контейнер

```bash
cd myproject
docker compose build
docker compose up
```

3. Информация об API

```
GET api/token/ - получение токена для авторизации
GET swagger/ - документация
GET api/breeds/ - получение информации о породах
GET api/kittens/<int:pk>/ - получить информацию о котёнке
PUT api/kittens/<int:pk>/ - обновить информацию о котёнке
DELETE api/kittens/<int:pk>/ - удалить котёнка
GET api/kittens/ - получить информацию о всех котятах
POST api/kittens/ - создать нового котёнка
GET kittens/?breed=<breed_id>/ - получить информацию о котёнке определённой породы
```
Неавторизованный пользователь не может получить данные о котятах

4. Запуск тестов

Перейдите в корневую папку проект и выполните команду
```bash
pytest
```
