#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>


const char* ssid = "V20_1263";
const char* password =  "gh8059936";
String address = "http://192.168.171.197:5026/insert";

String result = "";
HTTPClient http;
void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  

  
}
void loop() {
 
  
      if ((WiFi.status() == WL_CONNECTED)) { //Check the current connection status
      String result = address + "?"+"data1=" + "1"+"&data2=" + "2"+"&data3=" + "3"+"&data4=" + "4"+"&data5=" + "5"+"&data6=" + "6"+"&data7=" + "7";
      http.begin(result);
      int httpCode = http.GET();
      if (httpCode > 0) {
      //      Serial.println(httpCode);
      String result = http.getString();
      Serial.println(result);
      http.end();
      } else {
      Serial.println("Error on HTTP request");
      }
      delay(500);
    }
  
  }
