import math
import sys



def name_generator(W_n, Ad_n, MT):
    if MT == 0:
        SINGLE_MEM_NUM_ADDRESSES = 1024
        SINGLE_MEM_DATA_WIDTH = 8
    elif MT == 1:
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
    else:
        SINGLE_MEM_NUM_ADDRESSES = 512
        SINGLE_MEM_DATA_WIDTH = 32
        two_squre_space_x = 20
        two_squre_space_y = 10

    NUM_PARALLEL_MEMORIES = (W_n) // (SINGLE_MEM_DATA_WIDTH)
    NUM_SERIAL_MEMORIES = (Ad_n) // (SINGLE_MEM_NUM_ADDRESSES)

    vector_strings_name = []  # Empty vector

    
    #String name generator
    for i in range(NUM_SERIAL_MEMORIES):
        for j in range(NUM_PARALLEL_MEMORIES):
            if MT == 0: #8x1024 mem type
                vector_strings_name.append(f"SERIAL_MEMORY\[{i}\].PARALLEL_MEMORY\[{j}\].genblk1.genblk1.sky130_sram_1kbyte_1rw1r_8x1024_8_i")
            elif MT == 1: #32x256 mem type
                vector_strings_name.append(f"SERIAL_MEMORY\[{i}\].PARALLEL_MEMORY\[{j}\].genblk1.genblk1.sky130_sram_1kbyte_1rw1r_32x256_8_i")
            else: #32x512 mem type
                vector_strings_name.append(f"SERIAL_MEMORY\[{i}\].PARALLEL_MEMORY\[{j}\].genblk1.sky130_sram_2kbyte_1rw1r_32x512_8_i")
    return vector_strings_name

def row_placement(W_n, MT,Total_Mem):
    Num_mem_32 = 0;
    if MT == 0:
        if Total_Mem > 4:
            size_X = 495+(2*Total_Mem) #Real 446 + 35 offset //Space for conections
        else:
            size_X = 481+25 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 1024
        SINGLE_MEM_DATA_WIDTH = 8
        init_x_Offset = 50
        init_y_Offset = 50
        Num_mem_32 = 0
    elif MT == 1:
        if Total_Mem > 8:
            size_X = 495+(4*Total_Mem) #Real 446 + 35 offset //Space for conections
            Num_mem_32 = (2 * Total_Mem)
        else:
            size_X = 481+40 #Real 446 + 35 offset //Space for conections
        size_Y = 435+20 #Real 397 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
        init_x_Offset = 70
        if (W_n>=96) & ( MT != 0):
            Num_mem_32 = (5*Total_Mem)
        init_y_Offset = 85 + Num_mem_32
    else:
        Num_mem_32 = 0
        if Total_Mem > 4:
            size_X = 723+(4*Total_Mem) #Real 446 + 35 offset //Space for conections
            Num_mem_32 = (2 * Total_Mem)
        else:
            size_X = 723+25 #Real 446 + 35 offset //Space for conections
        size_Y = 541+20 #Real 397 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
        init_x_Offset = 70
        if (W_n>=96) & ( MT != 0):
            Num_mem_32 = (10*Total_Mem)
        init_y_Offset = 70 + Num_mem_32
        init_x_Offset= init_x_Offset + Num_mem_32


        

    vector_strings_coordinates = [] # Empty vector

    for Position_X in range(Total_Mem):
        vector_strings_coordinates.append(f"{(size_X*Position_X)+init_x_Offset} {init_y_Offset} N")

    return vector_strings_coordinates

def column_placement(W_n, MT, Total_Mem):
    if MT == 0:
        if Total_Mem > 4:
            size_Y = 481+(5*Total_Mem) #Real 446 + 35 offset //Space for conections
        else:
            size_Y = 481+25 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 1024
        SINGLE_MEM_DATA_WIDTH = 8
        two_squre_space_y = 40
        init_x_Offset = 50
        init_y_Offset = 50
    elif MT == 1:
        if Total_Mem > 4:
            size_Y = 481+(5*Total_Mem) #Real 446 + 35 offset //Space for conections
        else:
            size_Y = 481+25 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
        init_x_Offset = 70
        init_y_Offset = 50
    else:
        if Total_Mem > 4:
            size_Y = 481+(5*Total_Mem) #Real 446 + 35 offset //Space for conections
        else:
            size_Y = 481+25 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
        init_x_Offset = 70
        init_y_Offset = 50

    if (W_n>=24) & ( MT == 0):
        size_Y = size_Y+(2*Total_Mem)
    elif (W_n>=128) & ( MT == 2):
        size_Y = size_Y+(5*Total_Mem)
        init_x_Offset = init_x_Offset+(10*Total_Mem)
    elif (W_n>32) & ( MT != 0):
        size_Y = size_Y+(2*Total_Mem)
        init_x_Offset = init_x_Offset+(3*Total_Mem)



    vector_strings_coordinates = [] # Empty vector

    for Position_Y in range(Total_Mem):
        vector_strings_coordinates.append(f"{init_x_Offset} {(size_Y*Position_Y)+init_y_Offset} N")


    return vector_strings_coordinates

def Square_placement( MT,Total_Mem):
    if MT == 0:
        size_X = 495+25 #Real 455 + 40 offset //Space for conections
        size_Y = 481+20 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 1024
        SINGLE_MEM_DATA_WIDTH = 8
        two_squre_space_x = 20
        two_squre_space_y = 10
    elif MT == 1:
        size_X = 514+70 #Real 479 + 40 offset //Space for conections
        size_Y = 435+50 #Real 397 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
        two_squre_space_x = 20
        two_squre_space_y = 10
    else:
        size_X = 723+70 #Real 683 + 40 offset //Space for conections
        size_Y = 451+50 #Real 416 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 512
        SINGLE_MEM_DATA_WIDTH = 32
        two_squre_space_x = 20
        two_squre_space_y = 10

    init_x_Offset_param = 50
    init_y_Offset = 50

    if (Total_Mem>=24) & ( MT == 0):
        size_Y = size_Y+(2*Total_Mem)
        size_X = size_X+(2*Total_Mem)
        two_squre_space_x = two_squre_space_x*2
        two_squre_space_y = two_squre_space_y*2

    elif (Total_Mem>=24) & ( MT == 1):
        size_Y = size_Y+(2*Total_Mem)
        size_X = size_X+(2*Total_Mem)


    elif (Total_Mem>=24) & ( MT == 2):
        size_Y = size_Y+(3*Total_Mem)
        size_X = size_X+(3*Total_Mem)
        init_x_Offset_param = 110
        init_y_Offset = 110

    elif (Total_Mem>=12) & ( MT == 2):
        size_Y = size_Y+(3*Total_Mem)
        size_X = size_X+(3*Total_Mem)
        init_x_Offset_param = 80
        init_y_Offset = 80




    vector_strings_coordinates = [] # Empty vector
 
    Rows_and_Colums = math.ceil(Total_Mem ** 0.5)
    
    for Position_Y in range(Rows_and_Colums):
        init_x_Offset = init_x_Offset_param
        if Position_Y % 2 != 0 or Position_Y==0:
            Curret_position_Y = (size_Y*Position_Y)+init_y_Offset
        else:
            init_y_Offset = init_y_Offset + two_squre_space_y
            Curret_position_Y = (size_Y*Position_Y)+init_y_Offset

        for Position_X in range(Rows_and_Colums):
            if Position_X % 2 != 0 or Position_X==0:
                Curret_position_X =(size_X*Position_X)+init_x_Offset
            else:
                init_x_Offset = init_x_Offset + two_squre_space_x
                Curret_position_X =(size_X*Position_X)+init_x_Offset

            if(Total_Mem>=96) & ( MT != 0) & ((math.floor(Rows_and_Colums/2)==Position_X) or(math.ceil(Rows_and_Colums/2)==Position_X)):
                print(Position_X)
            vector_strings_coordinates.append(f"{Curret_position_X} {Curret_position_Y} N")

            
    return vector_strings_coordinates

def Custom_placement( W_n,MT, Rows, Columns,Total_Mem):
    if MT == 0:
        size_X = 495+25 #Real 455 + 40 offset //Space for conections
        size_Y = 481+20 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 1024
        SINGLE_MEM_DATA_WIDTH = 8
        two_squre_space_x = 20
        two_squre_space_y = 10
    elif MT == 1:
        size_X = 514+25 #Real 479 + 40 offset //Space for conections
        size_Y = 435+20 #Real 397 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
        two_squre_space_x = 20
        two_squre_space_y = 10
    else:
        size_X = 723+35 #Real 683 + 40 offset //Space for conections
        size_Y = 451+20 #Real 416 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 512
        SINGLE_MEM_DATA_WIDTH = 32
        two_squre_space_x = 20
        two_squre_space_y = 10

    init_x_Offset_param = 50
    init_y_Offset = 50
    if (Total_Mem>=24) & ( MT == 0):
        #size_Y_aux = size_Y+(15*Rows)
        
        size_X_aux = size_X+(6*Columns)
        if((size_X_aux>size_X+80) or (Rows>6)):
            size_Y = size_Y+80
            size_X = size_X + 80
        else:
            size_X = size_X_aux

    
    elif (Total_Mem>=12) & ( MT == 2):
        size_Y = size_Y+(3*Total_Mem)+70
        size_X = size_X+(3*Total_Mem)+50
        init_x_Offset_param = 80
        init_y_Offset = 80
        if (Total_Mem>31):
            init_y_Offset= init_y_Offset+50
            init_x_Offset_param = init_x_Offset_param+50
        if (Total_Mem>=16):
            init_y_Offset= init_y_Offset+35

    elif (Total_Mem>=16) & ( MT != 0) & (W_n>=128):
        size_Y = size_Y+80
        size_X = size_X+100
        two_squre_space_x = Total_Mem*2

    elif (Total_Mem>=24) & ( MT != 0) & (W_n>=64):
        size_Y = size_Y+80
        size_X = size_X+80

    elif ( MT != 0) & (W_n>=64):
        size_Y = size_Y+40
        size_X = size_X+50
        two_squre_space_x = Total_Mem*2

    if(((Rows/4)>  Columns)&(W_n>=64)): #Added tio harden 128x1024 with rows = 10 and columns =2 
        init_x_Offset_param = 80

    
    vector_strings_coordinates = [] # Empty vector

    for Position_Y in range(Rows):
        init_x_Offset = init_x_Offset_param
        
        if Position_Y % 2 != 0 or Position_Y==0:
            Curret_position_Y = (size_Y*Position_Y)+init_y_Offset
        else:
            init_y_Offset = init_y_Offset + two_squre_space_y
            Curret_position_Y = (size_Y*Position_Y)+init_y_Offset

        for Position_X in range(Columns):
            if Position_X % 2 != 0 or Position_X==0:
                Curret_position_X =(size_X*Position_X)+init_x_Offset
                vector_strings_coordinates.append(f"{Curret_position_X} {Curret_position_Y} N")
            else:
                init_x_Offset = init_x_Offset + two_squre_space_x
                Curret_position_X =(size_X*Position_X)+init_x_Offset
                vector_strings_coordinates.append(f"{Curret_position_X} {Curret_position_Y} N")
    """for Position_Y in range(Rows):
        for Position_X in range(Columns):
            vector_strings_coordinates.append(f"{(size_X*Position_X)+init_x_Offser} {(size_Y*Position_Y)+init_y_Offser} N")"""
    return vector_strings_coordinates
#####       Main


def Placement_File_Generator(W_n, Ad_n, MT,placement, Rows, Columns, Folder_Name):
    if MT == 0:
        size_X = 495+50 #Real 455 + 40 offset //Space for conections
        size_Y = 481+50 #Real 446 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 1024
        SINGLE_MEM_DATA_WIDTH = 8
    elif MT == 1:
        size_X = 514+70 #Real 479 + 40 offset //Space for conections
        size_Y = 435+50 #Real 397 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 256
        SINGLE_MEM_DATA_WIDTH = 32
    else:
        size_X = 723+35 #Real 683 + 40 offset //Space for conections
        size_Y = 451+20 #Real 416 + 35 offset //Space for conections
        SINGLE_MEM_NUM_ADDRESSES = 512
        SINGLE_MEM_DATA_WIDTH = 32

    vector_name = []  # Empty vector
    vector_strings_coordinates = [] # Empty vector
    
    if ((Ad_n) // (SINGLE_MEM_NUM_ADDRESSES)) == 0:
        Num_p_mem = 1
    else:
        Num_p_mem = ((Ad_n) // (SINGLE_MEM_NUM_ADDRESSES))

    Total_Mem = ((W_n) // (SINGLE_MEM_DATA_WIDTH)) * Num_p_mem

    vector_name = name_generator(W_n, Ad_n, MT)
    if placement == "square":
        vector_strings_coordinates = Square_placement( MT,Total_Mem)
    elif placement == "row":
        vector_strings_coordinates = row_placement(W_n,MT,Total_Mem)
    elif placement == "column":
        vector_strings_coordinates = column_placement(W_n, MT,Total_Mem)
    elif placement == "custom":
        if Columns*Rows < Total_Mem:
            # Display an error message and abort the execution
            print("\033[91m The number of memory blocks required exceeds the defined number of rows and columns. \033[0m")
            sys.exit(1)  # Exit with exit code 1
        elif Columns*Rows != Total_Mem:
            print("\033[93m The number of memory blocks required does not align with the defined number of rows and columns. In order to accommodate the memory blocks, they will be placed prioritizing the row configuration. \033[0m");
        
        #Rows and colums function has better area utilziation than custom functions around memtype 2
        if((MT==2 )& (Rows==1)): 
            vector_strings_coordinates = row_placement(W_n,MT,Total_Mem)
        elif((MT==2 )& (Columns==1)):
            vector_strings_coordinates = column_placement(W_n, MT,Total_Mem)
            print("COlum funciton")
        else:
            vector_strings_coordinates = Custom_placement(W_n,MT,Rows,Columns,Total_Mem)


    file_path = f"designs/{Folder_Name}/macro.cfg"
    ###### Print the Die Area ###########
    X_num = 0 #Used to store the largest number
    Y_num = 0 #Used to store the largest number
    numbers = [] #Used to store the largest number
    with open(file_path, "w") as file:
        for i in range(Total_Mem):
            file.write(f"{vector_name[i]} {vector_strings_coordinates[i]}\n")
            numbers = vector_strings_coordinates[i].split()[:2]
            numbers = [int(num) for num in numbers] 
            if numbers[0] > X_num:
                X_num = numbers[0]
            if numbers[1] > Y_num:
                Y_num = numbers[1]
            
    die_area = f"0 0 {X_num+size_X} {Y_num+size_Y}"
    return die_area




#Placement_File_Generator(64, 2048,1, "square", 2,2,"SRAM_X_X")

