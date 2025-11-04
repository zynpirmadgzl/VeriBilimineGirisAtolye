### 15. Pratik Alıştırmalar

'''Bu alıştırmaları çözerek öğrendiklerinizi pekiştirin:

- **Alıştırma 1: Tek mi Çift mi?** Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir program yazın.


- **Alıştırma 2: Faktöriyel Hesaplama** Bir sayının faktöriyelini hesaplayan bir fonksiyon yazın. (Örnek: 5! = 5 × 4 × 3 × 2 × 1 = 120)

- **Alıştırma 3: Kelime Sayacı** Kullanıcıdan bir cümle alın ve bu cümlede kaç kelime olduğunu bulan bir program yazın.

- **Alıştırma 4: Ortalama Hesaplama** Bir liste içindeki sayıların ortalamasını hesaplayan bir fonksiyon yazın.

- **Alıştırma 5: Palindrom Kontrolü** Bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın. (Palindrom: tersten okunuşu da aynı olan kelime, örnek: 'kayak')

- **Alıştırma 6: Liste Filtreleme** Bir sayı listesinden sadece pozitif sayıları seçen bir fonksiyon yazın.

### 16. Gelecek Hafta için Hazırlık

- **Python.org:** Resmi Python dokümantasyonu

- **W3Schools Python Tutorial:** İnteraktif öğrenme platformu

- **Real Python:** Detaylı Python makaleleri ve öğreticiler

- **LeetCode / HackerRank:** Pratik yapabileceğiniz platformlar'''

number=int(input("Sayı gir: "))
if number%2==0:
    print("Sayı çift")
else:
    print("Sayı tek")


def fact(n):
    result=1
    while n!=1:
       result=result*n
       n-=1
    print(result)
fact(6)

def word(str):
    str=str.split(" ")
    return(len(str))
print(word("Merhaba dünya nasılsın"))

def avg(list):
    return (sum(list))/len(list)
print(avg([3,5,7,9]))

def palindrom(word):
    if(word==word[::-1]):
        print("Bu metin palindromdur.")
    else:
        print("Metin palindrom değildir")
palindrom("ala")

def filter(list):
    positive=[]
    for i in list:
        if i>0:
            positive.append(i)
    print(positive)            
filter([-5,-4])