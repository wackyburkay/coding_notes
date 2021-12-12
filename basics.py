#Bir listeyi sortlarken, listenin elemanları tuple veya daha uzun şeyler ise, listeyi
#hangi tuple elemanına göre sortlayacağımızı "tup" argümanı belirler. Örn:

records = []

for _ in range(int(input())):
  name = input()
  score = float(input())
  records.append([name, score])
  
records.sort(key=lambda tup: tup[1])

#Bunu yazmak 'score'a göre sıralanmasını sağlar. Peki önce skora bak, sonra da isme bak
#şeklinde bişey isteseydik? O zaman da "x" argümanı kullanılır.

records.sort(key=lambda x:(x[1], x[0]))

#Burada diyoruz ki önce skora bak, onlar aynıysa isme bak. Stringleri de alfabetik olarak
#sıralıyor default halinde. Genellikle istenen de odur.

