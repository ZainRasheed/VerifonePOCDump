#include<ESP8266WiFi.h>
#include<ESP8266WebServer.h>

ESP8266WebServer server;

const char* ssid = "ACT102439631311";
const char* password = "26180410";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

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

  server.on("/", [](){server.send(200, "text/html", "<html><body><h1>Hello world!</html></body></h1>");});
  server.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();

}
