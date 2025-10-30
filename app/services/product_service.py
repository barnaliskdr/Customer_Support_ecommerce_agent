def get_all_products():
    # Example: Normally you'd fetch from a DB
    products = [
        {"id": 1, "name": "Laptop", "price": 75000},
        {"id": 2, "name": "Headphones", "price": 2500},
    ]
    return products


def get_product_by_id(product_id: int):
    # Example logic (in a real app, query DB here)
    product = {"id": product_id, "name": f"Product {product_id}", "price": 5000 + product_id * 100}
    return product