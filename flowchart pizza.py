#selamat datang di PizzaFortics
print("Selamat datang di PizzaFortics")
#kami menyediakan 2 menu best seller dan regular 
print("best seller : Super Supreme Chicken,Super Supreme")
print("Regular : Frankfurter BBQ, Meat Monsta")
#apa pesananmu?
pesananmu = input("apa pesananmu :").lower()
#best seller or regular
best_seller = {"super supreme", "super supreme chicken"}
regular = {"meat monsta", "frankfurter bbq"}
hargatotal = 0 
#harga pizza yang diberikan
harga_pizza = {"super supreme" : 50000, "super supreme chicken" : 45000,"meat monsta" : 35000, "frankfurter bbq" : 40000}
if pesananmu in best_seller : 
    print(f"anda memesan best seller : {harga_pizza[pesananmu]}")
    hargatotal += harga_pizza[pesananmu]
elif pesananmu in regular : 
    print(f"anda memesan regular : {harga_pizza[pesananmu]}")
    hargatotal += harga_pizza[pesananmu]
else : 
    print("pesanan anda tidak tersedia")
    exit()
#kami menyediakan untuk beberapa ukuran pizza kami.
size_pizza = input("choose your size : (small/medium/large)").lower()
if size_pizza == "small": 
    print("tambahan harga = 0")
elif size_pizza == "medium":
    print("tambahan harga = 0")
elif size_pizza == "large": 
    print("tambahan harga = Rp3000")
    hargatotal += 3000
else : 
    print("tidak tersedia")
    exit()
#kami menyediakan 2 crust untuk pizza kami. 
crust_pizza = input("choose your crust : (thin/thick)")
if crust_pizza == "thin": 
    print("tambahan harga = Rp0")
elif crust_pizza == "thick":
    print("tambahan harga = Rp1000")
    hargatotal += 1000
else : 
    print("tidak tersedia")
    exit()
#kami menyediakan beberapa tooping untuk pizza kami. 
print("mozarella, chili sauce, pepperoni, tomato sauce")
tooping_pizza = input("choose your tooping :")
#kami menyediakan untuk tambahan cheese di setiap menu 
tambahan_cheese = input("apakah anda ingin menambahkan cheese?")
if tambahan_cheese == "yes":
    hargatotal += 13000
    print("tambahan harga : Rp13000")
else:
    print("anda tidak menambahkan")
print(f"total harga yang didapatkan : {hargatotal}") 
print("selamat menikmati pizza kami")






