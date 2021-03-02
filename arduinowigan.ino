#include <Wiegand.h>
#include <SPI.h>
#include <Ethernet.h>
WIEGAND wg;
// replace the MAC address below by the MAC address printed on a sticker on the Arduino Shield 2
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

EthernetClient client;

int    HTTP_PORT   = 8000;
String HTTP_METHOD = "GET";
char   HOST_NAME[] = "192.168.58.124"; // change to your PC's IP address
String PATH_NAME   = "/";
String queryString = "?rfid=";

void setup() {
  Serial.begin(9600);
  wg.begin();
  pinMode(8, OUTPUT);
  // initialize the Ethernet shield using DHCP:
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to obtaining an IP address using DHCP");
    while (true);
  }

  // connect to web server on port 80:

}

void loop() {
  if (wg.available())
  {
    String data = String(wg.getCode());
    Serial.println(data);
    if (client.connect(HOST_NAME, HTTP_PORT)) {
      // if connected:
      Serial.println("Connected to server");
      // make a HTTP request:
      // send HTTP header
      client.println(HTTP_METHOD + " " + PATH_NAME + queryString + data + " HTTP/1.1");
      client.println("Host: " + String(HOST_NAME));
      client.println("Connection: close");
      client.println(); // end HTTP header

      while (client.connected()) {
        if (client.available()) {
          // read an incoming byte from the server and print it to serial monitor:
          char c = client.read();
          Serial.print(c);
          if (c == '1') {
            digitalWrite(8, HIGH);
          }
          else {
            digitalWrite(8, LOW);
          }

        }
      }

      // the server's disconnected, stop the client:
      client.stop();
      Serial.println();
      Serial.println("disconnected");
    } else {// if not connected:
      Serial.println("connection failed");
    }
  }
}
