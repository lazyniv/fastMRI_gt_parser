import os
import h5py
import time

from watchdog.events import RegexMatchingEventHandler

class HDF5EventHandler(RegexMatchingEventHandler):

    HDF5_REGEX = [r".*[^_thumbnail]\.h5$"]

    def __init__(self):
        super().__init__(self.HDF5_REGEX)

    def on_created(self, event):
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)

        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = "{filename}_gt.h5".format(filename=filename)
        with h5py.File(event.src_path, "r") as src:
            with h5py.File(filename, "w") as target:
                gt_tensor = src["reconstruction_rss"][()]
                target.create_dataset("gt_tensor", data=gt_tensor)

        os.remove(event.src_path)
