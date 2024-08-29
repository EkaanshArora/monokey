import serial
from serial import SerialException
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def press_escape_key():
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    print("Pressed escape key")

def read_serial(ser):
    try:
        serial_data = ser.readline().decode().strip()
        print(serial_data)
        return serial_data
    except UnicodeDecodeError:
        print("Decoding error")
        return None
    except SerialException as e:
        print(f"Serial error: {e}")
        return None

def main():
    ser = None
    state = 0
    
    while True:
        try:
            # If no serial connection, try to connect
            if ser is None or not ser.is_open:
                try:
                    ser = serial.Serial("COM3", 74880, timeout=0.1)
                    print("Connected to device")
                except SerialException:
                    print("Failed to connect, retrying in 1 second...")
                    time.sleep(1)
                    continue
            
            # Read from the serial port
            if ser.in_waiting > 0:
                serial_data = read_serial(ser)

                if serial_data == "0" and state == 0:
                    press_escape_key()
                    state = 1
                elif serial_data == "1" and state == 1:
                    state = 0
        
        except SerialException:
            print("Lost connection to the device. Trying to reconnect...")
            if ser is not None:
                ser.close()
            ser = None  # Reset the serial object
            time.sleep(1)  # Wait before retrying

        except KeyboardInterrupt:
            print("Program terminated by user.")
            if ser is not None and ser.is_open:
                ser.close()
            break

if __name__ == "__main__":
    main()
