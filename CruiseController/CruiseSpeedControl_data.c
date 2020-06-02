float limitSpeed(float speed)
{
    static const float SPEED_MAX = 150.0;
    static const float SPEED_MIN = 30.0;
    if (speed > SPEED_MAX)
    {
        return SPEED_MAX;
    }

    if (speed < SPEED_MIN)
    {
        return SPEED_MIN;
    }

    return speed;
}