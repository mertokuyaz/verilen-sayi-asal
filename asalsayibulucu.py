#1 asal sayı değildir!
sayı = int(input("Lütfen bir pozitif sayı giriniz: "))

def ran(start, end):
    return range(start, end+1)

    #alternatif olarak for loop için de yazılabilir
    #o sayiya kadar olan bütün sayıları o sayının kendisiyle böl gibi.
    #eğer bölünebilen sayı varsa print(num, "bir asal sayi degil") döngüsünü başlat.

if sayı > 1:  
   for i in ran(2, sayı//2): 
       if (sayı % i) == 0: 
           print(sayı, "bir asal sayı değil") 
           break
   else: 
       print(sayı, "bir asal sayı") 
  
else: 
   print(sayı, "bir asal sayı") 
