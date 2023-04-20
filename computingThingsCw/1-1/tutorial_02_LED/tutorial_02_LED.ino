
int LEDPin = 15;

void setup() 
{
    Serial.begin(9600);
    pinMode(LEDPin, OUTPUT);
    digitalWrite(LEDPin, LOW);
}

void loop() 
{
    int sensor = A1;
    int analogueReading = analogRead(sensor);
    float conversion = (analogueReading * 3.3) / 4095; // use conversion formula
    
    Serial.print("analogue reading is ");
    Serial.print(analogueReading);
    
    Serial.println();
    
    Serial.print("converted reading is ");
    Serial.print(conversion);

    if (analogueReading < 1500)
    {
        digitalWrite(LEDPin, HIGH);
    }
    else 
    {
        digitalWrite(LEDPin, LOW);
    }
    
    delay(1000);    // led will blink on and off in 1 sec intervals
}
