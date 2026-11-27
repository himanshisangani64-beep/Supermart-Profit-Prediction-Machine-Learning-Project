import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import streamlit as st  
from sklearn.model_selection import (train_test_split,cross_val_score)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_squared_error,r2_score,mean_absolute_error)



# Page Configration

st.set_page_config(page_title="Cost Price & Profit Predction App",page_icon="📊",layout="wide")
st.subheader("🛒 Supermart Profit Predction")

# Data Load
st.write("Upload File")
data=st.file_uploader("Select File",type=["csv"],label_visibility="collapsed")
if data is not None:
      
    df = pd.read_csv(data) 

    # Data Clean And Add

    df["Total Cost"] = df["Price"] * df["Quantity"]
    df["Profit"] = df["Total Cost"] - df["Sales Price"]  

    discount_rat = {"0%":0.00,"5%":0.05,"7%":0.07,"8%":0.08,"12%":0.12,"10%":0.10,"15%":0.15}
    df["New Discount"] = df["Discount"].map(discount_rat)

    # Model Train-Test
    
    x = df[["Sales Price","New Discount"]]
    y=  df["Profit"]

    x_train , x_test , y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=42)

    # Algorithem select 

    l = LinearRegression()

    l.fit(x_train,y_train)

    # Prediction 
    y_pred = l.predict(x_test)

    # train test
    y_pred_train = l.predict(x_train)

   

    # Croess Vlaue Score
    score = cross_val_score(l,x_train,y_train,cv=5,scoring='neg_mean_absolute_error')

    # SideBar
    with st.sidebar :
        st.markdown("""
        <p>Input Fratures</p>
        """,unsafe_allow_html=True)
        
        st.sidebar.markdown(
            '<hr style= " margin-top: -20px; margin-bottom: -15px; border: 1px solid #444;">'
        ,unsafe_allow_html=True)

        Sales_Amount = st.sidebar.slider("Sales Amount",max_value=500000,min_value=100000,step=10000,
                                       value=200000)
        Discount = st.sidebar.slider("Discount",max_value=20.0,min_value=1.0,value=5.0)           
    
    # Prediction Result

    c1 , c2 = st.columns(2)
    with c1:
     new1 = l.predict([[Sales_Amount,Discount/100]])
     st.metric("Estimated Profit",f"{new1[0]:,.2f}")
    with c2:
     st.metric("Model Performance",f"{r2_score(y_test,y_pred)*100:,.2f}%")
    
    col1 , col2 = st.columns(2)
    with col1:
        
        fig , ax = plt.subplots()
        ax.scatter(x_test["Sales Price"],y_test)
        ax.set_xlabel("Sales Price")
        ax.set_ylabel("Profit")
        ax.set_title("Actual Sales Price v/s  Actual Profit")
        st.pyplot(fig)

    with col2:
          
        fig , ax = plt.subplots()
        ax.scatter(x_test["Sales Price"],y_pred)
        ax.set_xlabel("Sales Price")
        ax.set_ylabel("Profit")
        ax.set_title("Sales Price v/s Prediction Profit")
        st.pyplot(fig)

    st.divider()

            
    col3 ,  col4 = st.columns(2)
    with col3:
         st.write("Prediction Error (MSE)",mean_squared_error(y_test,y_pred))
         st.write("Training Prediction Error",mean_absolute_error(y_train,y_pred_train))
         st.write("Training Performance",r2_score(y_train,y_pred_train))
    with col4:     
         st.write("Average Prediction Error:", -score.mean())
         st.write("Testing Performance",r2_score(y_test,y_pred))
         st.write("Testing Prediction Error",mean_absolute_error(y_test,y_pred))

         
         



                  
            
        
        
       

        
       








   
    
    