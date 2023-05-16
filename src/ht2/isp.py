"""
image signal processings
"""
import cv2

def jpg_noise(im, jpg_compress_rate):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), jpg_compress_rate]
    result, encimg = cv2.imencode('.jpg', im, encode_param)
    im = cv2.imdecode(encimg, 0)
    return im