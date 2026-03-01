# OCGA: Procedural 3D Buildings for OpenStreetMap

Creating detailed [3D buildings](https://wiki.openstreetmap.org/wiki/Simple_3D_Buildings) in OSM by manually adding **building:part's** and moving nodes back and forth is tedious and slow.

OCGA (OSM Computer-Generated Architecture) is built on a key insight: much like music, architecture is often based on the **repetition of common elements and patterns**.

Because architecture is inherently rule-based, we can leverage a different approach: **procedural generation**. Instead of building models by hand, you define these architectural patterns using a simple `.ocga` language, and let the engine execute the repetitive work of generating the complex geometry for you.

To achieve this, we have developed a new, unique domain-specific language: **OCGA**. This project provides both the **[OCGA language specification](https://github.com/Zkir/ocga/blob/main/docs/OCGA.md)** and a simple **command-line tool** that interprets this new language, enabling rapid creation of detailed building models.

While certain ideas were adopted from ESRI's CityEngine, OCGA is not its clone, and many things are implemented differently.


## Installation

Install the package from PyPI:
```bash
pip install ocga
```

## Workflow

The intended cycle for using OCGA is as follows:

1.  **Create an Outline:** Start by saving a building's footprint/outline into its own `.osm` file.

2.  **Define the Rules:** Write a corresponding `.ocga` rules file tailored to that building's architecture. This is where you describe how to procedurally generate the model's parts.

3.  **Generate the Model:** Run the `ocga` command-line tool, providing it with your outline and rules files.
    ```bash
    ocga -i <path/to/your_building.osm> -r <path/to/your_rules.ocga> -o <path/to/generated_model.osm>
    ```

4.  **Verify Before Uploading!** Before you upload the data to OpenStreetMap, it is **crucial** to visually inspect the generated model.
    - **Primary Method (JOSM):** The easiest way is to open the generated `.osm` file in JOSM and use the **[UrbanEye3D](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Urban_Eye_3D)** plugin viewer.
    - **Alternative Method:** You can use `osm2world` to export the model to a `.gltf` file, which can then be opened in any standard 3D viewer (like the built-in Windows 3D Viewer or `f3d` on Linux).

5.  **Upload to OpenStreetMap:** Once you are satisfied, you can upload the data from JOSM. You may need to merge the layer containing the generated model with your main data layer before uploading.

## Usage as a Library

While the primary use case for OCGA is the command-line tool, its core engine can be imported and used directly in your own Python projects, as permitted by the MIT license.

The main entry point function is `ocga_process2`, which can be imported from the top-level package. Its function is analogous to the CLI tool:

```python
from ocga import ocga_process2

input_file = "path/to/building.osm"
rules_file = "path/to/rules.ocga"
output_file = "path/to/generated.osm"

# The other arguments are optional
ocga_process2(input_file, output_file, rules_file)
```

Other functions from the engine modules (e.g., from `ocga.ocga_engine`) can also be imported, but their APIs are not guaranteed to be stable and may change. Use them at your own risk.

## Language and Examples

- For a complete guide to the syntax and operations, see the **[OCGA Language Reference](https://github.com/Zkir/ocga/blob/main/docs/OCGA.md)**.
- A collection of sample `.osm` and `.ocga` files can be found in the **[docs/ocga_samples](https://github.com/Zkir/ocga/tree/main/docs/ocga_samples)** directory.
- The `example.bat` and `example.sh` scripts in the root directory demonstrate how to run the tool on these samples.
