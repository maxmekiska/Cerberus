from pandas import DataFrame


def pred_input(stockdatapred: DataFrame, steps_past: int,
               target: str, steps_future: int = 0) -> [(array, DataFrame)]:
    '''Helper function to prepare data input to enable model to make future predictions. Furthermore, provides real values.
       Mainly for testing model performances.
        Parameters:
            data (DataFrame): DataFrame containing all features that shall be considered for predicting the future including the target feature.
            steps_past (int): How much the model needs to look back to make a prediction.
            target (str): Target variable name.
            steps_future (int): Default to 0 but can be any number of steps into the future.

        Returns:
            X (array): Array containing data the model uses to predict into the future.
            realvalues (DataFrame): DataFrame containing real values.
    '''
    realvalues = data[target]
    data = stockdatapred.drop(target, axis=1)
    data = stockdatapred.iloc[0:steps_past]
    realvalues = realvalues.iloc[steps_past:steps_past + steps_future]
    X = []
    for i in range(len(data)):
        X.append(list(data.iloc[i]))
    return array(X), pd.DataFrame(realvalues)
