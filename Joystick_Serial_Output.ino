// READ JOYSTICK VALUES AND PRINT OVER SERIAL

const int SW_pin = 2;   // Digital pin connected to Switch button
const int X_pin = 0;    // Analog pin connected to X
const int Y_pin = 1;    // Analog pin connected to Y

int AXIS_HIGH = 795;
int AXIS_LOW = 195;
int AXIS_NORM = 490;
int DELAY_MS = 200;

void setup() {
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(115200);
}

void loop() {
  
  int SWITCH_BUTTON = digitalRead(SW_pin);
  int X_AXIS = analogRead(X_pin);
  int Y_AXIS = analogRead(Y_pin);

  if (SWITCH_BUTTON == 0){
    Serial.println("1");
    delay(DELAY_MS);
  }
  if (X_AXIS < AXIS_LOW){
    Serial.println("2");
    delay(DELAY_MS);
  }
  if (X_AXIS > AXIS_HIGH){
    Serial.println("3");
    delay(DELAY_MS);
  }
  if (Y_AXIS < AXIS_LOW){
    Serial.println("4");
    delay(DELAY_MS);
  }
  if (Y_AXIS > AXIS_HIGH){
    Serial.println("5");
    delay(DELAY_MS);
  }
    

}
