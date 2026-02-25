# OCGA
osm-cga, or Computer Generated Architecture for OSM

The real holy grail of neocarthogaphy is to automatically generate photorealistic models of buildings to show on a map or to use in 3d applications and computer games such as flight simulators(e.g. X-plane). This goal remains as unattainable today as it was 20 years ago. 

In this project, we will do something a bit more easy.  We will create a simple computer language to describe 3D building models that will allow us to quickly and easily create 3D building models for [OpenStreetMap](https://www.openstreetmap.org/) based on the [Simple 3D Buildings](https://wiki.openstreetmap.org/wiki/Simple_3D_Buildings) standard.

This project is largely inspired by ESRI City Engine. However, many things are quite different.

## Installation

Install the package from PyPI:
```bash
pip install ocga
```

## Usage

The OCGA engine can be run from the command line. It takes an input OSM file, an OCGA rules file, and an output path.

```bash
ocga -i <input.osm> -r <rules.ocga> -o <output.osm>
```

**Example:**
To process `gorky_park_entrance.osm` using `gorky_park_entrance.ocga` rules and output to `ocga_output/gorky_park_entrance-rewrite.osm`:

```bash
ocga -i ocga_samples/gorky_park_entrance.osm -r ocga_samples/gorky_park_entrance.ocga -o ocga_output/gorky_park_entrance-rewrite.osm
```

You can also find example usage in `example.bat` (for Windows) and `example.sh` (for Linux/macOS).
