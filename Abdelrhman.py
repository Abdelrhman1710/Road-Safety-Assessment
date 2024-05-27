import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the pipeline and the necessary lists
preprocessing_pipeline = joblib.load('preprocessing_pipeline.h5')
model_pipeline = joblib.load('modelpipeline.h5')
CityList = joblib.load('CityList.h5')
StateList = joblib.load('StateList.h5')
CountyList = joblib.load('CountyList.h5')
TimezoneList = joblib.load('TimezoneList.h5')
StreetList = joblib.load('StreetList.h5')
Wind_DirectionList = joblib.load('Wind_DirectionList.h5')
Weather_ConditionList = joblib.load('Weather_ConditionList.h5')
input_features = joblib.load('input.h5')

# Define the function to predict payments
def predict_payment(Street, City, County, State, Timezone, Humidity, Pressure, Visibility, Wind_Direction, Wind_Speed, Weather_Condition, Amenity, Bump, Crossing, Give_Way, Junction, No_Exit, Railway, Roundabout, Station, Stop, Traffic_Calming, Traffic_Signal, Turning_Loop, Temperature, Day, Month, Year, Hour, Minutes):
    test_df = pd.DataFrame(columns=input_features)
    test_df.at[0, 'Street'] = Street
    test_df.at[0, 'City'] = City
    test_df.at[0, 'County'] = County
    test_df.at[0, 'State'] = State
    test_df.at[0, 'Timezone'] = Timezone
    test_df.at[0, 'Humidity(%)'] = Humidity
    test_df.at[0, 'Pressure(in)'] = Pressure
    test_df.at[0, 'Visibility(mi)'] = Visibility
    test_df.at[0, 'Wind_Direction'] = Wind_Direction
    test_df.at[0, 'Wind_Speed(mph)'] = Wind_Speed
    test_df.at[0, 'Weather_Condition'] = Weather_Condition
    test_df.at[0, 'Amenity'] = Amenity
    test_df.at[0, 'Bump'] = Bump
    test_df.at[0, 'Crossing'] = Crossing
    test_df.at[0, 'Give_Way'] = Give_Way
    test_df.at[0, 'Junction'] = Junction
    test_df.at[0, 'No_Exit'] = No_Exit
    test_df.at[0, 'Railway'] = Railway
    test_df.at[0, 'Roundabout'] = Roundabout
    test_df.at[0, 'Station'] = Station
    test_df.at[0, 'Stop'] = Stop
    test_df.at[0, 'Traffic_Calming'] = Traffic_Calming
    test_df.at[0, 'Traffic_Signal'] = Traffic_Signal
    test_df.at[0, 'Turning_Loop'] = Turning_Loop
    test_df.at[0, 'Temperature(C)'] = Temperature
    test_df.at[0, 'Day'] = Day
    test_df.at[0, 'Month'] = Month
    test_df.at[0, 'Year'] = Year
    test_df.at[0, 'Hour'] = Hour
    test_df.at[0, 'Minutes'] = Minutes
    xo=preprocessing_pipeline.transform(test_df)
    result=model_pipeline.predict(xo)

    if result == 1:
       st.markdown("<h1 style='color: #008000;'>The Road is safe. Have a happy and safe trip!</h1>", unsafe_allow_html=True)
       st.write("Explanation: This Road is safe for travel. Enjoy your journey!")
    elif result == 2:
       st.markdown("<h1 style='color: #008000;'>The Road is safe but please mind your car speed.</h1>", unsafe_allow_html=True)
       st.write("Explanation: This Road is generally safe, but it's recommended to be cautious about your speed.")
    elif result == 3:
       st.markdown("<h1 style='color: #ff5733;'>The Road has many risks. Please try to take another road.</h1>", unsafe_allow_html=True)
       st.write("Explanation: This Road is risky. It's advisable to consider an alternative Road.")
    elif result == 4:
       st.markdown("<h1 style='color: #ff5733;'>Beware, it is impossible to take that Road. You must look for another Road.</h1>", unsafe_allow_html=True)
       st.write("Explanation: It's not safe to take this Road. Please find another Road.")


def main():
    st.title('Road Safety Assessment')
    st.markdown("<h1 style='color: #ff5733;'>Hello, how are you? I hope you have a happy and safe trip.</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #ff5733;'>I'm here to help you decide if you can take this Road safely or if there will be risks.</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #ff5733;'>We will discover this with some questions about this Road you will take.</h1>", unsafe_allow_html=True)
    st.write("General Explanation:")
    st.write("- A result of 'The Road is safe' indicates that the path is safe for travel.")
    st.write("- A result of 'The Road is safe but please mind your car speed' indicates that the path is generally safe, but it's recommended to be cautious about your speed.")
    st.write("- A result of 'The Road has many risks. Please try to take another road' indicates that the path is risky, and it's advisable to consider an alternative Road.")
    st.write("- A result of 'Beware, it is impossible to take that Road. You must look for another Road' indicates that it's not safe to take this path, and you should find another Road.")

    st.subheader('Please answer the following questions:')


    Street = st.selectbox('Street', StreetList)
    City = st.selectbox('City', CityList)
    County = st.selectbox('County', CountyList)
    State = st.selectbox('State', StateList)
    Timezone = st.selectbox('Timezone', TimezoneList)
    Humidity = st.slider('Humidity (%)', min_value=0, max_value=100, value=50, step=1)
    Pressure = st.slider('Pressure (in)', min_value=0, max_value=50, value=25, step=1)
    Visibility = st.slider('Visibility (mi)', min_value=0, max_value=10, value=5, step=1)
    Wind_Direction = st.selectbox('Wind Direction', Wind_DirectionList)
    Wind_Speed = st.slider('Wind Speed (mph)', min_value=0, max_value=50, value=10, step=1)
    Weather_Condition = st.selectbox('Weather Condition', Weather_ConditionList)
    Amenity = st.selectbox('Amenity', ['Yes', 'No'])
    Bump = st.selectbox('Bump', ['Yes', 'No'])
    Crossing = st.selectbox('Crossing', ['Yes', 'No'])
    Give_Way = st.selectbox('Give Way', ['Yes', 'No'])
    Junction = st.selectbox('Junction', ['Yes', 'No'])
    No_Exit = st.selectbox('No Exit', ['Yes', 'No'])
    Railway = st.selectbox('Railway', ['Yes', 'No'])
    Roundabout = st.selectbox('Roundabout', ['Yes', 'No'])
    Station = st.selectbox('Station', ['Yes', 'No'])
    Stop = st.selectbox('Stop', ['Yes', 'No'])
    Traffic_Calming = st.selectbox('Traffic Calming', ['Yes', 'No'])
    Traffic_Signal = st.selectbox('Traffic Signal', ['Yes', 'No'])
    Turning_Loop = st.selectbox('Turning Loop', ['Yes', 'No'])
    Temperature = st.slider('Temperature (C)', min_value=-30, max_value=50, value=20, step=1)
    Day = st.slider('Day', min_value=1, max_value=31, value=1, step=1)
    Month = st.slider('Month', min_value=1, max_value=12, value=1, step=1)
    Year = st.slider('Year', min_value=2016, max_value=2050, value=2016, step=1)
    Hour = st.slider('Hour', min_value=0, max_value=23, value=0, step=1)
    Minutes = st.slider('Minutes', min_value=0, max_value=59, value=0, step=1)

    if st.button('Predict'):
        result = predict_payment(Street, City, County, State, Timezone, Humidity, Pressure, Visibility, Wind_Direction, Wind_Speed, Weather_Condition, Amenity, Bump, Crossing, Give_Way, Junction, No_Exit, Railway, Roundabout, Station, Stop, Traffic_Calming, Traffic_Signal, Turning_Loop, Temperature, Day, Month, Year, Hour, Minutes)
        st.write(result)

if __name__ == '__main__':
    main()

