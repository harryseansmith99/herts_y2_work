int LEDPin = 21;
int potentiometerPin = A6;


/*

    100% 16048438 HARRY SMITH

*/

void setup() 
{
    Serial.begin(9600);
    pinMode(LEDPin, OUTPUT);
}

void loop() 
{
    int potentiometerReading = analogRead(potentiometerPin);
    
    int brightness = map(potentiometerReading, 0, 4095, 0, 100);
    
    analogWrite(LEDPin, brightness);
    
    Serial.println(brightness);
    
    delay(100);
}

