# raisin_dataset
Using logistic regression and aequitas to find bias in data and create a model card

# Data Set Information:

Images of Kecimen and Besni raisin varieties grown in Turkey were obtained with CVS. A total of 900 raisin grains were used, including 450 pieces from both varieties. These images were subjected to various stages of pre-processing and 7 morphological features were extracted. These features have been classified using three different artificial intelligence techniques.


**Attribute Information**:

1. Area: Gives the number of pixels within the boundaries of the raisin.

2. Perimeter: It measures the environment by calculating the distance between the boundaries of the raisin and the pixels around it.

3. MajorAxisLength: Gives the length of the main axis, which is the longest line that can be drawn on the raisin.

4. MinorAxisLength: Gives the length of the small axis, which is the shortest line that can be drawn on the raisin.

5. Eccentricity: It gives a measure of the eccentricity of the ellipse, which has the same moments as raisins.

6. ConvexArea: Gives the number of pixels of the smallest convex shell of the region formed by the raisin.

7. Extent: Gives the ratio of the region formed by the raisin to the total pixels in the bounding box.


# Model card

From the above slices, we see that our model seems to perform consistently better on raisins that are smaller than average versus ones that are larger than average.

Looking at the summary statistics, we see that for nearly every measure the median is smaller than the mean. So more than 50% of our raisins are below the average which is also where our model is strongest. This indicates that we might want more data on larger raisins.

## Model details

Logistic Regresion model using default scikit-learn hyperparameters. Trained with sklearn version 0.24.1.


## Intended use

Classifying two different types of raisin from Turkey, Kecimen and Besni

## Metrics

F1 classification with a macro average of 0.85, 0.84 for the minority class, and 0.85 for the majority class.


When analyzing across data slices, model performance is higher for raisins below the average size and much lower for raisins above the average.


## Data

Raisin dataset acquired from the UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Raisin+Dataset


Originally from: Cinar I., Koklu M. and Tasdemir S., Classification of Raisin Grains Using Machine Vision and Artificial Intelligence Methods. Gazi Journal of Engineering Sciences, vol. 6, no. 3, pp. 200-209, December, 2020.


## Bias

The majority of raisins are below the average size. This could be a potential source of bias but more subject matter expertise may be necessary. Note to students: this is a useful call out, and in a real-world scenario should prompt you to engage in collaboration with subject matter experts so you can flesh this out.

