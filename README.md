# README: CS 412 InstaInfluencers Project

## Project Overview
This repository contains all the datasets and scripts used for the CS 412 InstaInfluencers project. Below is a description of the main files and their purpose in the project:

- **`training-dataset.jsonl.gz`**: Contains user profiles and their 36 most recent posts.
- **`train-classification.csv`**: Labels for user accounts assigned to categories.
- **`test-classification-round*.dat`**: Usernames to be classified for each round.
- **`test-regression-round*.jsonl`**: Post data for predicting like counts.
- **`prediction-classification-round*.json`**: Output predictions for classification tasks.
- **`prediction-regression-round*.json`**: Output predictions for regression tasks.
- **`json_to_csv.py`**: Converts JSON files into CSV format and splits data as needed.

---

## Methodology
This project focuses on predicting the following:

1. **Influencer Categories**: Multi-class classification of Instagram profiles into 10 categories. The features include user metadata, post content, hashtags, and engagement metrics.
   - Model: [Model type, e.g., Random Forest or BERT].
   - Features: Profile metadata, post captions, hashtags, and engagement metrics.

2. **Content Popularity**: Regression task to predict the **like_count** of posts using extracted features.
   - Model: [Model type, e.g., XGBoost or Linear Regression].
   - Features: Post content, time of posting, engagement rates, and account popularity metrics.

### Challenges Addressed:
- Imbalanced data for classification.
- Heavy-tailed distributions of like counts.
- Missing or noisy data.

### Approach:
- **Data Pre-processing**: Handling missing values, normalizing text, and feature scaling.
- **Feature Extraction**: Extracting meaningful insights from user profiles and posts.
- **Model Training**: Fine-tuning hyperparameters for optimal performance.
- **Evaluation**: Using accuracy for classification and MSE for regression tasks.

---

## Results
### Classification Results:
- **Accuracy**: [Insert performance metrics].
- **Confusion Matrix**: [Attach figure/table showing classification results].

### Regression Results:
- **MSE (log10)**: [Insert regression performance].
- **Visualizations**: [Graphs showcasing predictions vs. actual like counts].

### Observations:
- Influencers with larger followings tend to show distinct patterns in content popularity.
- Specific categories exhibit unique engagement profiles.

---

## My Contributions
1. **Seyma Sahin**:
   - Implemented the feature extraction pipeline.
   - Conducted exploratory data analysis (EDA) and visualizations.
   - Developed and fine-tuned both classification and regression models.
   - Analyzed results and prepared documentation.

---

## Instructions for Running the Code

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Convert JSON to CSV and split data**:
   ```bash
   python json_to_csv.py --input input_file.json --output output_file.csv
   ```

3. **Generate predictions for classification**:
   ```bash
   python prediction_classification.py --input test-classification-round*.dat --output prediction-classification-round*.json
   ```

4. **Generate predictions for regression**:
   ```bash
   python prediction_regression.py --input test-regression-round*.jsonl --output prediction-regression-round*.json
   ```

5. **Generate evaluation metrics**:
   ```bash
   python evaluation.py --input predictions/ --metrics accuracy mse
   ```

---

## Notes
- Make sure your predictions follow the specified formats (`prediction-classification-round*.json` and `prediction-regression-round*.json`).
- Submit the project through a public GitHub repository and ensure the URL format is correct.

---
