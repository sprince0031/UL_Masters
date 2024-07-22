from PIL import Image
import matplotlib.pyplot as plt

# util function to plot the original HE image, ground truth IHC image and transformed image from the diffuser model
TRAIN_DIR = 0
TEST_DIR = 1
VALIDATION_DIR = 2
def plotImages(original_image_name, ground_truth_image_name, dir_type, transformed_image=None):
  if dir_type == TRAIN_DIR:
    subfolder = 'train'
  elif dir_type == TEST_DIR:
    subfolder = 'test'
  elif dir_type == VALIDATION_DIR:
    subfolder = 'validation'

  HE_dir_prefix = f'BCI_dataset/HE/{subfolder}/'
  IHC_dir_prefix = f'BCI_dataset/IHC/{subfolder}/'
  original_image = Image.open(f'{HE_dir_prefix}/{original_image_name}')
  ground_truth_image = Image.open(f'{IHC_dir_prefix}/{ground_truth_image_name}')
  if transformed_image is not None:
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(original_image)
    plt.title('Original Image')
    plt.subplot(1, 3, 2)
    plt.imshow(ground_truth_image)
    plt.title('IHC Ground Truth Image')
    plt.subplot(1, 3, 3)
    plt.imshow(transformed_image)
    plt.title('IHC Transformed Image')
    plt.show()
  else:
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title('HE Image')
    plt.subplot(1, 2, 2)
    plt.imshow(ground_truth_image)
    plt.title('IHC Image')
    plt.show()