# VBR - VISION BEYOND REACH  [![Epitrack](http://www.epitrack.tech/images/logo.png)](http://epitrack.tech/)

### Highlights:
  - This is a **multi-class text classification (sentence classification)** problem.
  - This model was built with **CNN, RNN (LSTM and GRU) and Word Embeddings** on **Tensorflow**.

  - Input: **Descript**
  - Output: **Category**
    
### Train:
  - Command: python3 train.py train_data.file train_parameters.json
  - Example: ```python3 train.py ./data/train.csv.zip ./training_config.json```

### Predict:
  - Command: python3 predict.py ./trained_results_dir/ new_data.csv
  - Example: ```python3 predict.py ./trained_results_1489456639/ ./data/small_samples.csv```
  
### Reference:
 - [Implement a cnn for text classification in tensorflow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)

This project have a VirtualEnv called multiclassrnn for use, just run:
. ./vbr_venv/bin/activate

### Another commands:

```python3 train.py ./data/train.csv.zip ./training_config.json```

```python3 train.py ./data/dados_treinamento.csv.zip ./training_config.json```

```python3 train.py ./data/dados_treinamento.csv.zip ./training_config_small.json```

```python3 predict.py ./trained_results_1489522740/ ./data/test.csv```