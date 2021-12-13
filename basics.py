#SORTING #LIST #TUPLE ----------

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

#FLOATING POINT #STRING FORMATTING #INPUT #STAR OPERATOR #DICTIONARY ----------

#Öncelikle, star operator pointer ile alakalı değildir, ama aynı zamanda alakalıdır. Arkasındaki
#düşünce pointerdan gelmektedir. Ne halta yarar, örnekle gösterelim:

n = int(input())
  student_marks = {}
  for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
  query_name = input()
  
#HackeRank örneğinin baş kısmı bu. Burada anlamı, "kullanıcı bir line girecek. line içerisindeki
#ilk kelime name, sonrakileri de bir array halinde al" şeklindedir. Hani arrayler C++'ta ilk
#elemana işaret eden birer pointer ya, *args ile aynı mantık aslında. Bu operator bazen farklı
#anlamlarda da kullanılır. Bu linke bak görmek için:

#https://www.tutorialspoint.com/What-does-the-Star-operator-mean-in-Python

#Dict içindeki keye karşılı kgelen değere (ki burada o değer bir tuple/array) şöyle ulaşılır:

grades = student_marks[query_name]

#Kullanıcı verdiği öğrenci listesinden bir isim girince, o isme ait (keye ait) not listesini (value)
#çekmiş olduk.

average = 0
for grade in grades:
  average = average + grade
average = average / len(grades)
print(format(average, '.2f'))

#Buradaki format fonksiyonu, verilen stringi formatlamak için kullanılır. Burada floating point
#significant digit sayısını belirlemede kullanılmış. Daha enteresan kullanımlar için:
#https://www.w3schools.com/python/ref_string_format.asp

#DICTIONARY #PARSING #I/O ----------

#Gelen inputları kelimelere bölmek için input().split() kullanılır. Input string sonuçta.

N = int(input())
commands_arr = []
for i in range(N):
  command, *operands = input().split()
  commands_arr.append([command, operands])
  
#Burada kod N tane gelen "komut" ları, komut ve argümanları olacak şekilde bir arraye atar. Ama
#neden array de dict değil? Dict olsaydı, aynı komuttan 2 tane (farklı değerlerle de olsa) tutamazdık.
#İlk başta o salak hatayı yaptım, sonra düzelttim. Listler mutable, tuple'lar immutabledır.

#TUPLE #LIST #HASH #STRING #UPPERCASE #LOWERCASE #JOIN #SPLIT ----------

myTuple = tuple(some_list)

#Şeklindeki kod bir list'i tuple'a çevirecektir.

hash(myTuple)

#Şeklindeki kod verilen objenin hash değerini döner. List verirsen listedeki her şeyin tek tek hash
#değerini dönecektir. Hash, Python'un internal kısımlarında hızlı lookup için kullanılır. Daha ayrıntılı
#bilgi için buraya bak:

#https://stackoverflow.com/questions/17585730/what-does-hash-do-in-python

if someString.isupper():
  #do something
string.lower()

#isupper, islower: stringing bütün elemanları upper ya da lowercase mi diye bakar. Aynı şekilde upper ve
#lower fonksiyonları da stringin tüm elemanlarını upper ya da lower yaparlar.

otherString = someString.split(" ")
oneOtherString = "-".join(otherString)

#Bu iki line, verilen someString'i boşluklardan ayrılacak şekilde kelimelere bölüyor, ve sonra bu ayrılmış
#parçaları aralarda tire (-) olacak şekilde tekrar bir araya getiriyor. Cool feature bruv.

#STRING #SEARCH #OVERLAPPING #COUNT ----------

#count() fonksiyonu stringlerde kullanıldığı zaman non-overlapping occurrence'ları döner. Mesela
#aşağıdaki kod 1 dönecektir (verilen ABCDCDC ve substring CDC için):

mainString.count(subString)

#eğer overlapping occurrence'lar lazım ise, çok compact ve anlaşılır bir kod var, buraya eklemek isterim:

def count_substring(string, sub_string):
  sub_length = len(sub_string)
  count = 0
  for i in range(len(string)):
    if string[i:i+sub_length] == sub_string:
      count += 1
  return count

#LIST ----------

results = list(5*("False",))

#Bu kod parçacığı içinde 5 tane 'False' şeklinde string olan bir array oluşturur. Eğer ki:

results = [5*"False"]

#dersen, o zaman oluşan şey

['FalseFalseFalse']

#olacaktır. İstenen buysa güzel ama genelde istenen bu değildir.

