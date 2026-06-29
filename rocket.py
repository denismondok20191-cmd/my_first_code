import time

countdawn = 5
while countdawn > 0:
    print ("до старту залишилося " + str (countdawn) + "...")
    countdawn = countdawn -1 # зменшуємо число
    time.sleep(1)
print ("поїхали!")