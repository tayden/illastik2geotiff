import h5py
import numpy as np
import rasterio


def georeference_h5_file(image_path: str, seg_h5_path: str, output_path: str):
    # Pull the reference info, and other metadata from the source image
    with rasterio.open(image_path) as src:
        profile = src.profile

    # Reader the h5 output file into a numpy array
    with h5py.File(seg_h5_path, "r") as f:
        d = np.array(f["exported_data"])[0, 0, :, :, 0]
        height, width = d.shape

        assert height == profile["height"], "Label height does not match image height"
        assert width == profile["width"], "Label width does not match image width"

    # Write a new tif file, copying all the image metadata to it to transfer the ref info
    out_profile = profile.copy()
    out_profile.update({"count": 1})  # 1 band instead of 3 in src imagery

    with rasterio.open(output_path, "w", **out_profile) as dst:
        dst.write(d, indexes=1)
