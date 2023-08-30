import svgwrite
import cairosvg
import xml.dom.minidom
import random
import time
import math
import shutil
import os

def prettify_svg(svg_content):
    dom = xml.dom.minidom.parseString(svg_content)
    return dom.toprettyxml()

def draw_diagram(W_n, A_dn, MT, Folder_name, square_size=100):
    # Check MT base values
    current_directory = os.getcwd()
    destination_path = f'{current_directory}/designs/{Folder_name}/'

    if MT == 0:
        single_num_addresses = 1024
        single_data_width = 8
    elif MT==1:
        single_num_addresses = 256
        single_data_width = 32
    else:
        single_num_addresses = 512
        single_data_width = 32
    # Check if W_n and A_dn is a valid multiple of MT
    assert(W_n % single_data_width == 0)
    assert(A_dn % single_num_addresses == 0)
    # Print the current parameters
    # Get total number of parallel and serial memories
    NUM_PARALLEL_MEMORIES = int(W_n / single_data_width)
    NUM_SERIAL_MEMORIES = int(A_dn / single_num_addresses)
    print(f"Generated Memory = {W_n}x{A_dn} \n Parallel: {NUM_PARALLEL_MEMORIES} Serial: {NUM_SERIAL_MEMORIES} Total: {NUM_PARALLEL_MEMORIES*NUM_SERIAL_MEMORIES}")
    # Define SVG color, line and values for several blocks
    rectangle_color = svgwrite.rgb(255,255,255)
    rectangle_pen_color = svgwrite.rgb(0,0,0)
    rectangle_pen_width = 1
    data_color = svgwrite.rgb(0,0,255)
    address_color = svgwrite.rgb(30,255,30)
    # Define variables used through the code
    line_spacing = 2
    line_width = 1
    mid_sep = line_spacing / 2
    bottom_offset = square_size
    mux_separation = 100
    mux_width = 50
    right_offset = mux_width + square_size
    vertical_spacing = (line_spacing-line_width)  * NUM_SERIAL_MEMORIES + line_width * NUM_SERIAL_MEMORIES + mid_sep
    horizontal_spacing = vertical_spacing
    font_size = square_size / 5
    title_font_size = font_size 
    svg_height = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing) + bottom_offset + title_font_size
    svg_width = NUM_SERIAL_MEMORIES * (square_size + horizontal_spacing) - horizontal_spacing + mux_separation + right_offset
    # Create the canvas
    dwg = svgwrite.Drawing(size=(svg_width, svg_height))  
    # Draw a black background rectangle
    dwg.add(dwg.rect(insert=(0, 0), size=(svg_width, svg_height), fill="white")) 
    # Draw the green squares and lines of each square
    for row in range(NUM_PARALLEL_MEMORIES):
        for col in range(NUM_SERIAL_MEMORIES):
            x = col * (square_size + horizontal_spacing)
            y = row * (square_size + vertical_spacing)
            # Draw vertical lines on squares south
            line_x = x + (square_size / 2)       
            line_y1 = y + square_size
            line_y2 = y + square_size + mid_sep * (col + 1 ) + mid_sep * col + line_width
            dwg.add(dwg.line(start=(line_x, line_y1), end=(line_x, line_y2), stroke=address_color, stroke_width=line_width, stroke_linecap="round"))
            # Draw horizontal lines from each square's east
            hor_line_start_x = x + square_size 
            hor_line_start_y = y + (square_size / 2)
            hor_line_end_x = x + square_size + (horizontal_spacing / 2)
            hor_line_end_y = y + (square_size / 2)
            dwg.add(dwg.line(start=(hor_line_start_x, hor_line_start_y), end=(hor_line_end_x, hor_line_end_y), stroke=data_color, stroke_width=line_width, stroke_linecap="round"))
            # Draw Rectangle
            dwg.add(dwg.rect(insert=(x, y), size=(square_size, square_size), fill=rectangle_color, stroke= rectangle_pen_color, stroke_width=rectangle_pen_width))
            text = f'{single_data_width}x{single_num_addresses}'
            text_width = ((len(text) * (font_size * 0.6)) / 2) / 2
            dwg.add(dwg.text(text, insert=(x+text_width, y+font_size/2+square_size/2), fill="black", font_size=f"{font_size}px"))
    # Draw vertical connections per column
    for col in range(NUM_SERIAL_MEMORIES):  
        init = 0
        start_x = (col) * (square_size + horizontal_spacing) + square_size + horizontal_spacing / 2 
        start_y = init + square_size / 2
        end_x = (col) * (square_size + horizontal_spacing) + square_size + horizontal_spacing / 2
        end_y = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing) + bottom_offset
        #print(f"Drawing vertical line from ({start_x}, {start_y}) to ({end_x}, {end_y})")
        dwg.add(dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke=data_color, stroke_width=line_width, stroke_linecap="round"))
    # Draw horizontal connections per row
    for col in range(NUM_SERIAL_MEMORIES):
        for row in range(NUM_PARALLEL_MEMORIES):  
            init = 0
            start_x = init + ((square_size) * col) + square_size / 2 + horizontal_spacing * col 
            start_y = (row) * (square_size + vertical_spacing) + square_size + line_spacing * col + mid_sep + line_width #+ vertical_spacing / 2 
            end_x = NUM_SERIAL_MEMORIES * (square_size + horizontal_spacing) - horizontal_spacing + mux_separation
            end_y = (row) * (square_size + vertical_spacing) + square_size + line_spacing * col  + mid_sep + line_width#+ vertical_spacing / 2
            #print(f"Drawing horizontal line from ({start_x}, {start_y}) to ({end_x}, {end_y})")
            dwg.add(dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke=address_color, stroke_width=line_width, stroke_linecap="round"))
    # Calculate values for MUX and last lines
    x_pos = NUM_SERIAL_MEMORIES * (square_size + horizontal_spacing) - horizontal_spacing + mux_separation
    y_pos = 1 * (square_size) / 2
    mux_height = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing) - square_size / 2
    tilt = 25
    # Draw last Vertical connection
    init = 0
    start_x = NUM_SERIAL_MEMORIES * (square_size + horizontal_spacing) - horizontal_spacing + mux_separation + mux_width / 2
    start_y = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing) + bottom_offset 
    end_x = NUM_SERIAL_MEMORIES * (square_size + horizontal_spacing) - horizontal_spacing + mux_separation + mux_width / 2
    end_y = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing) 
    dwg.add(dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke=data_color, stroke_width=line_width, stroke_linecap="round"))
    # Draw Line going out from MUX
    start_x = x_pos + mux_width
    start_y = y_pos + mux_height / 2
    end_x = x_pos + right_offset
    end_y = y_pos + mux_height / 2
    dwg.add(dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke=address_color, stroke_width=line_width, stroke_linecap="round"))
    dwg.add(dwg.text(f'DATA: {W_n}', insert=(start_x, start_y  - line_width), fill="black", font_size=f"{font_size}px"))
    # Calculate the points for the MUX
    points = [
        (x_pos + mux_width, y_pos + tilt), #B
        (x_pos + mux_width, y_pos + mux_height), #D
        (x_pos , y_pos + mux_height + tilt), # C
        (x_pos , y_pos ) # A
    ]
    dwg.add(dwg.polygon(points, fill=rectangle_color, stroke = rectangle_pen_color, stroke_width = rectangle_pen_width))
    # Draw last Horizontal connection
    init = 0
    start_x = 0 # square_size + horizontal_spacing / 2
    start_y = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing)  + bottom_offset 
    end_x = NUM_SERIAL_MEMORIES * (square_size + horizontal_spacing) - horizontal_spacing + mux_separation + mux_width / 2
    end_y = NUM_PARALLEL_MEMORIES * (square_size + vertical_spacing)  + bottom_offset
    dwg.add(dwg.line(start=(start_x, start_y), end=(end_x, end_y), stroke=data_color, stroke_width=line_width, stroke_linecap="round"))
    dwg.add(dwg.text(f'ADDR: {math.ceil(math.log2(A_dn))}', insert=(0, start_y - line_width), fill="black", font_size=f"{title_font_size}px"))
    # Draw the total NxM memory
    dwg.add(dwg.text(f'{W_n}x{A_dn}', insert=(0, svg_height), fill="black", font_size=f"{title_font_size}px"))

    # Create the svg string content
    svg_content = dwg.tostring()
    prettified_svg = prettify_svg(svg_content)
    name = destination_path+f"{W_n}x{A_dn}-MT-{single_data_width}x{single_num_addresses}"
    # Save the svg
    with open(name  + ".svg", "w") as f:
        f.write(prettified_svg)
    # Convert the png if possible
    try:
        cairosvg.svg2png(url=f'{name}.svg', write_to=f'{name}.png')
    except Exception as e:
        print(f"TOO LARGE TO CONVERT TO PNG! {e}")
    else:
        print(f"Conversion to png correct.")
    #Finish
    print(f"Finished!")

def test_function(iter= 1):
    for i in range(iter):
        MT = random.randint(0,1)
        W_n_random_value = random.randint(2,12)
        A_dn_random_value = random.randint(2,12)

        if MT == 0:
            single_num_addresses = 1024
            single_data_width = 8
        elif MT==1:
            single_num_addresses = 256
            single_data_width = 32
        else:
            single_num_addresses = 512
            single_data_width = 32
        W_n = single_data_width * W_n_random_value
        A_dn = single_num_addresses * A_dn_random_value

        print(f"TESTING FOR: DataWidth: {W_n} AddressWidth: {A_dn} MT: {MT}")
        draw_diagram(W_n, A_dn, MT)
        time.sleep(2)
    exit()

if __name__ == "__main__":
    #test_function(1)
    W_n = int(input("Enter the number of Parallel Memories (W_n): "))
    A_dn = int(input("Enter the number of Serial (A_dn): "))
    MT = int(input("Enter the Memory type (MT): "))
    draw_diagram(W_n=W_n, A_dn=A_dn, MT=MT)

    