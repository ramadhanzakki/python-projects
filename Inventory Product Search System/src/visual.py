class VisualInventory:
    def __init__(self, data: list[dict]):
        self.data = data

    def printInventory(self):
        print('\n=== 📊Current Inventory List ===')
        print(f"{'ID':<5} | {'Nama Produk':<20} | {'Rak':<5}")
        print('-' * 36)
        for p in self.data:
            print(f'{p['id']:<5} | {p['nama']:<20} | {p['rak']:<5}')
        print('-' * 36)

    def printProduct(self, product):
        if product:
            print('=== Product Detail ===')
            print(f' ID : {product['id']}')
            print(f' Nama : {product['nama']}')
            print(f' Rak : {product['rak']}')
            print('-----------------------')
        else:
            print('Product is not found')
