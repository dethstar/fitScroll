// declare everything.
int ban = 7;
int ban2 = 8;
int led = 13;
int flag1=0;
int flag2=0;
int res=0;

//typical arduino setup
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  //start ban,ban2 as input pins 
  pinMode(ban, INPUT);
  pinMode(ban2, INPUT);
  pinMode(led, OUTPUT);//for debugging, will use Arduino's in led.
  //turn led off
  digitalWrite(led,0);
}

// the loop routine runs over and over again forever:
void loop() {
  //read !ed value from the pins
  int buttonState = !digitalRead(ban);
  int buttonState2 = !digitalRead(ban2);
  
  //if the pin 7 (ban) gets a positive value (the sensor got obstructed)
  if(buttonState){
    //checks if the sensor for pin 8 was obstructed before
    if(flag2){
      res=1; //turn led on
      flag2=0; //reset flag2
      Serial.write('1'); //sends 1, indicating to go up
      delay(200); //wait a little
    }
    else
     flag1=1; //this means the pin on this sensor was the first to be obstructed
  }
  if(buttonState2){
    //checks if the sensor for pin 7 was obstructed before
    if(flag1){
      res=0;//turn led off
      flag1=0;//reset value
      Serial.write('2'); //sends 2, indicating to go down
      delay(200);//waits for next input
    }
    else
      flag2=1;//this means the pin on this sensor was the first to be obstructed
  }
  digitalWrite(led,res);

}

