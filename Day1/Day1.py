from csv import reader



# open file in read mode
with open('Day1/Day1_Input.csv', 'r', encoding='utf-8-sig') as read_Day1_Input:
    csvreader = reader(read_Day1_Input)
    
    count = 0
    previous = 0
    current = 0
    first = True
    
    for row in csvreader:
        current = int(row[0])
        if first:
            row = f'{row} - No Previous Data'
            first = False
        else:
            if current > previous:
                count = count + 1
                row = f'{row} - Increased'
            else:
                row = f'{row} - Decreased'
        print(row)
        previous = current

    print(f'Total Increases: {count}')