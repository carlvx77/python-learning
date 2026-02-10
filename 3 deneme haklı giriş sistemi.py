users = {
    "carl": "5151",
    "ege": "2525"
}

def login(u, p):
    if u in users and users[u] == p:
        return True, "giriş başarılı"
    else:
        return False, "hatalı bilgiler"

hak = 3
while hak > 0:
    u = input("kullanıcı adınızı giriniz: ")
    p = input("şifrenizi giriniz: ")
    sonuc, mesaj = login(u, p)
    if sonuc:
        print("HOŞGELDİN REİS")
        break
    else:
        hak -= 1
        print(mesaj, "kalan deneme hakkı", hak)
    if hak == 0:
        print("hesap kilitlenmiştir")