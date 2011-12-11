// This is an arduino skecth used to interact with a computer and a coffee pot
//  
// Date : 12/2011
// Author : Mathieu (matael) Gaborit
// License : WTFPL
//
// ---------------------------------------------------------
// Controls :
//   -> link to coffee pot => pin13
//   -> USB => Rx/Tx (handled using serial)
//   -> Control codes :
//       - [Rx] 1 => Start coffe pot
//       - [Rx] 0 => Stop coffee pot

#define COFFEE_POT 13

void setup()
{
    pinMode(COFFEE_POT, OUTPUT);
    Serial.begin(9600); // Start serial connection
}

void loop()
{
 	if (Serial.available() != 0){
        int read_out = Serial.read();
        if(read_out == 49){ // If we received a "1" (ASCII:49)
            digitalWrite(COFFEE_POT, HIGH);
            Serial.println("Starting coffee pot...");
        } else if (read_out == 48) { // If we received a "0" (ASCII:48)
            digitalWrite(COFFEE_POT, LOW);
            Serial.println("Stopping coffee pot... :'(");
        } else {
            Serial.println("Bad control code....");
        }
    } 
}
