import argparse

from illastik2geotiff.lib import georeference_h5_file


def main():
    parser = argparse.ArgumentParser(
        description="Convert h5 segmentation output to a GeoTIFF"
    )

    parser.add_argument(
        "image_path",
        type=str,
        help="Path to the input image with the georeferencing info",
    )
    parser.add_argument(
        "seg_h5_path", type=str, help="Path to the h5 segmentation output"
    )
    parser.add_argument("output_path", type=str, help="Path to the output GeoTIFF")
    args = parser.parse_args()

    georeference_h5_file(args.image_path, args.seg_h5_path, args.output_path)


if __name__ == "__main__":
    main()
