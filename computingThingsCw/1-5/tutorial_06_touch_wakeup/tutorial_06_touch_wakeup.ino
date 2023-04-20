/*
  100% Harry Smith 16048438
*/

#define threshold 40 
 
RTC_DATA_ATTR int bootCount = 0; 
RTC_DATA_ATTR int touchCount = 0; 
 
touch_pad_t touchPin; 
 
int touched = 0; 
 
void wakeup_cause() 
{ 
  esp_sleep_wakeup_cause_t wakeup_reason; 
 
  wakeup_reason = esp_sleep_get_wakeup_cause(); 
 
  switch(wakeup_reason)
  {
    case ESP_SLEEP_WAKEUP_EXT0 : Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
    case ESP_SLEEP_WAKEUP_EXT1 : Serial.println("Wakeup caused by external signal using RTC_GPIO"); break;
    case ESP_SLEEP_WAKEUP_TIMER : Serial.println("Wakeup caused by timer"); break;
    case ESP_SLEEP_WAKEUP_TOUCHPAD : Serial.println("Wakeup caused by touchpad"); break;
    case ESP_SLEEP_WAKEUP_ULP : Serial.println("Wakeup caused by ULP program"); break;
    default : Serial.println("Wakeup was not caused by deep sleep"); break;
  }
} 
 
void wakeup_touch()
{
  touchPin = esp_sleep_get_touchpad_wakeup_status();

  switch (touchPin)
  {
    case TOUCH_PAD_NUM0:
      Serial.println("Touch detected on TOUCH_PAD_NUM0");
      break;
    case TOUCH_PAD_NUM1:
      Serial.println("Touch detected on TOUCH_PAD_NUM1");
      break;
    case TOUCH_PAD_NUM2:
      Serial.println("Touch detected on TOUCH_PAD_NUM2");
      break;
    case TOUCH_PAD_NUM3:
      Serial.println("Touch detected on TOUCH_PAD_NUM3 AKA pin15");
      break;
    case TOUCH_PAD_NUM4:
      Serial.println("Touch detected on TOUCH_PAD_NUM4");
      break;
    case TOUCH_PAD_NUM5:
      Serial.println("Touch detected on TOUCH_PAD_NUM5");
      break;
    case TOUCH_PAD_NUM6:
      Serial.println("Touch detected on TOUCH_PAD_NUM6");
      break;
    case TOUCH_PAD_NUM7:
      Serial.println("Touch detected on TOUCH_PAD_NUM7");
      break;
    case TOUCH_PAD_NUM8:
      Serial.println("Touch detected on TOUCH_PAD_NUM8");
      break;
    case TOUCH_PAD_NUM9:
      Serial.println("Touch detected on TOUCH_PAD_NUM9");
      break;
    default : Serial.println("Wakeup not by touchpad"); break;
  }
} 
 
void callback() 
{   
  touched = 1; 
} 
 
void setup()  
{ 
  // put your setup code here, to run once: 

 
  Serial.begin(115200); 
  delay(1000); 
 
  ++bootCount; 
  Serial.print("Boot number: "); 
  Serial.println(bootCount); 
 
  wakeup_cause(); 
  wakeup_touch(); 

  touchAttachInterrupt(T3, callback, threshold);



  delay(1000); // due to the fact that the board has to be awake for call back to be executed 
 
  if(touched == 1) 
  { 
    ++touchCount; 
    Serial.print("Touch number: "); 
    Serial.println(touchCount); 
    touched = 0; 

  }   
 
  //Configure Touchpad as wakeup source 
  esp_sleep_enable_touchpad_wakeup(); 
 
  Serial.println("Going to sleep now"); 
  Serial.flush();  
  esp_deep_sleep_start(); 
} 
 
void loop()  
{ 
  //This will never be reached 
} 