from classes.exceptions import *
from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from utils import Move


def main():
    # Обрабатываем запрос
    try:
        request = Request(input('Запрос: ')).get_request()
        from_ = request.get('from')
        to = request.get('to')
        amount = request.get('amount')
        product = request.get('product')
    except (TypeError, ValueError, IndexError):
        print('Проверьте правильность запроса')
        return ''
    move = Move(product, amount, from_, to)

    if to == 'магазин':
        move.find_product_in(store)
        move.move_product_to(shop)
    elif to == 'склад':
        move.find_product_in(shop)
        move.move_product_to(store)
    else:
        print(f'В {to} никто доставлять не будет((')

    # Выводим кол-во товаров на складе и в магазине
    print(f'\nВ "{from_}" хранится:')
    for k, v in store.get_items.items():
        print(f' - {k}: {v}')
    print(f'Свободного места осталось: {store.get_free_space()}')
    print(f'\nВ "{to}" хранится:')
    for k, v in shop.get_items.items():
        print(f' - {k}: {v}')
    print(f'Свободного места осталось: {shop.get_free_space()}')


# Запускаем программу
products = {
    'печеньки': 10,
    'апельсины': 20,
    'сахар': 10,
    'картошка': 10,
    'сок': 10,
    'рыба': 10,
}

store = Store(items=products)
shop = Shop()

print(
    'Привет! Что и куда будем доставлять?\n'
    'Запрос должен выглядеть так: "Доставить <кол-во> <товар> из <откуда> в <куда>"'
    '\n'
)
while shop.get_free_space() > 0:
    main()
    print('-' * 30)
print('В магазине не осталось свободного места!')
