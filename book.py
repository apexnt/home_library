from dataclasses import dataclass


@dataclass
class Book:
    title: str  # Наименование
    author: str  # Автор
    publisher: str  # Издательство
    series: str  # Серия
    year_pub: int  # Год издания
    isbn: str  # номер ISBN
    page_count: int  # Количество страниц
    type_cover: str  # Тип обложки
    circulation: int  # Тираж

