import json

def Config_File_Generator(MT, Folder_Name,Die_area):

    if MT == 0:
        Mem_Name = "sky130_sram_1kbyte_1rw1r_8x1024_8"
        inst_Name = "sky130_sram_1kbyte_1rw1r_8x1024_8_i"
        Lib_name = "sky130_sram_1kbyte_1rw1r_8x1024_8_TT_1p8V_25C"
    elif MT == 1:
        Mem_Name = "sky130_sram_1kbyte_1rw1r_32x256_8"
        inst_Name = "sky130_sram_1kbyte_1rw1r_32x256_8_i"
        Lib_name = "sky130_sram_1kbyte_1rw1r_32x256_8_TT_1p8V_25C"
    else:
        Mem_Name = "sky130_sram_2kbyte_1rw1r_32x512_8"
        inst_Name = "sky130_sram_2kbyte_1rw1r_32x512_8_i"
        Lib_name = "sky130_sram_2kbyte_1rw1r_32x512_8_TT_1p8V_25C"

    with open('Python_scripts/config_python_script.json') as f:
        archivo_json = json.load(f)

    "print(type(archivo_json))"
    file_path = f"designs/{Folder_Name}/config.json"

    archivo_json['DESIGN_NAME']='memory_generator_sky130'
    archivo_json['VERILOG_FILES_BLACKBOX']= f"dir::V_BB/{Mem_Name}.v"
    archivo_json['EXTRA_LEFS']= f"dir::LEF/{Mem_Name}.lef"
    archivo_json['EXTRA_GDS_FILES']= f"dir::GDS/{Mem_Name}.gds"
    archivo_json['EXTRA_LIBS']= f"dir::LIB/{Lib_name}.lib"
    archivo_json['FP_PDN_MACRO_HOOKS']= f"SERIAL_MEMORY.*{inst_Name} vccd1 vssd1 vccd1 vssd1"
    archivo_json['DIE_AREA']= f"{Die_area}"
    
    if(MT == 2):
        archivo_json['PL_RANDOM_INITIAL_PLACEMENT']= f"1"
    

    with open(file_path, "w") as new_file:
        # Write the JSON data to the file
        json.dump(archivo_json, new_file, indent=4)

    return

#Config_File_Generator(1,"SRAM_X_X","0 0 200 200")
