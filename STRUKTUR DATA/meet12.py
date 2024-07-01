# --------5+++++++++9--------12++++++++30--------pr
MasukkanUser = float(input("masukkan bilangan antara 5 dan 9, dan 12 dan 30 :"))

# -------cek lebih dari 5
LebDar = (MasukkanUser > 5)
print ("lebih dari 5 =", LebDar)

# -------cek kurang dari 9
KurDar  = (MasukkanUser < 9)
print ("kurang dari 9 =", KurDar)

# -------cek lebih dari 12
LebDar = (MasukkanUser > 12)
print ("lebih dari 12 =", LebDar)

# -------cek kurang dari 30
KurDar = (MasukkanUser < 30)
print ("kurang dari 30 =", KurDar)

# benar 
benar = KurDar or LebDar
print ("pengecekkan :", benar)
akhir = (5 > MasukkanUser < 9, 12 > MasukkanUser < 30)
print (akhir)