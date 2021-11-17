import pandas as pd
import argparse
import subprocess
import os.path

IMAGE_ORIGINAL_URL_COLUMN = 'jpegURL'
IMAGE_OVERLAY_URL_COLUMN = 'pngSegSelURL'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile')
    parser.add_argument('-l','--limit', type=int, default=None)
    parser.add_argument('--quiet', action='store_true')
    parser.add_argument('outputdir')
    args = parser.parse_args()

    # Read metadata file
    df = pd.read_csv(args.inputfile, nrows=args.limit)

    # Select those with region detection overlays
    mask = (df.pngSegSelURL.notnull())

    # Assemble list of URLs
    urls = list(df[mask][IMAGE_ORIGINAL_URL_COLUMN]) + list(df[mask][IMAGE_OVERLAY_URL_COLUMN])
    
    # Loop over URLs and download images
    for url in urls:
        outputfile = args.outputdir + os.path.sep + url.split('/')[-1]
        if not os.path.exists(outputfile):
            subprocess.run(['wget','--quiet','-O', outputfile, url])    

if __name__ == '__main__':
    main()