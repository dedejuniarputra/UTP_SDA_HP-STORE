#Definisi class item
class Item:
  #Menggunakan konstruktor __init__() yang mengambil tiga argumen yaitu nama, tipe, dan harga
    def __init__(self, name, tipe, price):
      #Menjelaskan bahwa kelas Item memiliki tiga atribut yaitu name, type, dan price
        self.name = name
        self.tipe = tipe
        self.price = price

#Mendefinisikan kelas HPStore menggunakan konstruktor init() yang akan menambahkan beberapa barang ke dalam list self.items
class HPStore:
  #Mendefinisikan list self.items yang berisi objek Item
    def __init__(self):
        self.items = [Item('Samsung', 'A10     ', 1000000), Item('Samsung', 'A15     ', 1500000), Item('Samsung', 'A25     ', 2000000), 
                      Item('Xiaomi ', 'Redmi 9 ', 1200000), Item('Xiaomi ','Redmi 10', 1800000), Item('Xiaomi ', 'Redmi 11', 2100000), 
                      Item('OPPO   ','A1      ', 1000000 ), Item('OPPO   ','A14     ', 1700000), Item('OPPO   ', 'Reno    ', 2200000)]

    #Metode show_items() akan menampilkan daftar barang yang tersedia dalam bentuk tabel.
    def show_items(self):
        print("==========================================")
        print("|       Selamat Datang di HP Store       |")
        print("==========================================")
        print("|        Daftar HP yang tersedia:        |")
        print("==========================================")
        print("|    Merk     |  Tipe     |  Harga       |")
        print("==========================================")

        for i, item in enumerate(self.items):
            print(f"| {i+1}. {item.name}  |  {item.tipe} |- Rp {item.price}  |")
        print("==========================================\n")
        
    #Metode buy() akan menanyakan username pengguna, menampilkan daftar barang yang tersedia, meminta pengguna untuk memilih barang dan jumlah yang ingin dibeli, menghitung total harga
    # dan kembalian, lalu menampilkan informasi tentang transaksi tersebut. 
    def buy(self, username):
        print(f"\nHallo, {username}! \n")
        self.show_items()
        
        total_price = 0
        selected_items = []
        total_item = 0
    
        def buy_items():
            nonlocal total_price, selected_items, total_item

            #Memilih item yang akan dibeli
            selected = input("Pilih nomor barang yang ingin dibeli (0 untuk selesai): ")
            if selected == '0':
                return
            
            try:
                selected_item = self.items[int(selected)-1]
            except:
                print("Mohon masukkan nomor barang yang valid!")
                return
                
            quantity = int(input("Jumlah barang yang ingin dibeli: "))
            
            total_price += selected_item.price * quantity
            selected_items.append((selected_item, quantity))
            
            print(f"Barang '{selected_item.name}' sebanyak {quantity} buah telah ditambahkan ke keranjang belanja.\n")
            total_item += quantity
            
            buy_items()

        buy_items()

        #Melakukan pembayaran
        print(f"\nTotal harga: Rp {total_price}")
        payment = int(input("Masukkan jumlah uang pembayaran: "))
        
        while payment < total_price:
            print("Maaf, uang pembayaran Anda kurang!")
            payment = int(input("Masukkan jumlah uang pembayaran: "))
            
        change = payment - total_price
        
        #Detail pembelian
        if change >= 0:
            print(f"\nTotal Item: {total_item}")
            print(f"\nTotal Belanja: Rp {total_price}")
            print(f"\nTunai: Rp {payment}")
            print(f"\nKembalian: Rp {change}")
            
        print("\nTerima kasih telah berbelanja di HP Store!")
        
        if input("Apakah Anda ingin membeli lagi? (y/t): ") == 'y':
            self.buy(username)
        else:
            print("Program selesai.")
            

#Mendefinisikan fungsi main() yang akan meminta username dan memulai transaksi belanja menggunakan kelas HPStore
def main():
    print("=== HP Store ===\n")
    username = input("Masukkan nama Anda: ")
    
    hp_store = HPStore()
    hp_store.buy(username)
    
# Mengatur agar fungsi main() akan dieksekusi jika program ini dijalankan langsung
if __name__ == '__main__':
    main()
