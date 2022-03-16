#include<ESP8266WiFi.h>

const char *ssid = "ESP_Hotspot";
const char *password = "Batman";

IPAddress ip(192,168,11,4);
IPAddress gateway(192,168,11,1);
IPAddress subnet(255,255,255,0);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(1000);
  
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip, gateway, subnet);
  WiFi.softAP("ESP_Hotspot", "Batmanman"); //Create hotspot
  
  Serial.println("");  
  Serial.println("----------------------------------------------");
  Serial.print("   Application '");Serial.print("<ProjectName>");Serial.println("' is running");
  Serial.print("   Instance    ");Serial.println(WiFi.softAPIP());
  Serial.print("   ssid        ");Serial.println(ssid);  
  Serial.print("   password    ");Serial.println(password);  
  Serial.println("----------------------------------------------");  
  Serial.println("");  

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("________________________");
  Serial.println("Connected stations:");
  Serial.println(WiFi.softAPgetStationNum());
  delay(10000);
}
