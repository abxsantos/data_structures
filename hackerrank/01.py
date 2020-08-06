input_array = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

def hourglassSum(input_array):
    row = 0
    hourglass_sum = []
    while row < len(input_array[row])-2:
        column = 0
        while column < len(input_array[column])-2:
            first_value = input_array[row][column:column+3]
            second_value = input_array[row+1][column+1:column+2]
            third_value = input_array[row+2][column:column+3]
            hourglass_sum.append(sum(first_value)+sum(second_value)+sum(third_value))
            column = column + 1
        row = row + 1
    return max(hourglass_sum)
