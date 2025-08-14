
from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+77711075028"),
    Smartphone("Samsung", "Galaxy S23", "+79222222222"),
    Smartphone("Xiaomi", "Mi 13", "+79333333333"),
    Smartphone("Google", "Pixel 8", "+79444444444")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")