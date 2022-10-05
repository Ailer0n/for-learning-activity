#define sensor_pin A2
 
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
  
}

void loop() {
  int val = analogRead(sensor_pin);
  // Serial.println(val);
  // int min_val = 0;
  // int max_val = 0;
  // if (max_val < val){
  //   max_val = val;
  // }

  // int ar_mean = ((min_val + max_val)/2);
  
  // Serial.println(val);
  // Serial.println("-");
  // Serial.println(min_val);
  // Serial.println(max_val);
  // Serial.println("--");
  // Serial.println(ar_mean); 
  // Serial.println("------------");

if (val < 17){
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);
}else{
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);
} 


}
