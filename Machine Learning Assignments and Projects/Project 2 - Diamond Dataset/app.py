import streamlit as st
import pandas as pd
import pickle


#--------------Page configuration-------

st.set_page_config(page_title="Diamond Price Predictor", layout="centered")



#----------Load trained pipeline---------

@st.cache_resource

def load_model():
    with open("Diamond_Price_Prediction.pkl","rb") as f:
        return pickle.load(f)


model=load_model()



# ------- App title----------
st.title("💎 Diamond Price predictor app")
st.write("Predict diamond price using trained ML model")


# ------User inputs--------

carat = st.number_input("Carat",min_value=0.1,max_value=5.0,value=0.7)
cut = st.selectbox("Cut",['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox("Color",['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox("Clarity",['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'] )
depth_percentage = st.number_input("depth_percentage",value=61.5)
table = st.number_input("Table",value=55.0)
length = st.number_input("Length in mm",value=5.7)
width = st.number_input("Width in mm",value=5.7)
depth = st.number_input("Depth in mm",value=5.7)



#-----Prediction-----------

if st.button("Predict price 💸"):
    input_df=pd.DataFrame([{
        "carat":carat,
        "cut":cut,
        "color":color,
        "clarity":clarity,
        "depth_percentage":depth_percentage,
        "table":table,
        "length":length,
        "width":width,
        "depth":depth}])

    prediction=model.predict(input_df)[0]
    st.success(f"Estimated Diamond price is:{round(prediction,2)}")






