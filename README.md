# Overview

The proposed script gets ground truth images in hdf5 format from the fastMRI dataset and unpack them to target folder

The fastMRI dataset is a large open dataset with MRI of the knees and brains.

Learn more about fastMRI project and how to get fastMRI dataset - https://fastmri.org/

# Requirements

* Python 3.5 or latter
* watchdog - `$ pip install watchdog`
* h5py `pip install h5py`

# Download

`$ git clone https://github.com/lazyniv/fastMRI_gt_parser.git`

# Usage

```
cd fast_MRI_gt_parser/
$ sh run.sh <URL/to/tar/archive> <path/to/target/folder>
```

