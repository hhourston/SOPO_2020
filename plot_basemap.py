import netCDF4
import pandas as pd
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib
import xarray as xr
# import matplotlib.pyplot as plt
# import numpy as np
# import argparse
# import common_functions as cf
# import os
# import scipy.io as sio
# from netCDF4 import Dataset
# import matplotlib.tri as tri
from mpl_toolkits.basemap import Basemap, shiftgrid, cm
# from scipy.spatial import Delaunay
# from pylab import ginput
# import cPickle as pickle
# import scipy as spy
# from scipy.interpolate import griddata
# import os
import matplotlib.pyplot as plt
# import csv
# import xarray as xr
import glob
import h5py
import dask.array as da
import numpy as np
from datareader import profiles
from dataplotter import datamap


# Year that is being processed
year = 2019
read_all = False
type = 'CTD'

# directory that stores all osd_archive_data
archive_dir_test = '/run/user/1000/gvfs/smb-share:server=sid01hnas01b,share=osd_data/OSD_DataArchive/osd_data_final/'


if read_all:

    data = profiles.read_ctd(archive_dir_test, year, 'CTD')
    input('ctd created?')

else:
    data = pd.read_csv('./data/ctd_'+str(year) + '.csv')

datamap.make_map(data)
