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

1. Univariate-Multistep forecasting

```python3
from cerberus.predictors.univarstandard import *
```

... to be continued 
