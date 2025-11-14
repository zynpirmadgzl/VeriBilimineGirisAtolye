import numpy as np

#1)	0 ile 9 arasındaki tam sayıları içeren tek boyutlu bir NumPy dizisi (array) oluşturun.
list=np.arange(9)
print(list)
#Sadece sıfırlardan oluşan 3X4 boyutlarında bir matris oluşturun.
list1=np.array([[np.zeros(4)],[np.zeros(4)],[np.zeros(4)]]).astype(int)
print(list1)
#Sadece birlerden oluşan 2X3 boyutlarında bir matris oluşturun.
list2=np.array([[np.ones(3)],[np.ones(3)]])
print(list2)
#4)	np.arange(12).reshape(3, 4) ile oluşturulan bir dizinin boyutunu (shape), eleman sayısını (size) ve kaç boyuta sahip olduğunu (ndim) bulun.
list3=np.arange(12).reshape(3,4)
print(f"{np.shape(list3)}, {np.size(list3)}, {np.ndim(list3)}")
#5)	[10, 20, 30, 40] listesini 64-bit tam sayı (int64) veri tipinde bir NumPy dizisine dönüştürün.
list4=np.array([10,20,30,40],dtype=np.int64)
print(list4.dtype)

#6)	np.arange(20) dizisi içindeki 5'ten büyük ve 15'ten küçük olan tüm elemanları seçerek yeni bir dizi oluşturun.
list5=np.arange(20)
list5=list5[list5>5 ]
list5=list5[list5<15]

print(list5)
#7)	a = np.array([1, 2, 3]) ve b = np.array([4, 5, 6]) dizilerini oluşturun.
a=np.array([1,2,3])
b=np.array([4,5,6])
#Bu iki dizinin toplamını ve çarpımını (eleman bazında) hesaplayın.
print(a+b)
print(a*b)
#9)	M = np.arange(1, 26).reshape(5, 5) matrisini oluşturun.
M=np.arange(1,26).reshape(5,5)
#10)Matrisin ikinci satırını ([6, 7, 8, 9, 10]) ve üçüncü sütununu ([3, 8, 13, 18, 23]) seçip ekrana yazdırın.
print(M[1])
print(M[:,2])
#12)	3X2 boyutunda rastgele tam sayılardan oluşan bir matris oluşturun ve bu matrisin transpozunu (devriğini) alın (2 X3 olmalı).
c=np.arange(6).reshape(3,2)
print(np.transpose(c))
#14)	dizi = np.array([1, 2, np.nan, 4, 5, np.nan, 7]) dizisindeki boş (NaN) eleman sayısını bulun.
dizi = np.array([1, 2, np.nan, 4, 5, np.nan, 7])
dizi=np.isnan(dizi)
print(dizi)
counter=0
for i in dizi:
    
    print(i)
    if i:
        counter+=1

print(counter)

#5X5 boyutlarında rastgele tam sayılardan oluşan bir matris oluşturun.
list7=np.random.randint(0,25,25).reshape(5,5)
print(list7)
#Bu matrisin tüm elemanlarının ortalamasını, en büyük değerini ve sütun bazındaki standart sapmasını (axis=0 kullanarak) hesaplayın.
print(np.mean(list7))
print(np.max(list7))
print(np.std(list7,axis=0))
#a = np.array([1, 2]) ve b = np.array([3, 4]) dizilerini yatay (hstack) ve dikey (vstack) olarak birleştirin.
a = np.array([1, 2]) 
b = np.array([3, 4])
d=np.array([a,b])
print(d)
print(np.transpose(d))
#A = np.array([[1, 2], [3, 4]]) ve B = np.array([[5, 6], [7, 8]]) matrislerini oluşturun.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
#Bu iki matrisin matris çarpımını (dot product) hesaplayın. (Skaler çarpım değil!)
C=np.dot(A,B)
print(C)

#5X5 boyutlarında rastgele bir matris oluşturun.
list8=np.random.randint(0,25,25).reshape(5,5)
#Bu matrisin her bir sütununa, o sütunun ortalama değerini çıkararak veriyi merkezleyin (ortalama sıfır olacak şekilde).
print(list8)
M=list8.astype(float)
col_mean=np.mean(M,axis=0)
print(f"{col_mean}, {col_mean.shape}")
M_centered=M-col_mean
print(M_centered)
means_after = M_centered.mean(axis=0)
print("Merkezlendikten sonra sütun ortalamaları (yaklaşık 0 olmalı):\n", means_after)
#C = np.array([[4, 7], [2, 6]]) matrisini oluşturun.
Z = np.array([[4, 7], [2, 6]])
#Matrisin determinantını hesaplayın.
print(np.linalg.det(Z))
#Matrisin tersini (inverse) hesaplayın ve ters matris ile orijinal matrisi çarparak birim matris (Identity Matrix) elde edip etmediğinizi kontrol edin.
Z_inv=np.linalg.inv(Z)
print(Z_inv)

result=Z_inv.dot(Z)
print(result)
print(np.allclose(result,np.eye(2)))

#veri = np.array([1, 2, 1, 4, 5, 2, 7, 1]) dizisindeki benzersiz elemanları ve her bir elemanın kaç kez tekrarlandığını bulun.
veri = np.array([1, 2, 1, 4, 5, 2, 7, 1])
unique_values, counts=np.unique(veri,return_counts=True)
print(f"{unique_values} , {counts}")

#dizi = np.random.randn(100) (Normal dağılımdan 100 rastgele sayı) dizisini oluşturun.
dizi = np.random.randn(100)
print(dizi)
#Dizideki tüm değerleri -2 ve 2 aralığına kırpın (clip). Yani, -2'den küçük olanları -2 yapın, 2'den büyük olanları 2 yapın.
dizi[dizi<-2]=-2
dizi[dizi>2]=2
print(f"\n\n{dizi}")
#v1 = np.array([1, 2, 3]) ve v2 = np.array([4, 5, 6]) vektörlerini oluşturun.
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
#Bu iki vektörün nokta ürününü (inner product) ve dış ürününü (outer product) hesaplayın.
inner=np.inner(v1,v2)
outer=np.outer(v1,v2)
print(inner)
print(f"\n\n{ outer}")
#1.000.000 elemanlı büyük bir listeyi (py_list) ve aynı elemanları içeren bir NumPy dizisini (np_array) oluşturun.
py_list=[]

for i in range(0,1000000):
    py_list.append(i)
print(py_list)

np_array=np.arange(1000000)
print(np_array)