hour = int(input("Enter your hour: "))
min = int(input("Enter your minute: "))
second = int(input("Enter your second: "))
hour = 3600 * hour
min = 60 * min
sum = hour + min + second
print("your time in seconds: ", sum )