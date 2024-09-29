
int LED_PIN = 13;
int MD_PIN = 7;
int MD_VALUE = 0;
int BUTTON_PIN = 8;
int BUTTON_VALUE =0;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  pinMode(MD_PIN, INPUT);
  pinMode(BUTTON_PIN, INPUT);
  digitalWrite(LED_PIN, HIGH);
  Serial.begin(9600);
}

void loop() 
{
  MD_VALUE = digitalRead(MD_PIN);
  BUTTON_VALUE = digitalRead(BUTTON_PIN);
  digitalWrite(LED_PIN, MD_VALUE);
  Serial.println(BUTTON_VALUE);
  

}
