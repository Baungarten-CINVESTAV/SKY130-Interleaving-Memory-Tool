# SKY130-Interleaving-Memory-Tool
The SKY130 Process Design Kit (PDK) comes with a limited set of SRAM memory configurations, only offering three preset memory sizes: 8×1024, 32×256, and 32×512. This is problematic for designers needing different memory attributes, forcing them to either construct a full memory design from the ground up or utilize interleaving methods with the provided memory setups. 

In response to this challenge, we introduce an innovative system that automates the creation of varied memory arrays using custom floorplans, capitalizing on the interleaving memory idea. This system lets designers produce diverse memory sizes and arrangements by mixing and interleaving the current SKY130 PDK memories.

With our system, designers can effortlessly define their preferred memory dimensions, word length, layout, among other vital parameters. The system then autonomously crafts several memory arrays aligning with the set criteria. Additionally, it supplies the necessary files for OpenLane, ensuring easy incorporation of these memories from RTL to GDSII stages.

Our system's primary strength is its capacity to simplify the making of tailor-made memories by automating interleaving and granting design layout flexibility. This dramatically cuts down on design duration and labor, allowing designers to adeptly generate memories with distinct attributes, all the while respecting SKY130 PDK constraints. Consequently, our system stands out as an indispensable asset for memory design within the SKY130 PDK framework, paving the way for more streamlined and optimized semiconductor designs.
![image](https://github.com/Baungarten-CINVESTAV/SKY130-Interleaving-Memory-Tool/assets/101527680/ee12ce04-a658-43a2-a06d-7f09dbd0f79a)
![image](https://github.com/Baungarten-CINVESTAV/SKY130-Interleaving-Memory-Tool/assets/101527680/a5a59cbe-d50a-44d2-91b4-c9bc5379ce4c)

## Interleaving-Memory-Tool
The Interleaving Memory Tool has been developed to simplify the memory design process when working with the SKY130 design kit. While the SKY130 kit offers three pre-defined memory sizes, sometimes projects need different sizes. This tool fills that gap.

Fundamentally, the tool is a collection of Python scripts that adjust memory sizes by tweaking parameters in a Verilog file. Leveraging the three SKY130 memory sizes, 8×1024, 32×256, and 32×512, the tool blends these memories to create the needed configuration. This allows designers to adapt to a variety of project needs, from simple modules to intricate memory structures.

The tool's user-friendliness is clear: users simply input the base memory type (0 for 8×1024, 1 for 32×256, or 2 for 32×512), word width, memory directions, and preferred layout (c for column, r for row, g for grid, ct for custom, or a for automatic). If custom layout is chosen, they also specify block memories on the X and Y axis with X position-based priority. For the automatic option, users set the X and Y perimeters, and the tool fills in as many memory blocks as the defined space permits.

Additionally, the tool collaborates with OpenLane configuration files. Using the Python scripts, it adjusts baseline configurations based on memory type and size, allowing for a more fluid integration process and reduced design time.

A visual workflow, illustrating the process of creating memory up to generating the GDSII file of the memories, has been provided for clarity. The workflow takes the user from selecting the memory type, determining data and address size, choosing the arrangement, importing files into OpenLane, and finally running the OpenLane flow.

![image](https://github.com/Baungarten-CINVESTAV/SKY130-Interleaving-Memory-Tool/assets/101527680/d5fd7f69-006e-4bcd-8daa-e451cc19dc5b)


Workflow Diagram for Memory Configuration – This illustration details the step-by-step process from selecting the memory type to executing the OpenLane flow, leading to the generation of the GDSII file of the memories.

**Tool Installation and Use**

Before you begin:
- Ensure you have Python 3.6+ with pip, svgwrite, cairosvg installed.
- You'll also need Git 2.34+ and OpenLane.

To start using the Interleaving Memory Tool:
1. Download the required files from its GitHub repository:
   ```
   git clone [GitHub Repository URL]
   ```
2. Generate the desired memory by executing the `imem_generator` python script. Example command:
   ```
   cd [Directory Path]
   python3 imem_generator.py [mt] [wn] [ad] [p] [op1] [op2]
   ```

Detailed parameter explanations can be found in the provided documentation.

**Output Structure**

Once the Python script is run, a summary of the memory setup will be shown. The tool contains a "designs" folder for storing generated memory structures. This folder follows a specific naming convention and houses essential files and sub-folders for compatibility with OpenLane. The tool also provides schematic visuals of the memory in both PNG and SVG formats.

**Usage Examples**

- **Grid Arrange**: Here, a grid layout is used with a memory size of 8×4096. After choosing the memory, set the parameters accordingly:
  ```
  python3 imem_generator.py 0 8 16384 g
  ```

- **Row Arrange**: For a memory size of 32×1024, use:
  ```
  python3 imem_generator.py 1 32 1024 r
  ```

- **Custom Arrange**: For a custom arrangement of 64×2048 using memory type 2, in a rectangle with 4 columns and 2 rows:
  ```
  python3 imem_generator.py 2 64 2048 ct 4 2
  ```

The visual outputs for these configurations can be found in the provided figures.


