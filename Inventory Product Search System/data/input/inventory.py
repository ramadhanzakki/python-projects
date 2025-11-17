INVENTORY = [
    {
        'id': 100 + (i * 10),
        'nama': f"Produk Item #{i + 1}",
        'rak': f"{chr(65 + (i // 100))}-{(i % 100):02d}" 
    }
    for i in range(1000)
]