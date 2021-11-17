# icedig-herb-benchmark-overlay

This repository contains utilities to download the original image and region detected overlays from the Dillen et al 2019 benchmark herbarium specimen dataset[1] built for the ICEDIG project.

A `Makefile` is used to manage dependencies, and a `python` script (`download-images.py`) uses `pandas` to read the metadata file and extract the URLs for download, which are passed to `wget`. 

Targets:

- `make` - default target, downloads the metadata file and then downloads all images which have region detection overlays available
- `clean` - removes downloaded images
- `sterilise` - removes all downloaded data

A utility script using OpenCV is supplied which displays a specimen image with its associated overlay. This can be called as:
`python overlay.py inputfile`

[1] Dillen, M., Groom, Q., Chagnoux, S., Güntsch, A., Hardisty, A., Haston, E., Livermore, L., Runnel, V., Schulman, L., Willemse, L., Wu, Z., Phillips, S., 2019. A benchmark dataset of herbarium specimen images with label data. Biodiversity Data Journal 7, e31817. https://doi.org/10.3897/BDJ.7.e31817
