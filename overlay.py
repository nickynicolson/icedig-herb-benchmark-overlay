import argparse
import cv2 as cv

RESIZE_PERCENTAGE=0.25

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile')
    args = parser.parse_args()

    img_spec = cv.imread(args.inputfile, cv.IMREAD_COLOR)
    overlay_image_filename = args.inputfile.replace('.jpg','_sel.png')
    img_overlay = cv.imread(overlay_image_filename, cv.IMREAD_COLOR)

    cv.imshow('specimen image',cv.resize(img_spec, (int(img_spec.shape[1]*RESIZE_PERCENTAGE), int(img_spec.shape[0]*RESIZE_PERCENTAGE))))
    cv.waitKey(0) 
    cv.destroyAllWindows()

    alpha = 0.75
    beta = (1.0 - alpha)
    img_overlaid = cv.addWeighted(img_spec, alpha, img_overlay, beta, 0.0)
    cv.imshow('overlaid image',cv.resize(img_overlaid, (int(img_overlaid.shape[1]*RESIZE_PERCENTAGE), int(img_overlaid.shape[0]*RESIZE_PERCENTAGE))))
    cv.waitKey(0) 
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()