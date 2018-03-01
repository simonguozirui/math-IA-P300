# Investigating the Effect of Target Ratio in Visual Oddball Paradigm Experiments on P300 Components
#### An International Baccalaureate Higher Level Mathematics Investigation

## Credit
Many of the scripts are from [Muse-lsl](https://github.com/alexandrebarachant/muse-lsl/), a collection of Python scripts to use the Muse 2016 BLE headset with LSL.

## Requirements

The code relies on [pygatt](https://github.com/peplin/pygatt) for the BLE communication.
pygatt works on Linux and should work on Windows and macOS provided that you have a BLED112 dongle.
You have to use the development version of pygatt, that can be installed with pip using:

`pip install git+https://github.com/peplin/pygatt`

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

You will also need to find the MAC address of your Muse headset or LowdownFocus. **This code is
only compatible with the 2016 version of the Muse headset as well as the Smith LowdownFocus glasses.**

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

## Data Analysis

For data analysis, check out [these notebooks](https://github.com/alexandrebarachant/muse-lsl/blob/master/notebooks/).
