# illastik2geotiff

A Python tool to apply GeoTIFF georeferencing information from a source image to an HDF5 output file produced by
Illastik, converting the segmentation results into a spatially referenced GeoTIFF.

## Description

Illastik is a powerful tool for interactive image segmentation. When working with geospatial imagery (like satellite or
aerial photos), the original images often contain georeferencing information (like projection, transform, and spatial
extent) embedded in their metadata. However, the HDF5 files exported by Illastik typically do not retain this critical
information.
`illastik2geotiff` solves this problem by taking the original GeoTIFF image (which contains the georeferencing) and the
corresponding HDF5 segmentation output from Illastik. It reads the georeferencing metadata from the source GeoTIFF and
applies it to the segmentation data from the HDF5 file, writing a new GeoTIFF file that is correctly georeferenced. This
allows the segmentation results to be accurately displayed and used within GIS software or other geospatial workflows.

## Installation

You can install `illastik2geotiff` directly from the GitHub repository using pip. The project uses pyproject.toml for
dependency management.

```bash
pip install git+https://github.com/tayden/illastik2geotiff.git
```

This command will install the package and its specified dependencies.

## Usage

The tool is primarily designed to be used from the command line.

### Command Line Interface (CLI)

The entry point for the command line tool is `illastik2geotiff`.
illastik2geotiff <image_path> <seg_h5_path> <output_path>

- `<image_path>`: Path to the original GeoTIFF image that contains the desired georeferencing information.
- `<seg_h5_path>`: Path to the HDF5 file exported by Illastik (e.g., prediction.h5). The tool expects the segmentation
  data to be in the /exported_data dataset within the HDF5 file.
- `<output_path>`: Path where the resulting georeferenced GeoTIFF file will be saved.

*Example:*

```bash
illastik2geotiff /path/to/your/original_image.tif /path/to/your/illastik_output.h5 /path/to/your/segmented_output.tif
```

The script will verify that the dimensions of the segmentation data in the HDF5 match the dimensions of the source image
before writing the output GeoTIFF.

### Python API

The core georeferencing logic is available as a function that can be imported and used in other Python scripts:

```python
from illastik2geotiff.lib import georeference_h5_file

# Replace with your file paths
image_file = "/path/to/your/original_image.tif"
h5_file = "/path/to/your/illastik_output.h5"
output_file = "/path/to/your/segmented_output.tif"

georeference_h5_file(image_file, h5_file, output_file)
```

This allows for integration into larger processing pipelines.

## Requiroements

- Python 3.10+
- `h5py>=3.13.0`
- `numpy>=2.2.5`
- `rasterio>=1.4.3`
-

These dependencies are automatically installed when using the `pip install` command from the GitHub repository.
