print("------------------------------------")
print("----Selamat Datang di Pizza Hut-----")
print("----Silahkan Pilih Topping Anda-----")
print("------------Menu Topping------------")
print("-->        Frankfurter BBQ       <--")
print("-->          Meat Monsta         <--")
print("-->         Super Supreme        <--")
print("-->     Super Supreme Chicken    <--")
print("------------------------------------")
#pseudocode
#pelanggan memilih topping terlebih dahulu


#ToppingPizza
ToppingPizza = str(input("Masukkan Pilihan Topping Anda: "))
if ToppingPizza == "Frankfurter BBQ" :
    print("Harga Pizza Rp.40000 ")
    harga_tiopping_pizza = 40000
elif ToppingPizza == "Meat Monsta" :
    print("Harga Pizza Rp.45000 ")
    harga_topping_pizza = 45000
elif ToppingPizza == "Super Supreme" :
    print("Harga Pizza Rp.47000 ")
    harga_topping_pizza = 47000
elif ToppingPizza == "Super Supreme Chicken" :
    print("Harga Pizza Rp.50000 ")
    harga_topping_pizza = 50000
else :
    print("Maaf Topping Tidak Tersedia dalam daftar ")


#pilihan crust
print("------------------------------------")
print("-------------Menu Crust-------------")
print("-->             Pan              <--")
print("-->      StuffedCrust Cheese     <--")
print("-->      StuffedCrust Sausage    <--")
print("-->         Cheese Bites         <--")
print("-->          Crown Crust         <--")
print("------------------------------------")

#pelanggan memilih crust pizza
CrustPizza = str(input("Masukkan Pilihan Crust Anda: "))
if CrustPizza == "Pan" :
    print("Harga Crust Rp.0")
    harga_crust_pizza = 0
elif CrustPizza == "StuffedCrust Cheese" :
    print("Harga Crust Rp.10000")
    harga_crust_pizza = 10000
elif CrustPizza == "StuffedCrust Sausage " :
    print("Harga Crust Rp.15000")
    harga_crust_pizza = 15000
elif CrustPizza == "Cheese Bites" :
    print("Harga Crust Rp.20000")
    harga_crust_pizza = 20000
elif CrustPizza == "Crown Crust" :
    print("Harga Crust Rp.15000")
    harga_crust_pizza = 15000
else:
    print("Maaf Crust Tidak Tersedia dalam Daftar ")

#pilihan size
print("------------------------------------")
print("---------------Menu size---------------")
print("-->              Small          <--")
print("-->              Medium         <--")
print("-->              Large          <--")
print("------------------------------------")

#pelanggan memilih size pizza
SizePizza = str(input("Masukkan Pilihan Size pizza Anda: "))
if SizePizza == "Small" :
    print("Harga Small size Rp.49000")
    harga_small_pizza = 49000
elif SizePizza == "Medium" :
    print("Harga Medium Rp.59000")
    harga_medium_pizza = 59000
elif SizePizza == "Large" :
    print("Harga Large Rp.80000")
    harga_large_pizza = 80000
else:
    print("Maaf Size Tidak Tersedia dalam Daftar ")
