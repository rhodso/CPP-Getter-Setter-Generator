//Source file auto-generated using CPP-Getter-Setter-Generator

//Includes
#include <testClass.h>

//Constructor and Destructor
testClass::testClass(){}
testClass::~testClass(){}

//Overloaded constructors
testClass::testClass(float _x){
	x = _x;
}
testClass::testClass(float _x, float _y){
	x = _x;
	y = _y;
}
testClass::testClass(float _x, float _y, float _z){
	x = _x;
	y = _y;
	z = _z;
}

//Getters and Setters
float testClass::getX(){ return x; }
float testClass::getY(){ return y; }
float testClass::getZ(){ return z; }

void testClass::setX( float _x){ x = _x; }
void testClass::setY( float _y){ y = _y; }
void testClass::setZ( float _z){ z = _z; }

//Other methods
void testClass::doSomething(){}
float testClass::doSomethingElse(){}
