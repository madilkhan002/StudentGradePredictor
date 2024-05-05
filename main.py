from data_preprocess import DataPreprocessing
from data_analysis import DataAnalysis
from model_training import ModelTraining

if __name__ == '__main__':
    dp = DataPreprocessing()
    da = DataAnalysis()
    mt = ModelTraining()

    df = dp.create_dataframe()

    # da.print_stats(da.mid2Summary(df))
    # da.print_stats(da.finalsSummary(df))

    # da.EDA_Mid2(df)
    # da.EDA_Finals(df)

    # mt.KNN_Mid2(df)
    # mt.KNN_Finals(df)

    # mt.DecisionTree_Mid2(df)
    # mt.DecisionTree_Finals(df)

