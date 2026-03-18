import socket
import keyboard
import time

ROBOT_IP = "192.168.0.113"
ROBOT_PORT = 3000
LEFT_TRACK_SPEED = -100
RIGHT_TRACK_SPEED = 100
sleep_time = 0.5

while True:
    try:
        if keyboard.is_pressed('w'):
            print('You Pressed w')
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(bytes(f"{100};{100}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            time.sleep(1)
            s.sendto(bytes(f"{0};{0}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            s.close()
        elif keyboard.is_pressed('s'):
            print('You Pressed s')
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(bytes(f"{-100};{-100}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            time.sleep(1)
            s.sendto(bytes(f"{0};{0}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            s.close()

        elif keyboard.is_pressed('a'):
            print('You Pressed a')
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(bytes(f"{50};{-50}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            time.sleep(0.2)
            s.sendto(bytes(f"{0};{0}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            s.close()

        elif keyboard.is_pressed('d'):
            print('You Pressed d')
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(bytes(f"{-50};{50}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            time.sleep(0.2)
            s.sendto(bytes(f"{0};{0}", "utf-8"),
                        (ROBOT_IP, ROBOT_PORT))
            s.close()

    except:
        break

