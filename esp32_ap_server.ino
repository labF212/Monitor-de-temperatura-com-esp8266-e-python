#include <WiFi.h>
#include <WebServer.h>

/* Put your SSID & Password */
const char* ssid = "ESP32";  // Enter SSID here
const char* password = "12345678";  //Enter Password here

/* Put IP Address details */
IPAddress local_ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WebServer server(80);

String umidade;
String temperatura;


void handle_OnConnect() {
  temperatura = (random(20,30));
  umidade = (random(50,70));
  
  Serial.println(temperatura);
  Serial.println(umidade);
  
  
  server.send(200, "text/plain", temperatura+"e"+umidade);  // 70.0e23.0
}

void handle_NotFound(){
  String message = "File Not Found\n";
  server.send(404, "text/plain", message);
}


void setup() {
  Serial.begin(115200);
 

  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  delay(100);
  
  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);
  
  server.begin();
  Serial.println("HTTP server started");
}
void loop() {
  server.handleClient();
  delay(1000)
 
}
