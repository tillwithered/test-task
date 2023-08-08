#Тест на позицию python разработчика 
Здесь находится описание и требования к тестовому заданию для претендентов на позицию Python/Django/etc Developer.

## Цель задания
Целью этого тестового задания является разработка простой панели администратора Django, целью которой является управление контентом для интернет-магазина и поддержка нескольких ролей.

## Описание домена
На следующем рисунке представлена схема классов, которую следует учитывать при разработке вашей админ-панели. Это минимальные требования к классам и полям, которые мы ожидаем от вас. Вы можете вносить свои собственные обновления и добавлять дополнительный функционал. Все поля изображений должны быть представлены в виде ссылок на изображения. Вы можете свободно использовать любую базу данных, которая кажется подходящей для вас и для проекта. 

![Class diagram](https://hb.bizmrg.com/kazanexpress/class_diagram.png)

## Requirements
### Shop admin
1. Navigate through the shops list.
2. Make a search by title.
3. Edit everything except shop id.
4. Upload image as shop pic. 

### Product admin
1. Navigate through product list.
2. Search by id or product title.
3. Edit everything except product id.
4. First image should be displayed as main image in both list view and product view.
5. Sort products in product list by number of orders and by price.
6. Filter list of products by active flag.
7. Filter by price range.
8. Attach product to one or more categories.

### Category admin
1. Navigate through categories list.
2. Search by product id, title and parent category.
3. Add one or more parent categories. 
4. Display all possible paths to chosen category. 

### Management
There should be at least two administrative roles for the following purposes:
1. Moderation for products. 
2. Moderation of all available pages. 

## Submission
Fork this repository, prepare your solution and make a pull request when you're done.
Don't forget to write docs :)

## Good luck!
