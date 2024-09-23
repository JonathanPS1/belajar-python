#-------------------------------------------------------------------------------
#
# NAMA   : Jonathan Putra Satria
# NIM    : 672021179
#
#-------------------------------------------------------------------------------
import datetime

# Soal 1
def decode(kalimat):
    kalimat_decode = ''
    try:
        if kalimat[0] == '-' or kalimat[0] == '+':
            raise ValueError("Tidak dapat memproses karakter + atau - di awal string")
    except IndexError:
        return "Error: String input tidak boleh kosong."

    for karakter in kalimat:
        if karakter == '-':
            kalimat_decode = kalimat_decode[:-1]
        elif karakter == '+':
            if kalimat_decode:
                kalimat_decode += kalimat_decode[-1]
        elif karakter in 'aiueo':
            kalimat_decode += str('aiueo'.index(karakter) + 1)
        elif karakter in '12345':
            kalimat_decode += 'aiueo'[int(karakter) - 1]
        else:
            kalimat_decode += karakter

    return kalimat_decode 

# Soal 2
class Product():
    def __init__(self, brand, supplier, harga):
        self.brand = brand
        self.supplier = supplier
        self.harga = harga

    def info(self):
        return  f"Brand: {self.brand}\nSupplier: {self.supplier}\nHarga: Rp.{self.harga}"

class FNB(Product):
    def __init__(self, brand, supplier, harga, expired_date):
        super().__init__(brand, supplier, harga)
        self.expired_date = expired_date
    
    def info(self):
        return super().info() + f"\nExpired Date: {self.expired_date}"

class HomeCare(Product):
    def __init__(self, brand, supplier, harga, type):
        super().__init__(brand, supplier, harga)
        self.type = type

    def info(self):
        return super().info() + f"\nType: {self.type}"

class Electronics(Product):
    def __init__(self, brand, supplier, harga, power_usage):
        super().__init__(brand, supplier, harga)
        self.power_usage = power_usage
    
    def info(self):
         return super().info() + f"\nPower Usage: {self.power_usage}"
    
def saveData(products, namafile):
    with open(namafile, 'w') as file:
        for product in products:
            if isinstance(product, FNB):
                file.write(f"{product.brand},{product.supplier},{product.harga},{product.expired_date}\n")
            elif isinstance(product, HomeCare):
                file.write(f"{product.brand},{product.supplier},{product.harga},{product.type}\n")
            elif isinstance(product, Electronics):
                file.write(f"{product.brand},{product.supplier},{product.harga},{product.power_usage}\n")

def loadData(namafile):
    products = []
    with open(namafile, 'r') as file:
        for line in file:
            data =  line.strip().split(',')
            if len(data) == 4:
                if '-' in data[3]:
                    products.append(FNB(data[0], data[1], int(data[2]), datetime.date.fromisoformat(data[3])))
                elif data[3].isdigit():
                    products.append(Electronics(data[0], data[1], int(data[2]), data[3]))
                else:
                    products.append(HomeCare(data[0], data[1], int(data[2]), data[3]))
    return products

if __name__ == "__main__":
    # Soal 1
    string = input("Masukkan Kalimat : ")
    hasil = decode(string)
    print("Hasil Decode : ", hasil + '\n')

    # Soal 2
    product1 = FNB('Fanta', 'Coca-Cola Company', 6000, datetime.date(2024, 1, 1))
    product2 = HomeCare('Head and Shoulders', 'Procter & Gamble', 15000, 'Shampoo')
    product3 = Electronics('ASUS TUF F15', 'ASUS', 13500000, '60w')

    products = [product1, product2, product3]
    saveData(products, "product.txt")

    loadedProducts = loadData("product.txt")
    for product in loadedProducts:
        print(product.info()+'\n')
