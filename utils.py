
from classes.exceptions import *


def moving_to_shop(product, amount, from_, to, shop, store):
    # Ищем нужное кол-во
    try:
        store.remove(product, amount)
        print(f'\nНужное количество есть в "{from_}"')
    except (StorageFull, NoRequiredQuantity, NotFound) as error:
        print(error)
        return ''

    # Доставляем куда угодно
    try:
        shop.add(product, amount)
        print(f'Курьер забрал {amount} "{product}" из "{from_}" и везет в "{to}"')
        print(f'Курьер доставил {amount} "{product}" в "{to}"')
    except (StorageFull, MaxUnique) as error:
        print(error)
        return ''


def moving_to_store(product, amount, from_, to, shop, store):
    # Ищем нужное кол-во
    try:
        shop.remove(product, amount)
        print(f'\nНужное количество есть в "{from_}"')
    except (StorageFull, NoRequiredQuantity, NotFound) as error:
        print(error)
        return ''

    # Доставляем куда угодно
    try:
        store.add(product, amount)
        print(f'Курьер забрал {amount} "{product}" из "{from_}" и везет в "{to}"')
        print(f'Курьер доставил {amount} "{product}" в "{to}"')
    except (StorageFull, MaxUnique) as error:
        print(error)
        return ''
