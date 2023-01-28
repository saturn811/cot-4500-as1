#Assignment 1
#Kendrick Dawkins

#Question 1
def get_mantissa(mantissa):
    iteration_counter = 1
    sum_variable = 0
    for item in mantissa:
        sum_variable += int(item) * ((0.5)**iteration_counter)
        iteration_counter += 1

    sum_variable += 1
    return sum_variable

def get_exponent(exponent):
    iteration_counter = 10
    sum_variable = 0
    for item in exponent:
        sum_variable += int(item) * (2**iteration_counter)
        iteration_counter -= 1

    sum_variable -= 1023
    return sum_variable

#Normalized format
def normalize(number):
    decimals = str(number).find(".")
    if number > 0:
        normalized_decimal = number / 10**decimals
    else:
        normalized_decimal = number / 10**(decimals-1)

    return normalized_decimal

#Question 2
def chopping(number, k):
    if number > 0:
        chopped_decimal = str(number)[:k+2]
    else:
        chopped_decimal = str(number)[:k+3]

    print(chopped_decimal)

#Question 3
def rounding(number, k):
    rounding_number = 5 / 10**(k+1)  
    rounded_number = number + rounding_number
    rounded_number = chopping(rounded_number, k)



#Question 4
z = normalize(491.5625) 
absolute_error = abs(z - 0.492) 
relative_error = absolute_error / z





s = 0
exponent = "10000000111"
mantissa = "111010111001"

exponent_degree = get_exponent(exponent)

mantissa_value = get_mantissa(mantissa)

final_result = (-1)**s * (2**exponent_degree) * (mantissa_value)
print(final_result)

normalized_format = normalize(final_result)
chopping(normalized_format, 3)
rounding(normalized_format, 3)
print(absolute_error)
print(relative_error)