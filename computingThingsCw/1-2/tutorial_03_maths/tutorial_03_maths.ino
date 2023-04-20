#define ntemp 10 
#include <DHT.h> 
#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

float temp[ntemp]; 
static int measurement_counter = 0; 
 
float getMin() 
{ 
    float result = temp[0]; 
    for (int i = 1; i < ntemp; i++) 
    { 
        if(temp[i] < result) 
        { 
            result = temp[i]; 
        } 
    } 
    return result; 
} 
 
float getMax() 
{ 
    float result = temp[0]; 
    for (int i = 1; i < ntemp; i++) 
    { 
        if(temp[i] > result) 
        { 
            result = temp[i]; 
        } 
    } 
    return result; 
} 
 
float getAvg() 
{ 
    float result = 0.0; 
    for (int i = 0; i < ntemp; i++) 
    { 
        result = result + temp[i]; 
    } 
    return (result / ntemp); 
} 
 
float getStdv() 
{ 
    float avg = getAvg(); 
    float deviation = 0.0; 
    float sumsqr = 0.0; 
    for (int i = 0; i < ntemp; i++) 
    { 
        deviation = temp[i] - avg; 
        sumsqr = sumsqr + sq(deviation); 
    } 
    float variance = sumsqr / ntemp; 
    return sqrt(variance); 
} 
 
void initialisation() 
{ 
    for (int i = 0; i < ntemp; i++) 
    { 
        temp[i] = 0.0; 
    } 
} 
 
void addCounter() 
{ 
    measurement_counter = measurement_counter + 1; 
   
    if (measurement_counter >= ntemp) 
    { 
        printProcessedData(); 
        resetCounter(); 
    } 
} 
 
void resetCounter() 
{ 
    measurement_counter = 0; 
} 

void addReading(float t) 
{ 
    temp[measurement_counter] = t; 
    addCounter(); 
} 
 
void printProcessedData() 
{ 
    Serial.print("Min: "); 
    Serial.print(getMin()); 
    Serial.print(", Max: "); 
    Serial.print(getMax()); 
    Serial.print(", Avg: "); 
    Serial.print(getAvg()); 
    Serial.print(", Stdev: "); 
    Serial.println(getStdv()); 
} 
 
void setup() 
{ 
    // put your setup code here, to run once: 
    Serial.begin(9600); 
    dht.begin(); 
    initialisation(); 
} 
 
void loop(){
    float deg_celcius = dht.readTemperature(); // Stores Celcius temperature value 
    Serial.print("temperature in celcius: ");
    Serial.print(deg_celcius);
    Serial.println();
    addReading(deg_celcius);
    delay(1000); 
} 
