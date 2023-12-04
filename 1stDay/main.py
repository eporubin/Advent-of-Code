
def calibrationSum():
    f = open("input.txt", "r")
    result = 0
    for line in f.readlines():
        numbers = line[:-1]
        numbers = [int(char) for char in line.strip() if char.isdigit()]
        calibration_value = [numbers[0], numbers[-1]]
        digits = 10 * calibration_value[0] + calibration_value[-1]
        result += digits

    print(result)
    f.close()

calibrationSum()
