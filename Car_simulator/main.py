is_car_started = False

while True:
    user_input = input('>').lower()
    if user_input == 'help':
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif user_input == 'start':
        if is_car_started == False:
            is_car_started = True
            print('Car is started')
        else:
            print('Car is already started')
    elif user_input == 'stop':
        if is_car_started == True:
            is_car_started = False
            print('Car is stop')
        else:
            print('Car is already stopped')
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that...")

print('Thaks for play')
