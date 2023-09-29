# nested loop
number = [5,2,5,2,2]
for i in number:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)
# Or
number = [5,2,5,2,2]
for i in number:
    print('x' * i)



for x in range(4):
    for y in range(5):
     print(f"({x},{y})")


# for loop
prices = [10,20,40]

total = 0
for i in prices:
    total += i
print(f"Total cost: {total}")

# for item in range(20):
#     print(item)




#car game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
        print(" car started")
    elif command == "stop":
        if not started:
            print("car is already stop")
        else:
            started = False
        print("car stopped")
    elif command == "help":
        print("""start the car
     stop the car
     quit """)
    elif command == "quit":
        break
    else:
        print("sorry")








# select number
secrets_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the secrete number: '))
    guess_count += 1
    if guess == secrets_number:
        print('you win')
        break
    else:
        print("you are wrong")


i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")
