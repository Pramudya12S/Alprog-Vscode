usia = int(input("masukkan usia anda :"))
darah = int(input("masukkan tekanan darah anda :"))

if usia >=60 and darah >=140:
    print(" status kesehatan : tinggi")
elif usia >=60 and darah <= 140 : 
    print("status kesehatan : normal")
elif usia <60 and darah >130 : 
    print("status kesehatan :tinggi")
elif usia <60 and darah <=130 :
    print("status kesehatan :normal")
     