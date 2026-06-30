import time

def spance_alarm():
    print("Cистема перевантажена!")

capitan_name = input ("Введsть ім'я: ")
print ("Ласкаво просимо на борт, капітане " + capitan_name + "!")
items = ["Лазер","Щит","Мапа зірок"]
print("перевірка предметів:")
for item in items:
    print("Предмет є: "+item+". Готовий до використання.")
    time.sleep(1)
countdawn = 5
while countdawn > 0:
    print ("до старту залишилося " + str (countdawn) + "...")
    countdawn = countdawn -1 # зменшуємо число
    time.sleep(1)
print ("поїхали!")
road =input("Куди летимо?(1-чорна діра/2-зелена планета)")
if road=="1":
    spance_alarm()
    print("Корабель затянуло в чорну діру. Game over")
elif road == "2":
    print("УРА! Перемога, ви знайшли нову дружелюбну цевілізацію! ")
else: print ("Визаснули на робочому місті і збилися з шляху.Game over")