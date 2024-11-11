# EEG-based Health Analysis and Personalized Recommendations System

## Project Overview

This project presents a comprehensive system that uses **EEG signals** to provide real-time health analysis and personalized recommendations. The system processes EEG data to assess various physiological and psychological states, including:
- Mental states
- Cognitive load
- Emotions

The signals are first subjected to **biomedical signal preprocessing**, then fed into deep learning models trained on specialized datasets targeting these states. The outputs from these models are processed by a **Large Language Model (LLM)** to generate a detailed health report. This report provides cumulative insights into a person's well-being, including recommendations for:

- Personalized activities
- Dietary plans
- Medical advice

By correlating multiple EEG signals, the system can identify potential health risks and offer tailored suggestions, such as:

- Rest or sleep recommendations
- Focus and cognitive load management
- Consultation with a healthcare provider

The system offers a holistic view of a person's health, enabling them to make informed decisions for a healthier lifestyle.

![Health Report Output 1](Screenshot%202024-11-12%20015438.png)
![Health Report Output 2](Screenshot%202024-11-12%20015455.png)
![Health Report Output](Screenshot%202024-11-12%20015530.png)



## Datasets Used

1. **DREAMER Dataset**: A dataset for emotion recognition based on EEG signals. 
   - [DREAMER Dataset](https://zenodo.org/record/546113)

2. **INRIA BCI Challenge Dataset**: A dataset for brain-computer interface classification, focusing on different cognitive states and error-related potentials.
   - [INRIA BCI Challenge Dataset](https://www.kaggle.com/c/inria-bci-challenge)

## Files and Functions

- **`bcipre.py`**: Preprocessing script for the BCI dataset.
- **`bcitrain.py`**: Script to train the BCI model.
- **`bcitest.py`**: Script to test the trained BCI model.
- **`dreamerpre.py`**: Preprocessing script for the DREAMER dataset.
- **`drtrain.py`**: Script to train the DREAMER model.
- **`drtest.py`**: Script to test the trained DREAMER model.
- **`Biogpt.py`**: Inference script to get predictions from the trained models.
- **`gemini.py`**: Script to generate the health report using a large language model (LLM).
- **`htmlgen.py`**: Script to convert the health report into a visually appealing HTML page.

## Requirements

To run this project, you need the following dependencies. Install them via pip:

```bash
pip install -r requirements.txt
