
// https://www.arduino.cc/en/Reference/Wire
#include <Wire.h>

// https://github.com/NorthernWidget/DS3231
#include <DS3231.h>

DS3231 Clock;
bool Century=false;
bool h12;
bool PM;
byte ADay, AHour, AMinute, ASecond, ABits;
bool ADy, A12h, Apm;

enum DOWS {
  LUNDI=1,
  MARDI,
  MERCREDI,
  JEUDI,
  VENDREDI,
  SAMEDI,
  DIMANCHE
};

// Define Pins
#define GREEN 3
#define YELLOW 5
#define RED 6

void flash_led(int pin, int mydelay=500)
{
  digitalWrite(pin, HIGH);
  delay(mydelay);
  digitalWrite(pin, LOW);
  delay(mydelay);
}

void flash_number(int number)
{
  int number_1 = number / 10;
  int number_2 = number % 10;

  for ( int i=0 ; i<number_1 ; ++i )
    flash_led(RED);
  
  for ( int i=0 ; i<number_2 ; ++i )
    flash_led(YELLOW);

  // Ack
  flash_led(GREEN, 1500);
}

void setup()
{
  Serial.begin(9600);
  Serial.println("Initialize DS3231");
  Wire.begin();

  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(13, OUTPUT);
  
  digitalWrite(RED, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(13, LOW);

  int hour = Clock.getHour(h12, PM);
  int minute = Clock.getMinute();
  
  Serial.println(hour, DEC); //24-hr
  Serial.println(minute, DEC);
  Serial.println(Clock.getSecond(), DEC);
  Serial.println(Clock.getDoW(), DEC);

  // Start flash
  flash_led(GREEN, 1500);
  flash_number(hour);
  flash_number(minute);
}

void loop()
{
  int current_hour   = Clock.getHour(h12, PM);
  int current_minute = Clock.getMinute();
  int dow = Clock.getDoW();
  int pinColor = RED;

  switch (dow)
  {
    case LUNDI:
    case MARDI:
    case JEUDI:
    case VENDREDI:
    {
      // Orange : 7h00 - 7h15
      if ( current_hour == 7 && current_minute < 15 )
        pinColor = YELLOW;
      // Green 7h15 - 10h00
      else if ( ( current_hour == 7 && current_minute >= 15 ) || current_hour == 8 || current_hour == 9 || current_hour == 10 )
        pinColor = GREEN;
      break;
    }

    case MERCREDI:
    case SAMEDI:
    case DIMANCHE:
    default:
    {
      // Orange : 8h00 - 8h30
      if ( current_hour == 8 && current_minute < 30 )
        pinColor = YELLOW;
      // Green 8h30 - 10h00
      else if ( ( current_hour == 8 && current_minute >= 30 ) || current_hour == 9 || current_hour == 10 )
        pinColor = GREEN;
      break;      
    }
        
  }

  digitalWrite(RED, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(pinColor, HIGH);
  delay(1000);
}
