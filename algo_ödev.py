# Recursive fonksiyon ile hanoi kuleleri çözümü

def HanoiKuleleri(n, kaynak, hedef, yedek):
    if n == 1:
        print("Disk 1 Taşı, Kaynak:", kaynak, " Hedef:", hedef)
        return
    HanoiKuleleri(n - 1, kaynak, yedek, hedef)
    print("Disk", n, "Taşı, Kaynak:", kaynak, " Hedef:", hedef)
    HanoiKuleleri(n - 1, yedek, hedef, kaynak)


# Sürücü Kod
n=(int(input("bir sayi giriniz")))
HanoiKuleleri(n, 'A', 'B', 'C')
# A, C, B çubukların adıdır
