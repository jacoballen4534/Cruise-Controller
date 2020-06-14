#ifndef SPEED_CONTROL_H
#define SPEED_CONTROL_H
#include <stdbool.h>

float saturateThrottle(float throttleIn, bool *saturate);
float regulateThrottle(int isGoingOn, float cruiseSpeed, float vehicleSpeed);

#endif // SPEED_CONTROL_H