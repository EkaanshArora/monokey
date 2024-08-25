int buttonState = HIGH;  // Initialize with HIGH (because of INPUT_PULLUP)
int lastButtonState = HIGH; // Initialize with HIGH as well
unsigned long lastDebounceTime = 0;  // The last time the output was toggled
unsigned long debounceDelay = 50;    // The debounce time (50 ms is usually sufficient)

void setup() {
  Serial.begin(74880);
  pinMode(4, INPUT_PULLUP);  // Configure pin 4 as input with a pull-up resistor
}

void loop() {
  // Read the state of the button
  int reading = digitalRead(4);

  // If the button state has changed
  if (reading != lastButtonState) {
    // Reset the debounce timer
    lastDebounceTime = millis();
  }

  // Check if the debounce delay has passed
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // If the button state has stabilized
    if (reading != buttonState) {
      buttonState = reading;

      // Print the button state when it has changed after debounce
      Serial.print(buttonState);
      Serial.print("\n");
    }
  }

  // Save the current reading for the next iteration
  lastButtonState = reading;
}
