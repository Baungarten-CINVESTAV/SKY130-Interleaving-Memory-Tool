"type(var)"
import sys
import math
from colorama import Fore, Back, Style


from Python_scripts.Folder_Src_generator import *
from Python_scripts.placement_generator import *
from Python_scripts.json_generator import *
from Python_scripts.GDS_LEF_LEG_VBB_generator import *
from Python_scripts.calculate_rectangles import *
from Python_scripts.auto_1024 import *
from Python_scripts.Bidujador import *

def mensaje_error():
    print(Fore.BLUE + "If you need help, run the following command:")
    print(Fore.BLUE + "python app_mem.py --help")
    print(Style.RESET_ALL)
    sys.exit()
    
aux=sys.argv; "tipo lista"
try:
    if aux[1]=='--help':
        print(Fore.GREEN) 
        print("The correct command structure is:")
        print("python app_mem.py [mt] [wn] [ad] [p] [op1] [op2]")
        print("_____________________________________________________________________________________") 
        print("| Data | Type | Information          | Expected values                              |")
        print("|______|______|______________________|______________________________________________|")
        print("|  mt  | int  | Memory Type          | 0,1,2 corresponds to 8x1024, 32x256, 32x512  |")
        print("|      |      |                      | respectively                                 |")               
        print("|______|______|______________________|______________________________________________|")     
        print("|  wn  | int  | Data Width           | If mt=0, wn must be a multiple of 8          |")
        print("|      |      |                      | If mt=1 or mt=2, wn must be a multiple of 32 |")
        print("|      |      |                      |                                              |")  
        print("|______|______|______________________|______________________________________________|")
        print("|  ad  | int  | Number of Addresses  | Must always be a multiple of 2               |")
        print("|      |      |                      | If mt=0 the minimum value is 2048            |")
        print("|      |      |                      | If mt=1 the minimum value is 512             |")
        print("|      |      |                      | If mt=2,  the minimum value is 1024          |") 
        print("|______|______|______________________|______________________________________________|")
        print("|  p   | str  | Arrangement          | If it is 'g' it is arranged in a grid, 'r'   |")
        print("|      |      |                      | if it is arranged in a row, 'c' if it is     |")
        print("|      |      |                      | arranged in a column, 'ct' if it is arranged |")
        print("|      |      |                      | in a custom way, and 'a' is arranged automa- |")
        print("|      |      |                      | tically you can only choose if wn is 8 or 32 |")
        print("|______|______|______________________|______________________________________________|")
        print("|  opl | int  | If p=ct, op1=columns | Refers to the columns and maximum can be 10  |")
        print("|      |      |______________________|______________________________________________|")   
        print("|      |      | p=a, op1=x_space     | Refers to the size in x                      |")
        print("|______|______|______________________|______________________________________________|")
        print("|  op2 | int  | If p=ct, op1=rows    | Refers to the rows                           |")
        print("|      |      |______________________|______________________________________________|")   
        print("|      |      | p=a, op1=y_space     | Refers to the size in y                      |")
        print("|______|______|______________________|______________________________________________|")
        print(Style.RESET_ALL)              
        sys.exit()
    else:
        
        mtt=[0,1,2,3]
        t1=[8,32,32]
        t2=[1024,256,512]
        fl=0
        cl=0
        try:
            mt=int(aux[1])
            if mtt.index(mt)==2:
                mt=2
        except ValueError:
            print(Fore.RED + "mt only receives int data and can only take the values 0,1,2")
            mensaje_error()
        
        
        try:
            wn=int(aux[2])
            if wn % t1[mt]!=0:
                print(Fore.RED + "wn only receives int data and since wt ="+str(mt)+", wn must be a multiple of "+str(t1[mt]))
                mensaje_error()   
            
        except ValueError:
            print(Fore.RED + "wn only receives int data and since wt ="+str(mt)+", wn must be a multiple of"+str(t1[mt]))
            mensaje_error()
            
        try:
            ad=int(aux[3])
            if (math.log2(ad) % 1 != 0)or(ad<2*t2[mt]):
                print(Fore.RED + "ad only receives data of the int type and must be a power of 2 and since mt="+str(mt)+" the minimum value it can have is "+str(2*t2[mt]))
                mensaje_error()  
            
        except ValueError:
            print(Fore.RED + "ad only receives data of the int type and must be a power of 2 and since mt="+str(mt)+" the minimum value it can have is "+str(2*t2[mt]))
            mensaje_error()
            
        p=aux[4] 
        if p=="g":
            acom="square"
            acom2="grid"
        elif p=="r":
            acom="row"
            acom2="row"
        elif p=="c":
            acom="column"
            acom2="column"
        elif p=="ct":
            acom="custom"
            acom2="custom"
            try:
                fl=int(aux[6])
                cl=int(aux[5])
                if fl>10:
                    print(Fore.RED +"as p="+p+", op1 and op2 must be integers and op1=f1 and op2=c1, also that op1 must be less than 10")
                    mensaje_error()                   
            except ValueError:
                print(Fore.RED +"as p="+p+", op1 and op2 must be integers and op1=f1 and op2=c1, also that op1 must be less than 10")
                mensaje_error()
        elif p=="a":
            if ~((wn==8) or (wn==32))==-1:
                print(Fore.RED +"can't use auto mode as wn is not 8 or 32")
                mensaje_error()
            else:
                acom="auto"
                acom2="auto"
                try:
                    x=int(aux[5])
                    y=int(aux[6])
                except ValueError:
                    print(Fore.RED +"as p="+p+", op1 and op2 must be integers and op1=x and op2=y")
                    mensaje_error()
        else:
            print(Fore.RED + "p is of type str and can only get values of 'c', 'r', 'g', 'ct' and 'a'")
            mensaje_error()    
except IndexError:
    print(Fore.RED +"The data received by the command is not complete")
    mensaje_error()
"""__________________________________________________________________________________________"""
print("Final variables")
if acom != "auto":
    print("type = "+str(mt)+", memory of "+str(t1[mt])+"x"+str(t2[mt]))
    print("wn = "+ str(wn))
    print("ad = "+ str(ad))
if acom=="square":
    print("Arrangement = grid")
else:
    print("Arrangement = "+acom)
if acom=="custom":
    print("coordinates = ("+str(cl)+","+str(fl)+")")
elif acom=="auto":
    print("x_space="+str(x)+", y_space="+str(y))



#test variables, the system will ask for this variables
W_n = wn
Ad_n = ad
MT = mt
placement = acom


#ask for "Rows" and "Columns" just if "custom" placement was chosen
Columns = cl
Rows = fl
#ask for "x" and "y" space just if "auto" placement was chosen
#x_space = x 
#y_space = y

#This auto placement based on "x" and "y" space just work for 8 and 32 data width
if (placement == "auto" )& (MT != 0):
  Columns, Rows, Ad_n,MT  = auto_size(x,y)
  placement = "custom"
  print("type = "+str(MT)+", memory of "+str(t1[MT])+"x"+str(t2[MT]))
  print("wn = "+ str(wn))
  print(f"ad = {Ad_n}")
elif (placement == "auto") & (MT == 0):
  Columns, Rows, bytes  = auto_size_1024(x,y)
  placement = "custom"
  Ad_n = bytes
  print("type = "+str(MT)+", memory of "+str(t1[MT])+"x"+str(t2[MT]))
  print("wn = "+ str(wn))
  print(f"ad = {bytes}")

Folder_name = Src_generator(f"{W_n}", f"{Ad_n}", f"{MT}",acom2,Rows,Columns) #W_n, Ad_n, MT)
die_area = Placement_File_Generator(W_n, Ad_n,MT, placement, Rows,Columns,Folder_name) #W_n, Ad_n, MT,placement, Rows, Columns, Folder_Name
Config_File_Generator(MT, Folder_name,die_area)
Copy_macro_files(Folder_name)
draw_diagram(W_n, Ad_n, MT,Folder_name)