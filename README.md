
## Required environment
torch == 1.2.0

## File download
The CEW dataset is available for download at the following address:  
Link: https://parnec.nuaa.edu.cn/_upload/tpl/02/db/731/template731/pages/xtan/ClosedEyeDatabases.html  


## Prediction steps
### Use pre-trained weights
1. Unzip the library after downloading, download it from Baidu.com, put it into model_data, run predict.py, and enter  
`` python
img/street.jpg
```
2. Inside predict.py, you can set up the settings to do fps test and video video detection.  
### b. Use your own trained weights
1. Follow the training steps.  
2. Inside the ssd.py file, modify model_path and classes_path to correspond to the trained files in the following section; **model_path corresponds to the weights file under the logs folder, and classes_path corresponds to the classes in model_path **. 3.  

3. Run predict.py and enter  
`` python
img/street.jpg
```
4. Inside predict.py, you can set up fps testing and video detection.  

## Evaluation Steps
1. This paper uses the VOC format for evaluation.  
2. If the voc_annotation.py file has been run before training, the code will automatically divide the dataset into training set, validation set and test set. If you want to modify the ratio of the test set, you can modify the trainval_percent under the voc_annotation.py file. trainval_percent is used to specify the ratio of (training set + validation set) to the test set, by default (training set + validation set):test set = 9:1. train_percent is used to specify the ratio of training set to validation set in (training set + validation set), by default training set:validation set = 9:1.
3. After dividing the test set using voc_annotation.py, go to the get_map.py file and modify classes_path. classes_path is used to point to the txt corresponding to the detection category, which is the same as the txt used for training. Evaluating your own dataset must be modified.
4. Modify model_path and classes_path in ssd.py. **model_path points to the trained weights file in the logs folder. classes_path points to the txt that corresponds to the detection category.  
5. Run get_map.py to get the evaluation results, which are saved in the map_out folder.

