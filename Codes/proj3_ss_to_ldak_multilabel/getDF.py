import pandas as pd

def SimulateDF1():
    # Generate example DataFrames
    data1 = {'feature1_exp1': [1, "123", "1:123", 0.67,20000],
            'feature2_exp1': [2, "1", "2:1", 1.10,20000],
            'feature3_exp1': [4, "34789", "4:34789", 0.003,20000],
            'feature4_exp1': [10, "97654", "10:97654", 0.37,20000],
            'feature5_exp1': [20, "2", "20:2", 0.85,20000],
            'feature6_exp1': [22, "234", "22:234", 1.7,20000],
            'labels_exp1': ['Chr', 'Pos', 'Predictor', 'Stat', 'n']
             }
    df1 = pd.DataFrame(data1)

    data2 = { 'feature1_exp1': [3, "2", "3:2", 0.47,10000],
            'feature2_exp1': [4, "2134", "4:2134", 2.20,10000],
            'feature3_exp1': [4, "333", "4:333", 0.017,10000],
            'feature4_exp1': [6, "567", "6:567", 0.007,10000],
            'feature5_exp1': [15, "678", "15:678", 0.35,10000],
            'feature6_exp1': [18, "789564", "18:789564", 1.1,10000],
            'labels_exp1': ['Chr', 'Pos', 'Predictor', 'Stat', 'n']
             }
    df2 = pd.DataFrame(data2)

    # Combine the two DataFrames
    df_combined = pd.concat([df1, df2], axis=1)
    return df_combined

def SimulateDF():
    # Generate example DataFrames
    data1 = {'feature1_exp1': [1.1, 2.2, 3.3, 4.4],
             'feature2_exp1': [5.5, 6.6, 7.7, 8.8],
             'feature3_exp1': [9.9, 10.1, 11.2, 12.3],
             'labels_exp1': ['Chr', 'Pos', 'Predictor', 'Stat']}
    df1 = pd.DataFrame(data1)

    data2 = {'feature1_exp2': [1.0, 2.0, 3.0, 4.0],
             'feature2_exp2': [5.0, 6.0, 7.0, 8.0],
             'feature3_exp2': [10.0, 9.0, 11.0, 12.0],
             'labels_exp2': ['Chr', 'Pos', 'Predictor', 'Stat']}
    df2 = pd.DataFrame(data2)

    # Combine the two DataFrames
    df_combined = pd.concat([df1, df2], axis=1)
    return df_combined

def ReadFile():
    return