import serial
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()


def main():
    try:
        ser = serial.Serial("COM3", 74880, timeout=1)
        state = 0
        while True:
            if ser.in_waiting > 0:
                try:
                    serial_data = ser.readline().decode().strip()
                    print(serial_data)
                    if serial_data == "0":
                        if state == 0:
                            keyboard.press(Key.esc)
                            keyboard.release(Key.esc)
                            print("Pressed escape key")
                            state = 1
                    elif serial_data == "1":
                        if state == 1:
                            state = 0
                        pass
                except:
                    print("An exception occurred")
    except:
        print("Couldn't access device, trying again in 1 second")
        time.sleep(1)
        main()


if __name__ == "__main__":
    main()
