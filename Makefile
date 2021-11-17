benchmark_datafile_url=https://zenodo.org/record/3697797/files/Data%20and%20links.csv?download=1

dlimages: downloads/images
downloads/images: download-images.py downloads/benchmark_metadata.txt
	mkdir -p downloads/images 
	python download-images.py downloads/benchmark_metadata.txt downloads/images

dlmeta: downloads/benchmark_metadata.txt
downloads/benchmark_metadata.txt: 
	mkdir -p downloads
	wget --quiet -O $@ $(benchmark_datafile_url)

clean:
	rm -rf downloads/images

sterilise:
	rm -rf downloads