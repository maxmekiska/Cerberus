# Cerberus
Standard and Hybrid Deep Learning Multivariate-Multi-Step
(+ Univariate-Multi-Step, because why not?) Time Series Forecasting.


░█████╗░███████╗██████╗░██████╗░███████╗██████╗░██╗░░░██╗░██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██║░░░██║██╔════╝
██║░░╚═╝█████╗░░██████╔╝██████╦╝█████╗░░██████╔╝██║░░░██║╚█████╗░
██║░░██╗██╔══╝░░██╔══██╗██╔══██╗██╔══╝░░██╔══██╗██║░░░██║░╚═══██╗
╚█████╔╝███████╗██║░░██║██████╦╝███████╗██║░░██║╚██████╔╝██████╔╝
░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░


## Basics

This library aims to ease the application of deep learning models for time
series forecasting. To achieve this, the library differentiates between two
modes:

1. Univariate-Multistep forecasting
2. Multivariate-Multistep forecasting

These two main modes are further divided based on the complexity of the underlying model architectures:

1. Standard
2. Hybrid

Standard supports the following architectures:

- MLP
- LSTM
- CNN
- BI-LSTM

Hybrid supports:

- CNN-LSTM
- CNN-BI-LSTM

Please note that each model is supported by a prior input data pre-processing procedure which allows to set how many datapoints should look a model look back for a prediction, how many datapoints should be predicted into the future, how many subsequences should be considered (only for hybrid architectures) and what scaling should be applied.

The following scikit-learn scaling procedures are supported:

- StandardScaler
- MinMaxScaler
- MaxAbsScaler
- Normalizing ([0, 1])
- None (raw data input)

Trained models can furthermore be saved or loaded if the user wishes to do so.

## How to use?

Simplified workflow, more possible.

1. Univariate-Multistep forecasting

```python3
from cerberus.predictors.univarstandard import *

predictor = BasicMultStepUniVar(steps_past: int, steps_future: int, data = pd.DataFrame(), scale: str = '')

# Choose between one of the architectures:

# predictor.create_mlp(optimizer: str = 'adam')
# predictor.create_lstm(optimizer: str = 'adam')
# predictor.create_cnn(optimizer: str = 'adam')
# predictor.create_bilstm(optimizer: str = 'adam')

# Fit the predictor object
predictor.fit_model(epochs: int, show_progress: int = 1, validation_split: float = 0.20, batch_size: int = 10)

# Have a look at the model performance - MSE based, more evaluation forms might be added on architecture level in the future
predictor.show_performance()

# Make a prediction based on new unseen data
predictor.predict(data: array)

# Safe your model:
predictor.save_model()

# Load a model:
# Step 1: initialize a new predictor object with same characteristics as model to load
# Step 2: Do not pass in any data
# Step 3: Invoke the method load_model()
# optional Step 4: Use the setter method set_model_id(self, name: str) to give model a name

loading_predictor = BasicMultStepUniVar(steps_past: int, steps_future: int)
loading_predictor.load_model(location: str)
```

... to be continued
