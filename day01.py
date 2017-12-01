import sys

def get_input_filename(day, test):
    return "day" + str(day).zfill(2) + ".input"

def get_output_filename(day, test):
    return "day" + str(day).zfill(2) + "." + str(test).zfill(2) + ".output"

def process(raw_input):
    return calculate_sum_of_neighbors(parseInput(raw_input))

def calculate_sum_of_neighbors(input_list):
    sum = 0
    for pos, current in enumerate(input_list):
        if current == get_distant_digit(input_list, pos, int(len(input_list)/2)):
            sum += current
        last = current
    return sum

def calculate_sum_of_digits(input_list, distance):
    sum = 0

def get_distant_digit(intput_list, pos, distance):
    otherPos = (pos+distance) % (len(intput_list))
    return intput_list[otherPos]

def parseInput(raw_input):
    return [int(char) for char in list(raw_input)]

if __name__ == "__main__":
    day = 1
    test = 2

    with open(get_input_filename(day, test)) as input_file:
        raw_input = input_file.readlines()[0]

    result = process(raw_input)
    print(result)

    with open(get_output_filename(day, test), 'w') as output_file:
        output_file.write(str(result))
