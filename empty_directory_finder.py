# -*- coding: utf-8 -*-

import argparse
import os

parser = argparse.ArgumentParser(description='Identify any empty directories within a root directory')
parser.add_argument('rootPath', help='path to the root directory to be searched')

args = parser.parse_args()

rootPath = args.rootPath

for root, dirs, files in os.walk(rootPath):
    for folder in dirs:
        if len(os.listdir(os.path.join(root,folder))) == 0:
            print(folder)