# HER2 Molecular Marker Scoring Using Transfer Learning and Decision Level Fusion | Notes and inferences
**Paper reference:**
> HER2 Molecular Marker Scoring Using Transfer Learning and Decision Level Fusion

[[HER2_Molecular_Marker_Scoring_Using_Transfer_Learning_and_Decision_Level_Fusion_s10278-021-00442-5.pdf#page=1&selection=6,0,7,12|HER2_Molecular_Marker_Scoring_Using_Transfer_Learning_and_Decision_Level_Fusion_s10278-021-00442-5, page 1]]

## Key takeaways
1. Five pre-trained deep learning architectures were used for the comparative assessment of HER2 scoring. The different architectures are as follows:
	1. [[HER2_Molecular_Marker_Scoring_Using_Transfer_Learning_and_Decision_Level_Fusion_s10278-021-00442-5.pdf#page=4&selection=151,0,151,41|VGG16]]
	2. [[HER2_Molecular_Marker_Scoring_Using_Transfer_Learning_and_Decision_Level_Fusion_s10278-021-00442-5.pdf#page=4&selection=151,0,151,41|VGG19]]
	3. ResNet50
	4. MobileNetV2
	5. NASNetMobile
2. The training dataset consisted of 2130 image patches extracted from 300 training images, while the testing dataset consisted of 800 new test image patches from 100 test images.
3. The VGG19 architecture showed the best accuracy for the test images, with an accuracy of 93% for patch-based scoring and 98% for image-based scoring using statistical voting.
4. The proposed approach of transfer learning with VGG19 and statistical voting provides a capable quantification pipeline for automated HER2 score generation.

## Data preparation and pre-processing

## Model architectures
Below screenshot from the paper represents the pre-trained DL model architectures that were used.

![[HER2 Molecular Marking with transfer learning - DL model architectures.png]]


## How does the proposed approach compare to other methods in terms of accuracy?

The proposed approach, which uses transfer learning and statistical voting, achieves high accuracy in HER2 scoring. Specifically, the VGG19 pre-trained model with statistical voting achieves an accuracy of 93% in patch-based scoring and 98% in image-based scoring. This accuracy is competitive with other state-of-the-art methods reported in the literature. The proposed approach outperforms other deep learning-based approaches for HER2 scoring in terms of accuracy.

## How is the training data preparation in this work different from other reported literature?

In this work, the training data is prepared by extracting image patches from 30 different cases of HER2-stained breast cancer tissue samples. A total of 2130 image patches are generated from these cases, with each case contributing an equal number of patches. The patches are randomly selected from the images and then cropped into 8 sub-image patches. The dataset is balanced, with an equal number of patches for each class (negative, equivocal, positive). The patches are then used for training the deep learning models.

This approach to training data preparation is different from other reported literature in the following ways:

1. Dataset Size: The dataset used in this work consists of 2130 image patches, which is relatively small compared to some other studies that use larger datasets. For example, one study mentioned in the document used 4019 image patches from 52 whole slide images (WSIs).

2. Labeling: In this work, the patches are labeled based on the overall score of the corresponding whole image, as provided in the dataset. There is no manual marking or segmentation of specific regions within the patches. This is different from some other studies that may involve manual segmentation of nuclei or cell membranes within the patches.

3. Class Distribution: The dataset in this work is balanced, with an equal number of patches for each class (negative, equivocal, positive). This ensures that each class has an equal contribution to the training data. Other studies may have different class distributions depending on the specific dataset and research question.

4. Ground Truth: The ground truth used in this work is based on the training data provided in the HER2 Challenge dataset. The scores were obtained from hospital records, which had at least two expert scores as per routine practice. Other studies may have different sources of ground truth or may involve manual scoring by pathologists.

Overall, the training data preparation in this work focuses on generating a balanced dataset of image patches from different cases of HER2-stained tissue samples, without manual segmentation or marking within the patches.

## What are the histological features observed in HER2-stained tissue samples?

The histological features observed in HER2-stained tissue samples include:
1. Stained cells: The tissue samples are observed under a microscope to identify stained cells. These cells can be either positively or negatively stained for HER2.
2. Cell membrane: The continuity and intensity of staining in the cell membrane are important features for HER2 scoring. High intensity and continuous staining of the cell membrane are scored higher, while low intensity or broken staining is scored lower.
3. Hematoxylin: Hematoxylin is a blue-colored stain that negatively stains the cells. It is one of the components of the histological features observed in HER2-stained tissue samples.
4. Diaminobenzidine (DAB): DAB is a brown-colored stain that often encircles the tumor cells with variation in intensity. It is another component of the histological features observed in HER2-stained tissue samples.
5. Stain intensity: The intensity of staining in the cell membrane is an important feature for HER2 scoring. High intensity staining is scored higher, while low intensity staining is scored lower.
6. Cell nucleus: The nucleus of the cells is also observed in HER2-stained tissue samples. However, it is not specifically mentioned in the document whether the nucleus is a histological feature used for HER2 scoring.

## Were the samples classified and scored based on the IHC standard of scoring where the samples are given scores of 0/+1/+2/+3 based on the staining characteristics?

Yes, the samples were classified and scored based on the IHC standard of scoring. The scoring system used in this study for the HER2-stained tissue samples was as follows:

- Score = 0/1+: No membrane staining or incomplete membrane staining in <10% of invasive tumor cells (0+) or faint/barely perceptible or weak incomplete membrane staining in >10% of tumor cells (1+). Clinical Significance: Negative.
- Score = 2+: A weak to moderate complete membrane stain is observed in >10% of tumor cells or strong complete membrane staining in ≤10% of tumor cells. Clinical Significance: Equivocal or borderline.
- Score = 3+: A strong (intense and uniform) complete membrane staining is observed in >10% of invasive tumor cells. Clinical Significance: Positive.

These scores were assigned based on the amount of complete or broken cell membrane and the stain intensity of the scoring, as described in the document.

## Which staining components are removed from the training dataset?

In the training dataset, the staining components that are removed are the images that have only background tissue, regions without any staining, and very small regions showing staining components. These images are not included in the training dataset to ensure that the dataset has a balanced distribution of data and includes images with significant staining components for accurate training.

## What is "decision level fusion" as described in this paper and how does it help here with her2 scoring?

"Decision level fusion" refers to the process of combining multiple individual decisions or predictions to make a final decision or prediction. In the context of this paper, decision level fusion is used to combine the scores obtained from multiple image patches to generate an overall score for the HER2-stained tissue sample.

In the proposed methodology, the HER2-stained tissue sample is divided into multiple sub-image patches. Each patch is individually classified using a pre-trained deep learning model, resulting in a patch-based score. These patch-based scores are then combined using a statistical voting mechanism called the mode operator. The mode operator selects the most frequently occurring score among the patch-based scores as the overall score for the image.

Decision level fusion helps in improving the accuracy and reliability of the HER2 scoring process. By considering multiple patches and combining their scores, the approach takes into account the heterogeneity of the HER2-stained tissue samples. It reduces the impact of variations and inconsistencies that may occur in individual patches and provides a more robust and accurate assessment of the HER2 status.

The proposed methodology section in the paper outlines the steps and techniques used in the study to develop an automated HER2 scoring system using transfer learning and decision level fusion. Here are the key takeaways from the proposed methodology:

1. Data Preparation: The dataset used in the study consisted of 172 whole-slide images (WSIs) of HER2-stained tissue samples. The dataset was divided into training and testing sets, with 30 cases used for training and 10 cases used for testing. Image patches were extracted from the training cases to generate the training dataset.

2. Proposed Methodology: The proposed methodology involved using transfer learning with pre-trained deep learning architectures (VGG16, VGG19, ResNet50, MobileNetV2, and NASNetMobile) for HER2 scoring. The last fully connected layers of the pre-trained networks were modified to classify the image patches into three output classes: negative, equivocal, and positive.

3. Data Augmentation: Data augmentation techniques were applied to increase the training dataset and reduce overfitting. Techniques such as width and height shift, shear, horizontal and vertical flip, and rotation were used.

4. Patch Classification: The pre-trained networks with modified output layers were trained on the training dataset. The training was performed for different numbers of epochs (25, 50, 75, and 100) with a batch size of 32. The training accuracy and loss were monitored.

5. Statistical Voting: The trained classifiers were tested on the testing dataset, which consisted of 100 images (800 image patches). Patch-based scoring was performed, and the scores were then combined using statistical voting with the mode operator to generate the overall image-based score.

6. Performance Metrics: The performance of the proposed approach was evaluated using various metrics such as precision, recall, F1-score, accuracy, macro accuracy, and weighted accuracy. The accuracy of the patch-based scoring and image-based scoring using statistical voting was compared.

Key Takeaways:
- The proposed methodology used transfer learning with pre-trained deep learning architectures for HER2 scoring.
- Data augmentation techniques were applied to increase the training dataset.
- The pre-trained networks were trained on the training dataset with modified output layers.
- Patch-based scoring was performed, and the scores were combined using statistical voting to generate the overall image-based score.
- The performance of the proposed approach was evaluated using various metrics.