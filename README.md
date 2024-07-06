# Color Prediction for Dark Images

## Overview
This project enhances color prediction for dark images by incorporating image enhancement techniques. The original color prediction code is taken from [LakshmanKishore's colorNamePrediction repository](https://github.com/LakshmanKishore/colorNamePrediction) and improved with custom image enhancement code.

## Method
The study recommends improving unsatisfactory light pictures using Contrast Limited Adaptive Histogram Equalization (CLAHE) and incorporating K-Nearest Neighbors (KNN) for color recognition. The following steps are implemented:

1. **Convert the image into LAB color space** to separate the lightness (L) from color information (A and B channels).
2. **Apply CLAHE** to the L channel to increase contrast and brighten regions.
3. **Combine the regular A and B channels** with the refined L channel to recapture the original image.
4. **Use a pre-trained KNN model** to predict RGB pixel values of colors. The model works by finding the nearest match from a list of color names and their RGB values.
5. **Compute the absolute difference** between input RGB values and the training data to make predictions based on the closest match.
6. **User-friendly interface** for easier color selection and analysis.

## Dataset Description
The dataset `colorName.csv` contains 866 colors with columns for color name, hexadecimal number, and RGB values. Preparing the data involves:
- Examining and standardizing image noise.
- Separating data into three portions: training, validation, and testing.
- Achieving variety in the dataset through light variations, noise injection, and image rotation.

## Implementation
1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/YourRepoName.git
    ```
2. Navigate to the project directory:
    ```bash
    cd YourRepoName
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the project:
    ```bash
    python main.py
    ```

## How It Works
1. **Image Enhancement**: Convert the image to LAB color space, apply CLAHE to the L channel, and recombine with A and B channels.
2. **Color Prediction**: Use KNN to predict the RGB values and color names based on the refined image.
3. **User Interface**: Provides a simple click-to-identify color name and RGB values feature.

## Results
Before:
![IMG_0078](https://github.com/Vinithra02/Color-predictor-for-Dark-Images/assets/141245778/717d7b4c-d82c-496f-b261-70a4b9e47296)

After:
![image](https://github.com/Vinithra02/Color-predictor-for-Dark-Images/assets/141245778/24192d16-8d91-4163-85b8-17666acc996b)

## Conclusion
This project combines image enhancement techniques and KNN-based color prediction to provide accurate color recognition for dark images. The system ensures improved contrast and brightness, facilitating better color analysis and selection.

## Acknowledgements
The color prediction code is based on the work from [LakshmanKishore's colorNamePrediction repository](https://github.com/LakshmanKishore/colorNamePrediction).
