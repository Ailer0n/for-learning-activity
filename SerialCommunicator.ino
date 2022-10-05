#define led_pin 3
// #define sensor_pin A2

void setup() {
 pinMode(led_pin,OUTPUT);
 Serial.begin(9600);
}

void loop() {
if (Serial.available() > 0) {
  char  message = Serial.read();
  Serial.println(message);

    if  (message == 'u'){
      digitalWrite(led_pin, HIGH);
    }
    else if (message == 'd'){
      digitalWrite(led_pin, LOW);
    }

    else if (message == 'i'){
      int val = analogRead(sensor_pin);
      val = map(val, 0, 1023, 100, 999)
      Serial.print(val);
    }
    else if (message == '\n'){
    }
    else{
      Serial.println("unknown Message");
    }

    
  }
}

