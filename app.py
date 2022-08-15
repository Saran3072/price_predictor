import streamlit as st
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse

df = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\IPL_Data(AutoRecovered).csv")
df['Type'].unique()

label_encoder = preprocessing.LabelEncoder()
df['Type']= label_encoder.fit_transform(df['Type'])
df['Type'].unique()

st.title("Price Predictor")

selection = st.sidebar.selectbox("Select the type of Player", ("Batsman", "Bowler", "All Rounder", "Wicket Keeper"))

def get_dataset(selection):
    if selection == "Batsman":
        batsman = df[df['Type'] == 1][['Name','ValueinCR', 'MatchPlayed', 'InningsBatted', 'RunsScored', '100s', '50s', 'BattingAVG', 'BattingS/R', 'CatchesTaken', 'Captaincy']].fillna(0)
        x_bat_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingDataBat.csv")
        x_bat_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingDataBat.csv")
        y_bat_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingTargetBat.csv")
        y_bat_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingTargetBat.csv")
        return x_bat_train, x_bat_test, y_bat_train, y_bat_test
    elif selection == "Bowler":
        bowler = df[df['Type'] == 2][['Name','ValueinCR', 'MatchPlayed', 'CatchesTaken', 'InningsBowled', 'EconomyRate', 'Wickets', 'BowlingAVG', '3s', '5s', 'Captaincy']].fillna(0)
        x_bowl_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingDataBowl.csv")
        x_bowl_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingDataBowl.csv")
        y_bowl_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingTargetBowl.csv")
        y_bowl_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingTargetBowl.csv")
        return x_bowl_train, x_bowl_test, y_bowl_train, y_bowl_test

    elif selection == "All Rounder":
        all_rounder = df[df['Type'] == 0][['Name', 'ValueinCR', 'MatchPlayed', 'InningsBatted', 'RunsScored', '100s', '50s', 'BattingAVG', 'BattingS/R', 'CatchesTaken', 'InningsBowled', 'EconomyRate', 'Maidens', 'Wickets', 'BowlingAVG', '3s', '5s', 'Captaincy']].fillna(0)
        x_all_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingDataAll.csv")
        x_all_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingDataAll.csv")
        y_all_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingTargetAll.csv")
        y_all_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingTargetAll.csv")
        return x_all_train, x_all_test, y_all_train, y_all_test

    elif selection == "Wicket Keeper":
        wk = df[df['Type'] == 3][['Name', 'ValueinCR', 'MatchPlayed', 'InningsBatted', 'RunsScored', '100s', '50s', 'BattingAVG', 'BattingS/R', 'CatchesTaken', 'StumpingsMade', 'Captaincy']].fillna(0)
        x_wk_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingDataWk.csv")
        x_wk_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingDataWk.csv")
        y_wk_train = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TrainingTargetWk.csv")
        y_wk_test = pd.read_csv(r"C:\Users\Sai Saran\OneDrive\Desktop\Minor Project\TestingTargetWk.csv")
        return x_wk_train, x_wk_test, y_wk_train, y_wk_test


def take_input(selection):
    if selection == "Batsman":
        matches = st.number_input("Enter Number of Matches Played:", value = 0)
        innings = st.number_input("Enter Number of Innings Played:", value = 0)
        runs = st.number_input("Enter Number of Runs Scored:", value = 0)
        centuries = st.number_input("Enter Number of Centuries:", value = 0)
        hcenturies = st.number_input("Enter Number of Half Centuries:", value = 0)
        average = st.number_input("Enter Batting Average", value = 0)
        strikerate = st.number_input("Enter Batting Strike Rate:", value = 0)
        catches = st.number_input("Enter Number of Catches taken:", value = 0)
        captain = st.number_input("Enter 1 if is or was captain else enter 0:", value = 0)
        return matches, innings, runs, centuries, hcenturies, average, strikerate, catches, captain
    elif selection == "Bowler":
        matches = st.number_input("Enter Number of Matches Played:", value = 0)
        innings = st.number_input("Enter Number of Innings Bowled:", value = 0)
        economy = st.number_input("Enter the Economy rate:", value = 0)
        wickets = st.number_input("Enter Number of Wickets:", value = 0)
        average = st.number_input("Enter Bowliing Average", value = 0)
        h3 = st.number_input("Enter 3 Wicket Hauls:", value = 0)
        h5 = st.number_input("Enter 5 Wicket Hauls:", value = 0)
        catches = st.number_input("Enter Number of Catches taken:", value = 0)
        captain = st.number_input("Enter 1 if is or was captain else enter 0:", value = 0)
        return matches, innings, economy, wickets, average, h3, h5, catches, captain
    elif selection == 'All Rounder':
        matches = st.number_input("Enter Number of Matches Played:", value = 0)
        innings_bat = st.number_input("Enter Number of Innings Played:", value = 0)
        runs = st.number_input("Enter Number of Runs Scored:", value = 0)
        centuries = st.number_input("Enter Number of Centuries:", value = 0)
        hcenturies = st.number_input("Enter Number of Half Centuries:", value = 0)
        average_bat = st.number_input("Enter Batting Average", value = 0)
        strikerate = st.number_input("Enter Batting Strike Rate:", value = 0)
        catches = st.number_input("Enter Number of Catches taken:", value = 0)
        innings_bowl = st.number_input("Enter Number of Innings Bowled:", value = 0)
        economy = st.number_input("Enter the Economy rate:" , value = 0)
        maidens = st.number_input("Enter the number of maidens: ", value = 0)
        wickets = st.number_input("Enter Number of Wickets:", value = 0)
        average_bowl = st.number_input("Enter Bowliing Average", value = 0)
        h3 = st.number_input("Enter 3 Wicket Hauls:", value = 0)
        h5 = st.number_input("Enter 5 Wicket Hauls:", value = 0)
        captain = st.number_input("Enter 1 if is or was captain else enter 0:", value = 0)
        return matches, innings_bat, runs, centuries, hcenturies, average_bat, strikerate, catches, innings_bowl, economy, maidens, wickets, average_bowl, h3, h5, captain

    elif selection == 'Wicket Keeper':
        matches = st.number_input("Enter Number of Matches Played:", value = 0)
        innings = st.number_input("Enter Number of Innings Played:", value = 0)
        runs = st.number_input("Enter Number of Runs Scored:", value = 0)
        centuries = st.number_input("Enter Number of Centuries:", value = 0)
        hcenturies = st.number_input("Enter Number of Half Centuries:", value = 0)
        average = st.number_input("Enter Batting Average", value = 0)
        strikerate = st.number_input("Enter Batting Strike Rate:", value = 0)
        catches = st.number_input("Enter Number of Catches taken:", value = 0)
        stumpings = st.number_input("Enter the Number of Stumpings: ", value = 0)
        captain = st.number_input("Enter 1 if is or was captain else enter 0:", value = 0)
        return matches, innings, runs, centuries, hcenturies, average, strikerate, catches, stumpings, captain        

x_train, x_test, y_train, y_test = get_dataset(selection)

reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)
y_bat_pred = reg.predict(x_test)



if selection == "Batsman":
    matches, innings, runs, centuries, hcenturies, average, strikerate, catches, captain = take_input(selection)
    input_bat = np.array([[matches, innings, runs, centuries, hcenturies, average, strikerate, catches, captain]])
    out_bat = reg.predict(input_bat)
    predict = st.button("Predict Price")
    if predict:
        st.subheader(f"The estimated price of the player is {out_bat[0][0]:.2f} Crores")
elif selection == "Bowler":
    matches, innings, economy, wickets, average, h3, h5, catches, captain = take_input(selection)
    input_bowl = np.array([[matches, innings, economy, wickets, average, h3, h5, catches, captain]])
    out_bowl = reg.predict(input_bowl)
    predict = st.button("Predict Price")
    if predict:
        st.subheader(f"The estimated price of the player is {out_bowl[0][0]:.2f} Crores")
elif selection == "All Rounder":
    matches, innings_bat, runs, centuries, hcenturies, average_bat, strikerate, catches, innings_bowl, economy, maidens, wickets, average_bowl, h3, h5, captain = take_input(selection)
    input_all = np.array([[matches, innings_bat, runs, centuries, hcenturies, average_bat, strikerate, catches, innings_bowl, economy, maidens, wickets, average_bowl, h3, h5, captain]])
    out_all = reg.predict(input_all)
    predict = st.button("Predict Price")
    if predict:
        st.subheader(f"The estimated price of the player is {out_all[0][0]:.2f} Crores")
elif selection == 'Wicket Keeper':
    matches, innings, runs, centuries, hcenturies, average, strikerate, catches, stumpings, captain = take_input(selection)
    input_wk = np.array([[matches, innings, runs, centuries, hcenturies, average, strikerate, catches, stumpings, captain]])
    out_wk = reg.predict(input_wk)
    predict = st.button("Predict Price")
    if predict:
        st.subheader(f"The estimated price of the player is {out_wk[0][0]:.2f} Crores")