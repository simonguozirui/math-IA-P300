import sys
from collections import OrderedDict

from mne import create_info, concatenate_raws
from mne.io import RawArray
from mne.channels import read_montage

import pandas as pd
import numpy as np

from glob import glob
import seaborn as sns
from matplotlib import pyplot as plt

sys.path.append('../muse')
import utils

#matplotlib inline

subject = 1
session = 1
#add data file
dataPath = '../data/HeadbandP/p=0.5'

raw = utils.load_data(dataPath, sfreq=256., subject_nb=subject, session_nb=session, ch_ind=[0, 1, 2, 3])

#raw.plot_psd(tmax=np.inf)
print raw
#raw.set_eeg_reference(ref_channels='average', projection=False, verbose=None)
raw.filter(1,30, method='iir')


from mne import Epochs, find_events

events = find_events(raw)
event_id = {'Non-Target': 1, 'Target': 2}

epochs = Epochs(raw, events=events, event_id=event_id, tmin=-0.1, tmax=1.1, baseline=None,
                reject={'eeg': 100e-6}, preload=True, verbose=False, picks=[0,1,2,3], add_eeg_ref=False)


conditions = OrderedDict()
conditions['Non-target'] = [1]
conditions['Target'] = [2]

print epochs

conditions = OrderedDict()
conditions['Non-target'] = [1]
conditions['Target'] = [2]

fig, ax = utils.plot_conditions(epochs, conditions=conditions, ci=97.5, n_boot=1000, title='', diff_waveform=(1, 2))
