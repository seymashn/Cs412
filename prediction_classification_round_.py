# -*- coding: utf-8 -*-
"""prediction-classification-round*.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rSEcqhGX7sFDl4cW-drxOStE1-ND9kon

Json object where user name is key and predicted label is the value.
"""

import numpy as np
import pandas as pd
import gzip
import json

from pprint import pprint

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
turkish_stopwords = stopwords.words('turkish')

import pandas as pd
import json

def validate_category_label(label):
    """
    Validate that the category label is textual, not numeric index
    """
    # Convert to string first to handle any input type
    label_str = str(label)

    # Check if the label is purely numeric (which would indicate an index)
    if label_str.isdigit():
        raise ValueError(f"Label '{label}' appears to be a numeric index. Please use textual category labels.")

    # Check if label is empty
    if not label_str.strip():
        raise ValueError("Empty labels are not allowed")

    return label_str

def process_user_data(user_profiles_csv):
    """
    Process user profile data for classification task
    """
    df = pd.read_csv(user_profiles_csv)
    print("Available features for user classification:")
    print("\nUser Profile Features:")
    for col in df.columns:
        print(f"- {col}")

    print("\nSample of user data:")
    print(df.head())

    return df

def save_classification_predictions(predictions, round_number):
    """
    Save classification predictions in required format with validation
    predictions: dict with username as key and category as value
    """
    # Validate and clean all predictions
    validated_predictions = {}
    for username, label in predictions.items():
        try:
            # Validate and convert label to proper format
            validated_label = validate_category_label(label)
            validated_predictions[username] = validated_label
        except ValueError as e:
            print(f"Error with prediction for user {username}: {str(e)}")
            print("Please fix this prediction before continuing.")
            return None

    # All predictions are valid, save to file
    output_file = f'prediction-classification-round{round_number}.json'
    with open(output_file, 'w') as f:
        json.dump(validated_predictions, f, indent=2)
    print(f"\nSuccessfully saved classification predictions to {output_file}")
    print("All labels are in correct textual format")

if __name__ == "__main__":
    # Process user profiles
    user_df = process_user_data('user_profiles.csv')

    # Example of correct and incorrect predictions
    sample_predictions = {
        "user1": "Fashion",      # Correct: textual label
        "user2": "Travel",       # Correct: textual label
        "user3": "0",            # Incorrect: numeric index
        "user4": "Lifestyle"     # Correct: textual label
    }

    # Save predictions
    save_classification_predictions(sample_predictions, round_number=1)