def productEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'manufacturer': item['manufacturer'],
        'price': item['price'],
        'amount': item['amount']
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
