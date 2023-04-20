/*
  100% Harry Smith 16048438
*/

const int r = A0;
const int g = A1;
const int b = A5;
const int motionSensor = 27;

int red = 256;
int green = 256;
int blue = 256;
 
#define timeSeconds 10 

 
unsigned long now = millis(); 
unsigned long lastTrigger = 0; 
volatile boolean startTimer = false; 
 
void led_off() 
{ 
  red = 255;
  green = 255;
  blue = 255;
} 
 
void led_random() 
{ 
  red = random(0, 256);
  green = random(0, 256);
  blue = random(0, 256);
} 
 
void led_change() 
{ 
  analogWrite(r, red);
  analogWrite(g, green);
  analogWrite(b, blue);
} 
 
// Checks if motion was detected, and starts a timer 
void IRAM_ATTR detectsMovement()  
{   
  startTimer = true; 
  lastTrigger = millis(); 
  led_random();
  led_change();
} 
 
void setup() { 
  // put your setup code here, to run once: 
  pinMode (r, OUTPUT); 
  pinMode (g, OUTPUT); 
  pinMode (b, OUTPUT); 
  led_off();
  led_change();
  // TO DO: call the relevant functions to pick an "off" RGB colour and 
  //        send the output to their corresponding pins 
 
 
  // PIR Motion Sensor mode INPUT_PULLUP 
  pinMode(motionSensor, INPUT_PULLUP); 
  attachInterrupt(motionSensor, detectsMovement, HIGH); 
   
  Serial.begin(9600); 
} 
 
void loop() { 
  // put your main code here, to run repeatedly: 
 
  // Current time 
  now = millis(); 
  // Turn off the LED after the number of seconds defined in the timeSeconds variable 
  if(startTimer && (now - lastTrigger > (timeSeconds * 1000)))  
  { 
    Serial.println("Motion stopped..."); 
    startTimer = false; 
    led_off();
    led_change();
    // TO DO: call relevant functions to turn off the LED 
     
  } 
  // TO DO: turn on the LED with random RGB values for the number of seconds defined  

  Serial.print("R: "); 
  Serial.print(red); 
  
  Serial.println();

  Serial.print("\tG: "); 
  Serial.print(green);

  Serial.println(); 

  Serial.print("\tB: "); 
  Serial.print(blue); 

  Serial.println();
 
  delay(100); 
} 