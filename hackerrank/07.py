
# h = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
h = [1, 2, 3, 4, 5]

def largest_rectangle(buildings):
    """
    heights_stack = []
    positions_stack = []
    maximum_area
    size = height_from_stack_bigger_than_current * (current_position - position_of_maximum_stack_height
    """
    heights_stack = []
    positions_stack = []
    position = 0
    while position < len(buildings):
        building = buildings[position]
        if heights_stack == 0 or building > heights_stack[len(heights_stack) - 1]:
            heights_stack.append(building)
            positions_stack.append(position)
        else:
            if building < heights_stack[(heights_stack) - 1]:
                pass
        position += 1

