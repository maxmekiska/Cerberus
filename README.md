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

- Multilayer Perceptron (MLP)
- Long short-term memory (LSTM)
- Gated recurrent unit (GRU)
- Convolutional neural network (CNN)
- Bidirectional long-short term memory (BI-LSTM)
- Bidirectional gated recurrent unit (BI-GRU)
- Encoder-Decoder long-short term memory (supported in Univariate-Multistep class)

Hybrid supports:

- Convolutional neural network + Long short-term memory (CNN-LSTM)
- Convolutional neural network + Bidirectional long-short term memory (CNN-BI-LSTM)

Please note that each model is supported by a prior input data pre-processing procedure which allows to set how many datapoints should look a model look back for a prediction, how many datapoints should be predicted into the future, how many sub-sequences should be considered (only for hybrid architectures) and what scaling should be applied.

The following scikit-learn scaling procedures are supported:

- StandardScaler
- MinMaxScaler
- MaxAbsScaler
- Normalizing ([0, 1])
- None (raw data input)

Trained models can furthermore be saved or loaded if the user wishes to do so.

## How to use?

Simplified workflows, more possible.

### Univariate Models:

1. Univariate-Multistep forecasting - Standard architectures

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
# optional Step 4: Use the setter method set_model_id(name: str) to give model a name

loading_predictor = BasicMultStepUniVar(steps_past: int, steps_future: int)
loading_predictor.load_model(location: str)
loading_predictor.set_model_id(name: str)
```

2. Univariate-Multistep forecasting - Hybrid architectures

```python3
from ceberus.predictors.univarhybrid import *

predictor = HybridMultStepUniVar(sub_seq: int, steps_past: int, steps_future: int, data = pd.DataFrame(), scale: str = '')

# Choose between one of the architectures:

# predictor.create_cnnlstm(optimizer: str = 'adam')
# predictor.create_cnnbilstm(optimizer: str = 'adam')

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
# optional Step 4: Use the setter method set_model_id(name: str) to give model a name

loading_predictor =  HybridMultStepUniVar(sub_seq: int, steps_past: int, steps_future: int)
loading_predictor.load_model(location: str)
loading_predictor.set_model_id(name: str)
```

### Multivariate Models:

1. Multivariate-Multistep forecasting - Standard architectures

```python3
from ceberus.predictors.multivarstandard import *

# please make sure that the target feature is the first variable in the feature list
predictor = BasicMultStepVar(steps_past: int, steps_future: int, data = pd.DataFrame(), features = [], scale: str = '')

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
# optional Step 4: Use the setter method set_model_id(name: str) to give model a name

loading_predictor = BasicMultStepVar(steps_past: int, steps_future: int)
loading_predictor.load_model(location: str)
loading_predictor.set_model_id(name: str)
```
2. Multivariate-Multistep forecasting - Hybrid architectures

```python3
from ceberus.predictors.multivarhybrid import *

# please make sure that the target feature is the first variable in the feature list
predictor = HybridMultStepVar(sub_seq: int, steps_past: int, steps_future: int, data = pd.DataFrame(), features:list = [], scale: str = '')

# Choose between one of the architectures:

# predictor.create_cnnlstm(optimizer: str = 'adam')
# predictor.create_cnnbilstm(optimizer: str = 'adam')

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
# optional Step 4: Use the setter method set_model_id(name: str) to give model a name

loading_predictor =  HybridMultStepUniVar(sub_seq: int, steps_past: int, steps_future: int)
loading_predictor.load_model(location: str)
loading_predictor.set_model_id(name: str)
```
