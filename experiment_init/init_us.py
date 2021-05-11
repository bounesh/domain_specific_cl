################################################################
# Definitions required for CNN graph
################################################################
#Filter size at different depth level of CNN in order
fs=3
#Interpolation type for upsampling layers in decoder
interp_val=1 # 0 - bilinear interpolation; 1- nearest neighbour interpolation
################################################################

################################################################
# data dimensions, num of classes and resolution
################################################################
#Name of dataset
dataset_name='us'
#Image Dimensions
img_size_x = 240
img_size_y = 193
# Images dimensions in one-dimensional array
img_size_flat = img_size_x * img_size_y
# Number of colour channels for the images: 1 channel for gray-scale.
num_channels = 1
# Number of label classes : # 0-background, 1-uterus
num_classes=2
#Image dimensions in x and y directions
size=(img_size_x,img_size_y)
#target image resolution
target_resolution=(1.5,1.5)
#label class name
class_name='ut'
#class_name='lv'
################################################################
#data paths
################################################################
#validation_update_step to save values
val_step_update=5
#base directory of the code
# base_dir='D:/Dokumenti/Faks/Magisterij/LGM/domain_specific_cl'
# srt_dir='D:/Dokumenti/Faks/Magisterij/LGM/domain_specific_cl'
base_dir='/home/eb1690/Documents/domain_specific_cl'
srt_dir='/home/eb1690/Documents/domain_specific_cl'

#Path to data in original dimensions in default resolution
data_path_tr='../data_us'

#Path to data in cropped dimensions in target resolution (saved apriori)
data_path_tr_cropped='../data_us'
################################################################

################################################################
#training hyper-parameters
################################################################
#learning rate for segmentation net
lr=0.001
#pre-training batch size
mtask_bs=20
#batch_size for fine-tuning on segmentation task
batch_size_ft=10
#foreground structures names to segment
struct_name=['ut']
