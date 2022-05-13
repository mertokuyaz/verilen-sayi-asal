sayı = int(input("Lütfen bir sayı giriniz: "))

def ran(start, end):
    return range(start, end+1)

    #alternatif olarak for loop için de yazılabilir
    #o sayiya kadar olan bütün sayıları o sayının kendisiyle böl gibi.
    #eğer bölünebilen sayı varsa print(num, "asal sayi degil") döngüsünü başlat.

if sayı > 1:  
   for i in ran(2, sayı//2): 
       if (sayı % i) == 0: 
           print(sayı, "asal sayı değil") 
           break
   else: 
       print(sayı, "asal sayı") 
  
else: 
   print(sayı, "asal sayı") 
