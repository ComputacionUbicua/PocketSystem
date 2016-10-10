// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  pinMode(7, INPUT);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int enable = digitalRead(7);
  if(enable == 1)
  {
    int sensorValue = analogRead(A0);
    int sensorValue1 = analogRead(A1);
    int sensorValue2 = analogRead(A2);
    // print out the value you read:
    Serial.print("+");
    Serial.print(sensorValue);
    Serial.print("-");
    Serial.print(sensorValue1);
    Serial.print("-");
    Serial.print(sensorValue2);
    Serial.println("/");
  }
  delay(1);        // delay in between reads for stability
}
