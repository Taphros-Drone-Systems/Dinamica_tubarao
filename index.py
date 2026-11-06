from time import sleep
from djitellopy import Tello

SHARK_HEIGHT = 40  # altura do tubarão em cm

tello = Tello()
tello.connect(); sleep(3)
battery = tello.get_battery(); sleep(1)
print(battery)

if battery > 70:
    tello.takeoff(); sleep(3)

    initial_height = tello.get_distance_tof(); sleep(1)
    print("initial_height=", initial_height)
    
    shark_found = False
    for _ in range(4):  # para fazer um quadrado
        for _ in range(2):
            tello.move_forward(50); sleep(1)
            current_height = tello.get_distance_tof(); sleep(1)
            print("initial_height, current_height=", initial_height, current_height)
            if current_height <= initial_height - SHARK_HEIGHT:
                shark_found = True
                tello.flip_forward(); sleep(1)  # só funciona com bateria > 50%
                tello.move_forward(50); sleep(1)
                break
        if shark_found:
            break
        tello.rotate_clockwise(90); sleep(1)
    tello.land()
else:
    print("Bateria insuficiente. Substitua a bateria e tente novamente.")
