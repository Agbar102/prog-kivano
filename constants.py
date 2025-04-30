from category.models import Category, SubCategory
from category.utils import get_category

CATEGORY_DATA = [
    Category(title="Электроника"),
    Category(title="Компьютеры"),
    Category(title="Бытовая техника"),
    Category(title="Красота и здоровье"),
    Category(title="Детские товары"),
    Category(title="Спорт и отдых"),
    Category(title="Автотовары"),
    Category(title="Одежда"),
]


SUB_CATEGORY_DATA = [
    SubCategory(title='Мобильные телефоны', category=get_category('Электроника')),
    SubCategory(title='Планшеты и Букридеры', category=get_category('Электроника')),
    SubCategory(title='Ноутбуки и Компьютеры', category=get_category('Компьютеры')),
    SubCategory(title='Сетевое оборудование', category=get_category('Компьютеры')),
    SubCategory(title='Мелкая бытовая техника', category=get_category('Бытовая техника')),
    SubCategory(title='Крупная бытовая техника', category=get_category('Бытовая техника')),
    SubCategory(title='Товары для красоты', category=get_category('Красота и здоровье')),
    SubCategory(title='Парфюмерия', category=get_category('Красота и здоровье')),
    SubCategory(title='Часы', category=get_category('Одежда')),
    SubCategory(title='Аксессуары', category=get_category('Одежда')),
    SubCategory(title='Детский спорт', category=get_category('Детские товары')),
    SubCategory(title='Прогулки и путешествия', category=get_category('Детские товары')),
    SubCategory(title='Туризм', category=get_category('Спорт и отдых')),
    SubCategory(title='Лыжи и Сноуборд', category=get_category('Спорт и отдых')),
    SubCategory(title='Автомобильная акустика', category=get_category('Автотовары')),
    SubCategory(title='Автоэлектроника', category=get_category('Автотовары')),
]

