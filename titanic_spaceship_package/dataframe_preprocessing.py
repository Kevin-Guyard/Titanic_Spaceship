import pandas as pd
import numpy as np

def dataframe_preprocessing(df_train, df_test):
    
    def complete_missing_home_planet_using_deck(row):
        if pd.notna(row.HomePlanet):
            home_planet = row.HomePlanet
        elif pd.isna(row.CabinDeck):
            home_planet = row.HomePlanet
        elif row.CabinDeck in ['A', 'B', 'C', 'T']:
            home_planet = 'Europa'
        elif row.CabinDeck in ['G']:
            home_planet = 'Earth'
        else:
            home_planet = row.HomePlanet
        return home_planet
    
    df_train["GroupId"] = df_train.PassengerId.apply(lambda passenger_id: passenger_id.split('_')[0])
    df_train["PassengerGroupNumber"] = df_train.PassengerId.apply(lambda passenger_id: passenger_id.split('_')[1])
    df_test["GroupId"] = df_test.PassengerId.apply(lambda passenger_id: passenger_id.split('_')[0])
    df_test["PassengerGroupNumber"] = df_test.PassengerId.apply(lambda passenger_id: passenger_id.split('_')[1])
    
    df_train["CabinDeck"] = df_train.Cabin.apply(lambda cabin: cabin.split('/')[0] if pd.notna(cabin) else cabin)
    df_train["CabinSide"] = df_train.Cabin.apply(lambda cabin: cabin.split('/')[2] if pd.notna(cabin) else cabin)
    df_test["CabinDeck"] = df_test.Cabin.apply(lambda cabin: cabin.split('/')[0] if pd.notna(cabin) else cabin)
    df_test["CabinSide"] = df_test.Cabin.apply(lambda cabin: cabin.split('/')[2] if pd.notna(cabin) else cabin)
    
    group_home_planet_mapping = {row.GroupId: row.HomePlanet for _, row in pd.concat([df_train, df_test]) \
                                                                             .groupby(by=["GroupId"], axis=0, as_index=False)["HomePlanet"] \
                                                                             .first()
                                                                             .iterrows()}

    group_home_planet_mapping = {key: value if value != None else np.nan for key, value in group_home_planet_mapping.items()}

    df_train["HomePlanet"] = df_train.apply(lambda row: row.HomePlanet if pd.notna(row.HomePlanet) else group_home_planet_mapping.get(row.GroupId, row.HomePlanet), axis=1)
    df_test["HomePlanet"] = df_test.apply(lambda row: row.HomePlanet if pd.notna(row.HomePlanet) else group_home_planet_mapping.get(row.GroupId, row.HomePlanet), axis=1)
    
    df_train.HomePlanet = df_train.apply(complete_missing_home_planet_using_deck, axis=1)
    df_test.HomePlanet = df_test.apply(complete_missing_home_planet_using_deck, axis=1)
    
    X_train = df_train.drop(columns=["PassengerId", "Cabin", "GroupId", "PassengerGroupNumber", "Name", "Transported"])
    X_test = df_test.drop(columns=["PassengerId", "Cabin", "GroupId", "PassengerGroupNumber", "Name"])
    y_train = df_train["Transported"]
    list_passenger_id = df_test["PassengerId"]
    
    return X_train, X_test, y_train, list_passenger_id
    
    