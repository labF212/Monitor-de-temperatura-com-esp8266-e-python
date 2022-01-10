#include <WiFi.h>
#include <WebServer.h>
#include "DHTesp.h"

DHTesp dht;

/* Put your SSID & Password */
const char* ssid = "ESP32";  // Enter SSID here
const char* password = "12345678";  //Enter Password here

/* Put IP Address details */
IPAddress local_ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WebServer server(80);





void handle_OnConnect() {
  String umidade = String(dht.getHumidity());
  String temperatura = String(dht.getTemperature()); 
  server.send(200, "text/plain", temperatura+"e"+umidade);  // 70.0e23.0
}

void handle_NotFound(){
  String message = "File Not Found\n";
  server.send(404, "text/plain", message);
}


void setup() {
  dht.setup(14, DHTesp::DHT11); // D5
  
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
  delay(1500);

  float u = dht.getHumidity();
  float t = dht.getTemperature();
  Serial.print("Umidade (%): ");
  Serial.print(u, 1);
  Serial.print("\t");
  Serial.print("Temperatura (C): ");
  Serial.print(t, 1);
  Serial.print("\t");
  Serial.println();
}
