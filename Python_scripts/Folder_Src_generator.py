import os
import shutil
import sys

#imput_parametros = ["8", "4096", "0"]

def imput_parametros():
    W_n = sys.argv[1]
    Ad_n = sys.argv[2]
    MT = sys.argv[3]
    return W_n, Ad_n, MT

# Realizar cambio de extensión de archivo, para edición de parámetros
def cambio_extension(directorio): 
    archivo_txt = None
    archivos = os.listdir(directorio)
    for archivo in archivos:
        if archivo == objetivo:
            archivo_v = os.path.join(directorio,objetivo)
            #print(archivo_v)
            archivo_txt = os.path.join(directorio,editable+".txt" )
            #print(archivo_txt)
            shutil.copy(archivo_v,archivo_txt)
            return archivo_txt
    return archivo_txt

# Funcion para cambiar solo un parámetro
def editar_parametros (ruta_editable,letra,parametro):
    archivo_txt = open(ruta_editable, 'r')
    contenido_archivo = archivo_txt.read()
    cambio_parametros = contenido_archivo.replace(letra,parametro)
    archivo_txt = open(ruta_editable, 'w')
    archivo_txt.write(cambio_parametros)
    #print("Se aignó el parámetro " + parametro)
    archivo_txt.close()
    return archivo_txt




def Src_generator(W_n, Ad_n, MT,placement,Rows,Columns):
    directorio = os.getcwd()
    directorio = f"{directorio}/Python_scripts"
    directorio_r = f"{directorio}/../designs" #acceder a directorios anterioes 
    global objetivo
    global editable
    global subdirectorios
    objetivo = "memory_generator_python.v"
    editable = "memory_generator_sky130"
    subdirectorios = ["designs","scripts"]

    Size_type = placement
    if MT == "AUTO" or MT == "auto" or MT == "Auto":
        MT = "2" #Agregar condicional para entrada auto
        Size_type =  "auto"
    

    #W_n = "8"
    #Ad_n = "4092"
    #MT = "0"

    x = "W_n"
    y = "Ad_n"
    z = "MT"

    # Función para hacer el cambio de todos los parámetros, generar archivo.v y asignarlo en la carpeta correspondinte

    ruta_editable = cambio_extension(directorio)
    editar_parametros(ruta_editable,x,W_n)
    editar_parametros(ruta_editable,y,Ad_n)
    editar_parametros(ruta_editable,z,MT)
    cambio_ruta = os.path.splitext(ruta_editable)
    ruta_final = editable + "_" + W_n + "_" + Ad_n + "_" + MT + ".v"
    os.rename(ruta_editable,ruta_final)
    #Create the folder with size information
    if MT == "AUTO" or MT == "auto" or MT == "Auto":
        sram = "SRAM_" + W_n + "_" + Ad_n + "_" + MT + "_" + Size_type + "_" + Rows + "_" + Columns 
    else:
        sram = "SRAM_" + W_n + "_" + Ad_n + "_" + MT + "_" + Size_type 
    
    src = "src"
    carpetas = os.path.join(directorio_r,sram,src)
    if os.path.exists(f"{directorio_r}/{sram}"):
        shutil.rmtree(f"{directorio_r}/{sram}")
    ruta_carpetas = os.makedirs(carpetas, exist_ok=True)
    archivo_origen = ruta_final
    archivo_destino = carpetas
    shutil.move(archivo_origen,archivo_destino)

    Folder_name = sram

    #re_escritura()
    return Folder_name

#Src_generator("8", "4096", "0")