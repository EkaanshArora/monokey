# Monokey

use a cherry mx style mechanical switch with esp8266 to simulate a keystroke

inspired by [evan kale on youtube](https://www.youtube.com/watch?v=frV9unHnqgg)

- python script to read esp8266 serial input and perform a keypress
- arduino sketch to program an esp8266 or compatible microcontroller to read button press and write to serial

the esp8266 (what i had on hand) doesn't have native USB so we use the python script to read the serial output and simulate a keypress

if you're thinking of building this, i'd suggest using an ardino pro micro or something that has atmega32u4 that can utilise `Keyboard.h` to act as a real HID (human interface device) keyboard