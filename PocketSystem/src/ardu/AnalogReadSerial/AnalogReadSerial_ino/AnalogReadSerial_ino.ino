byte pins[] = {2,3,4,5,6,7,8,9,10,11};
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  for (byte i=0; i<10; i++) 
  {
    pinMode(pins[i], OUTPUT);
  }
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue0 = analogRead(A0);
  int sensorValue1 = analogRead(A1);
  int sensorValue2 = analogRead(A2);
  // print out the value you read:
  Serial.print("1 ");
  Serial.print(sensorValue0);
  Serial.print(" - 2 ");
  Serial.print(sensorValue1);
  Serial.print(" - 3 ");
  Serial.println(sensorValue2);

  delay(1);        // delay in between reads for stability
}
