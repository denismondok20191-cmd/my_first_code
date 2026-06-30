def spance_alarm():
    print("ТРИВОГА!")
    print("УВАГА! ЗБІЙ У СИСТЕМІ ДМИГУНА!")
    print("ТРИВОГА!")

choice=input("Запустити двигун?(так?ні)")
if choice != "так":
    spance_alarm()