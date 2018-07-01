#! /usr/bin/env python3
import os
os.environ['GLOG_minloglevel'] = '2' # suprress Caffe verbose prints
import caffe
os.environ['GLOG_minloglevel'] = '1'
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prototxt", help="prototxt of caffe model", type=str)
parser.add_argument("caffemodel", help="output filename", type=str)
args = parser.parse_args()

net = caffe.Net(args.prototxt, caffe.TEST)
net.save(args.caffemodel)
