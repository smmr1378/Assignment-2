second = int(input("Enter your second: "))
h = second / 3600
hour= int(h)
min = (second % 3600) // 60
seconds = second % 60
print("your hour: ", hour, min, seconds )