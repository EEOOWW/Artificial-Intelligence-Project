# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:14:56 2022

@author: Admin
"""
import tarfile
import numpy as np
import pandas as pd
import os
import shutil


path=r"D:\University\FYP\dataset\images_003.tar.gz"
#filename="/images_001"
#count="9"
#counts=9
filetype=".tar.gz"
files = tarfile.open(path)
files.extractall(r"D:\University\FYP\dataset\images_003")

