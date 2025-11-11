'''def max(list):
    maxNumber=list[0]
    for i in list:
        if maxNumber<i:
            maxNumber=i

    return maxNumber

print(max([3,5,2,8]))

def opp():
    str=input("Metin gir: ")
    str=str[::-1]
    print(str)
opp()

def fact(n):
    result=1
    while n!=1:
       result=result*n
       n-=1
    print(result)
fact(6)

def filterEven(list):
    even=[]
    for i in list:
        if i%2==0:
            even.append(i)
    print(even)
filterEven([3,5,7,8])

def mix():
    list1=[1,2]
    list=[1,2,1,3]
    mixed=[]
    for i in range(0,len(list)):
        for j in range(0,len(list1)):
            if list[i]==list1[j]:
                mixed.append(list[i])
    print(set(mixed))

mix()

def palindrom(word):
    if(word==word[::-1]):
        print("Bu metin palindromdur.")
    else:
        print("Metin palindrom değildir")
palindrom("ala")

def ebob(a,b):
    lista=[]
    listb=[]
    listmax=[]
    if a>b:
        for i in range (2,a+1):
            if(a%i==0):
                lista.append(i)
            if(b%i==0):
                listb.append(i)
        print(lista,listb)
        if len(lista)>len(listb):
            for i in range(0,int(len(lista))):
                for j in range(0,int(len(listb))):
                    if(lista[i]==listb[j]):
                        listmax.append(lista[i])
            if listmax==[]:
                print("Ortak bölen yoktur")
            else:
                listmax.sort
                print(listmax)
                print(listmax[-1])
        if len(listb)>=len(lista):
            for i in range(0,int(len(listb))):
                for j in range(0,int(len(lista))):
                    if(lista[j]==listb[i]):
                        listmax.append(lista[j])
            if listmax==[]:
                print("Ortak bölen yoktur")
            else:
                listmax.sort
                print(listmax)
                print(listmax[-1])

            
    if b>a:
        for i in range (2,b+1):
            if(a%i==0):
                lista.append(i)
            if(b%i==0):
                listb.append(i)
        print(lista,listb)
        if len(lista)>=len(listb):
            for i in range(0,int(len(lista))):
                for j in range(0,int(len(listb))):
                    if(lista[i]==listb[j]):
                        listmax.append(listb[j])
            if listmax==[]:
                print("Ortak bölen yoktur")
            else:
                listmax.sort
                print(listmax)
                print(listmax[-1])
            
        if len(listb)>len(lista):
            for i in range(0,int(len(listb))):
                for j in range(0,int(len(lista))):
                    if(lista[j]==listb[i]):
                        listmax.append(lista[j])
            if listmax==[]:
                print("Ortak bölen yoktur")
            else:
                listmax.sort
                print(listmax)
                print(listmax[-1])

    else:
        if listmax==[]:
                print("Ortak bölen yoktur")
        

    
ebob(13,32)  

def anagram(str,str1):
    if len(str)==len(str1):
        list=[]
        str=set(str)
        str1=set(str1)
        print(str,str1)
        for i in str:
            for j in str1:
                if i==j:
                    list.append(i)
        print(list)
        if len(list)==len(str):
            
            return True
        else: return False
    else:
        return False
print(anagram("hello","olleh"))

def isExist(list):
    for i in range(0,list[-1]):
        if i+1==list[i]:
            continue
        else:
            print(f"{i+1} eksik eleman")
            break
        
isExist([1,2,3,5])

def rotate(k):
    list=[1,2,3,7,6,8]
    end=[]
    first=[]
    for i in range(k+1,len(list)):
        end.append(list[i])
    for i in range(0,k+1):
        first.append(list[i])
    print(end+first)

rotate(2)
def median(list,list1):
    result=(list+list1)
    result.sort
    print(result)
    if len(result)%2==0:
        med=float(result[int(len(result)/2)]+result[int(len(result)/2)-1])/2
    else:
        med=float(result[int(len(result)/2)])
    print(med)
    
median([1,2,3],[4,22,23])

def longestPalindrom(str):
    result=[]
    str1=str[::-1]
    print(str1)
    if str==str[::-1]:
        print(str)
    for i in str:
        for j in str1:
            if i==j:
                #print(i)
                if j==str1[len(str)-1]:
                    print(str[len(str)-1])
                    break
                else:
                    result.append(j)
                    
                    break
    print(result)
                

    
longestPalindrom("kalama")'''

def longestPalindrome(s):
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        # Merkez etrafında palindromu genişlet
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Palindromun uzunluğu
    
    for i in range(len(s)):
        # Tek uzunluklu palindrom (merkez bir karakter)
        len1 = expand_around_center(i, i)
        # Çift uzunluklu palindrom (merkez iki karakter arası)
        len2 = expand_around_center(i, i + 1)
        
        # En uzun palindromu güncelle
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]

# Test
print(longestPalindrome("babab"))
# Çıktı: "bab" veya "aba"