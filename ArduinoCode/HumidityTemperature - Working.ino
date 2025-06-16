#include <DHT.h>
#define Type DHT11

String myCmd;
bool blinking = false;
int sensePin = 2;

DHT humidityAndTemparture(sensePin, Type);

float humidity;
float tempC;
float tempF;

int setTime = 500;
int shortDelay = 250;
int longDelay = 2500;
int normalDelay = 1000;
int outputTime = 500;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  humidityAndTemparture.begin();
  
  delay(setTime); // give sensor time to intialise
}

void loop() {
  delay(2000);

  // Serial.print("\n");
  // humidity = humidityAndTemparture.readHumidity();
  // tempC = humidityAndTemparture.readTemperature();
  // tempF = humidityAndTemparture.readTemperature(true);

  // Serial.print("Humidty: ");
  // Serial.println(humidity);
  // Serial.print("Temperature C: ");
  // Serial.println(tempC);
  // Serial.print("Temperature F: ");
  // Serial.println(tempF);
  // delay(outputTime);

  blinkLED();

  while(Serial.available() == 0){
    // blinkLED();
  }
  
  myCmd = Serial.readStringUntil('\r');
  // Serial.println(myCmd);

    if(myCmd == "ON"){
      digitalWrite(LED_BUILTIN, HIGH);
    }else if (myCmd == "OFF"){
      digitalWrite(LED_BUILTIN, LOW);
    }else if (myCmd == "getTempC"){
      getTempC();
    }else if (myCmd == "getTempF"){
      getTempF();
    }else if (myCmd == "getHumidity"){
      getHumidity();
    }else if (myCmd == "getAll"){
      getAll();
    }else {
      Serial.print("NOT FOUND");
    }
 
}
void getHumidity(){
  humidity = humidityAndTemparture.readHumidity();

  if (isnan(humidity)){
    Serial.println("ERR");
  }else{
    Serial.println(humidity);
  }
  Serial.println();
}
void getTempC(){
  tempC = humidityAndTemparture.readTemperature();
  if(isnan(tempC)){
    Serial.println("ERR");
  }else{
    Serial.println(tempC);
  }
}
void getTempF(){
  tempF = humidityAndTemparture.readTemperature(true);

  if(isnan(tempF)){
    Serial.println("ERR");
  }else{
    Serial.println(tempF);
  }
}

void getAll() {
  Serial.print(humidityAndTemparture.readHumidity());
  Serial.print(humidityAndTemparture.readTemperature());
  Serial.print(humidityAndTemparture.readTemperature(true));
}
int blinkLED() {
  // turn on an doff 10 times fast to show initialisation


  for (int i = 0; i < 10; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(shortDelay);
    digitalWrite(LED_BUILTIN, LOW);
    delay(shortDelay);
  }

  delay(normalDelay);
  digitalWrite(LED_BUILTIN, LOW);
  delay(normalDelay);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(normalDelay);
  digitalWrite(LED_BUILTIN, LOW);
  delay(normalDelay);
}