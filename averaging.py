counter = 0
sum = 0
while True:
 grade = input("Enter the grade of the lesson or type the word 'exit' to exit: ")
 if grade == "exit":
    break
 else:
     grade = float(grade)
     counter = counter + 1
     sum = grade + sum
print("average: ", sum/counter)
print("thank you for using my app")
        