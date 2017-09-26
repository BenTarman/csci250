#buzz function (uses half period method)

def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)

    for i in range(cycles):
        GPIO.output(buzzerPin, True)
        time.sleep(delay)
        GPIO.output(buzzerPin, False)
        time.sleep(delay)

    time.sleep(duration * 0.3)
