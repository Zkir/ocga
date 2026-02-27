# OCGA Project Documentation for Gemini CLI

This document provides an overview of the OCGA (osm-cga, or Computer Generated Architecture for OSM) project, and mandatory operating instructions intended to serve as contextual knowledge for the Gemini CLI agent to interact with the project effectively.

## Project Overview

The OCGA project is a procedural modeling engine designed to generate detailed 3D building models for OpenStreetMap from simple 2D footprints. Inspired by ESRI CityEngine, it utilizes a custom, declarative "shape grammar" language with the `.ocga` file extension to define generation rules.

**Key Components and Workflow:**

1.  **Input:** The process begins with a standard `.osm` file containing a building's 2D outline.
2.  **Data Modeling (`src/ocga/mdlOsmParser.py`):** Reads `.osm` data, defining `T3DObject`s (representing building parts) which maintain their own local coordinate systems ("scopes") for contextual transformations. It also handles writing the final detailed `.osm` output.
3.  **Rule Definition (`.ocga` files):** Users define generation logic using named `rules` within `.ocga` files. These rules describe how to modify or subdivide shapes using operations like `split_x`, `split_z`, and `scale`.
4.  **Compilation (`src/ocga/ocgaparser/` module):** An ANTLR-based parser (defined by `ocga.g4`) parses `.ocga` files and translates them into a dynamically generated Python function (e.g., `checkRulesMy`).
5.  **Execution (`src/ocga/cli.py`):** The main engine executes the generated Python function, which applies geometric manipulations to `T3DObject`s via an `OCGAContext` object.
6.  **Output:** The result is a new, detailed `.osm` file containing the generated 3D building parts.

## Operation instructions

* **Python version**: use Python 12
*   **Code Structure:** The project uses a standard `src` layout. The main package code is located in `src/ocga`, and tests are in `tests/`.
* **Local installation:** For development, install the package in editable mode from the project root. This will also install all required dependencies: `pip install -e`
* **Automated tests** can be run via `pytest` or via runing the test script directly from the project root: `python tests/test_main.py`
* **Manual testing** can be done via running the `ocga` command-line tool. It takes an input OSM file, an OCGA rules file, and an output path. `ocga -i <input.osm> -r <rules.ocga> -o <output.osm>`
* **Definition of Done**: A task is considered DONE only when:
    * pylint reveals no errors: run `pylint -E src tests`
	* all the autotests passed successfully: run `pytest`
	* successful execution of manual test confirmed by the human.
	* GEMINI.md file is updated, including (but not limiting to) the following sections: "Recent Accomplishments", and if necessary, "Next Steps".
* Do not suggest git commits. Git commits in this project are allowed for protein-based developers only.	
*   **OCGA Language:** A custom domain-specific language for defining procedural architectural rules. The grammar is defined in [ocga.g4](src/ocga/ocgaparser/ocga.g4). Human readable description of the language and avalible operations are described in [OCGA.md](docs/OCGA.md).
*   **Comments and Documentation:** Comments within the code should explain *why* certain decisions were made, especially for complex logic. External documentation, like this `GEMINI.md`, should provide a high-level overview and usage instructions.


## Command Line Example
To process `gorky_park_entrance.osm` using `gorky_park_entrance.ocga` rules and output to `ocga_output/gorky_park_entrance-rewrite.osm`:

```bash
ocga -i docs/ocga_samples/gorky_park_entrance.osm -r docs/ocga_samples/gorky_park_entrance.ocga -o docs/ocga_output/gorky_park_entrance-rewrite.osm
```

You can find example usage in `example.bat` (for Windows) and `example.sh` (for Linux/macOS).

This script will execute various OCGA rule sets on sample OSM files and compare the generated output against reference files.



## Recent Accomplishments (24-Feb-2026)

**Goal:** Prepare the project for publication on the Python Package Index (PyPI).

To make the `ocga` tool easily distributable and installable for other users, the project was refactored into a standard Python package.

**Key Changes:**

*   **Project Restructuring:** The project was converted to a modern `src` layout, with all source code moved into `src/ocga`.
*   **Packaging Metadata:** A `pyproject.toml` file was created to define project metadata, dependencies, and the command-line entry point.
*   **Command-Line Tool:** A proper command-line script entry point was created, so the tool can now be run with the simple `ocga` command after installation.
*   **Code Adaptation:** All internal imports were updated to be relative, making the code function correctly as a package.
*   **Standardization:** A `LICENSE` file was added, and the `README.md` was updated with installation and usage instructions.
*   **Testing:** Tests were moved to a dedicated `tests` directory and updated to work with the new package structure. The package was installed locally in editable mode (`pip install -e .`) and all tests were confirmed to pass.
*   **Build:** The project was successfully built into standard distribution formats (`.whl` and `.tar.gz`) located in the `dist/` directory.

## Versioning Notes

- The latest version uploaded to **test.pypi.org** is `0.1.2`.
- **Reminder:** Before the next upload to TestPyPI, the `version` in `pyproject.toml` must be manually incremented.
- **Future Improvement Note:** For more automated versioning (especially for development builds), consider implementing `setuptools_scm`. This tool can generate unique versions like `0.1.2.dev1` automatically based on Git history, removing the need for manual edits.