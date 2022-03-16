#include<ESP8266WiFi.h>

const char* ssid = "ESP_Hotspot";
const char* password = "Batmanman";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  WiFi.begin(ssid, password); //This is an async method.
  while (WiFi.status()!=WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.println("----------------------------------------------");
  Serial.print("   Connected to WIFI: ");Serial.println(ssid);
  Serial.print("   Application '");Serial.print("<ProjectName>");Serial.println("' is running");
  Serial.print("   Instance    ");Serial.println(WiFi.localIP());
  Serial.println("----------------------------------------------");

}

void loop() {
  // put your main code here, to run repeatedly:

}
