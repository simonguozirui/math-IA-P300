# Investigating the Effect of Target Ratio in Visual Oddball Paradigm Experiments on P300 Components
#### An International Baccalaureate Higher Level Mathematics Investigation

## Credit
Many of the scripts are modified upon or are from [Muse-lsl](https://github.com/alexandrebarachant/muse-lsl/), a collection of Python scripts to use the Muse 2016 BLE headset with LSL.

## Requirements

#### Hardware
You must have a Muse headband 2016 or a LowdownFocus Glasses.
If you have a Windows or MacBook, please ensure you have a BLED112 dongle in order to establish BLE connection.

**This code is
only compatible with the 2016 version of the Muse headset as well as the Smith LowdownFocus glasses.**

#### Software
Install a variety of pip packages required in both Python2 and Python3.

```
pip install -r requirements.txt
pip3 install -r requirements.txt
```

Please install mne 0.13 in Python2 and mne 0.15 in Python3
```
pip install mne==0.13
pip3 install mne
```

Install the older Pygatt version for the BLE communication.
`pip install pygatt==3.1.1`

Finally, the code for streaming and recording data is compatible with Python
2.7 and Python 3.x. However, the code for stimulus presentation relies on
psychopy and therefore only runs with Python 2.7.

## Running Experiments

Start the experiment by establishing streaming.

`python muse-lsl.py --a YOUR_DEVICE_MAC_ADDRESS`

Once the stream is up and running, you can visualize it with

`python3 lsl-viewer-V2.py`

Start the P300 experiment in another terminal by executing

`python experiment/generate_Visual_P300.py -d 120 & python lsl-record.py -d 120`

## Data
Samples of data that I collected can be found in `/data/`
All data are in .csv format, and the subject names are replaced with numbers to ensure privacy.
If you choose to collect your data, make sure that your data is put in a hierarchy such as `data/category/subjectX/sessoinX/date+time.csv`

## Data Analysis
To produce the raw EEG power density spectrum and the ERP waveform, please edit the data folder reference in `/script/P300.py`

And then run `python /script/P300.py`

For sample procedure of data analysis, check out [this notebook by Alexandre Barachant](https://github.com/alexandrebarachant/muse-lsl/blob/master/notebooks/P300%20with%20Muse.ipynb/).

My full research would be published soon. For now, you can check the ERP waveforms that I generated in `/graph/`
