Calibrating custom DIGIT sensor:
1. cd DataCollection
2. python record_Gel.py and specify folder, object name along with # of frames to capture

After finishing recording, run in this order:
3. cd Calibration
4. python polyTableCalib.py ( check data_path is pointing at recorded frames folder)
5. python generateShadowMasks.py ( check data path)
6. python generateTensorMap.py

This will create dataPack.npz, polycalib.npz, shadowTable.npz under DATA_PATH.
This will also create femCalib.npz under calibs folder.

# Usage
1. cd OpticalSimulation
2. Change data_folder path into calibration folder's path
3. Change image name according to your taste.

I guess the gelmap5.npy is still an issue. There are some glitches in simulated images at the moment.

Also, in simOptical.py, I am doing manual tensor transpose to make up for inconsistencies in tensor broadcasting. 
It seems to be working.