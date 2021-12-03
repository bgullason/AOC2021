# Advent Of Code 2021
# Ben Gullason
# https://github.com/bgullason



# --- Day 3: Binary Diagnostic ---



from csv import reader

# Set these two variables to enable test mode and set the file path
test_mode = False
day_number = 3


data = []
file_identifier = 'Input'


# Read from the csv file that contains the data to be processed
if test_mode: 
    file_identifier = 'Test' 
with open(f'Day{day_number}\{file_identifier}.csv', 'r', encoding='utf-8-sig') as csv_data:
    csv_reader = reader(csv_data)
    for row in csv_reader:
        data.append(row[0])



# get gamma_rate
gamma_rate = ''
index = 0
while index < len(data[0]):
    one_count = 0
    zero_count = 0
    for line in data:
        if int(line[index]): one_count += 1
        else: zero_count += 1
    gamma_rate += '1' if one_count > zero_count else '0'
    index += 1

# get epsilon_rate
epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

# get power_consumption
power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

# Output results
print(f'\nGamma Rate: {gamma_rate} = {int(gamma_rate, 2)}')
print(f'Epsilon Rate: {epsilon_rate} = {int(epsilon_rate, 2)}')
print(f'Power Consumption: {power_consumption}\n')