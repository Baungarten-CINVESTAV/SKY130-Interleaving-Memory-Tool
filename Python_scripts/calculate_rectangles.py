def calculate_rectangles(size):
    rectangles = [
        (500, 500, 1024),
        (530, 350, 1024),
        (730, 470, 2048)
    ]
    
    rectangles.sort(key=lambda x: x[2], reverse=True)
    
    max_score = 0
    best_rectangle = None
    best_num_rectangles = 0
    
    for rectangle in rectangles:
        if rectangle[0] <= size[0] and rectangle[1] <= size[1]:
            num_rectangles = (size[0] // rectangle[0]) * (size[1] // rectangle[1])
            score = num_rectangles * rectangle[2]
            if score > max_score:
                max_score = score
                best_rectangle = rectangle
                best_num_rectangles = num_rectangles
    
    if best_rectangle is None:
        return None
    
    num_rows = size[1] // best_rectangle[1]
    num_columns = size[0] // best_rectangle[0]
    
    if best_rectangle[2] == 2048:
     score = best_num_rectangles * 512
    else:
     score = best_num_rectangles * 256
    
    coordinates = []
    for i in range(num_columns):
        for j in range(num_rows):
            x = i * best_rectangle[0]
            y = j * best_rectangle[1]
            coordinates.append((x, y))
    
    return best_rectangle, best_num_rectangles, num_columns, num_rows, score, coordinates



def auto_size(x_space, y_space):
    size = (x_space, y_space)  # Specify the size you want to maximize the score for
    result = calculate_rectangles(size)
    
    if result is not None:
        best_rectangle, num_rectangles, num_rows, num_columns, score, coordinates = result
        print(f"Number of Rows: {num_rows}")
        print(f"Number of Columns: {num_columns}")
        """print(f"Number of Rectangles: {num_rectangles}")
        print(f"Score: {score}")
        print(f"Best Rectangle: {best_rectangle[0]}x{best_rectangle[1]} with score {best_rectangle[2]}")
        print("Coordinates:")"""
        for coordinate in coordinates:
            """print(coordinate)"""
    else:
        print(f"No valid rectangle found for size {size}.")

    if best_rectangle[0] > 700:
        MT = 2
    else:
        MT = 1

    num_columns = result[2]
    num_rows = result[3]
    num_addr = result[4]
    return num_columns, num_rows, num_addr, MT