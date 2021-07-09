
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
# defining the function which will make the prediction using the data which the user inputs
def prediction(Amount, gio, weekday, thang, ngay):  
   
        # Pre-processing user input  
    if weekday == "Thứ 2":    
        weekday = 1
    elif weekday == "Thứ 3":
        weekday = 2
    elif weekday == "Thứ 4":
        weekday = 3
    elif weekday == "Thứ 5":
        weekday = 4
    elif weekday == "Thứ 6":
        weekday = 5
    elif weekday == "Thứ 7":
        weekday = 6
    else:
        weekday = 7 
    
    
    if thang == "Tháng 1":    
        thang = 1
    elif thang == "Tháng 2":
        thang = 2
    elif thang == "Tháng 3":
        thang = 3
    elif thang == "Tháng 4":
        thang = 4
    elif thang == "Tháng 5":
        thang = 5
    elif thang == "Tháng 6":
        thang = 6
    elif thang == "Tháng 7":
        thang = 7
    elif thang == "Tháng 8":
        thang = 8
    elif thang == "Tháng 9":
        thang = 9
    elif thang == "Tháng 10":
        thang = 10
    elif thang == "Tháng 11":
        thang = 11
    else:
        thang = 12 
        
        
    # Making predictions    
    prediction = classifier.predict(
        [[Amount, gio, weekday, thang, ngay]])
    
    if prediction == 1:
        pred = 'Normal Transaction'
    else:
        pred = 'Abnormal Transaction'
    return pred

# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.subheader("Fraudulent Transaction Detection System")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:#0066CC;padding:13px">
    <h1 style ="color:white;text-align:center;">Transaction Detection </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Amount = st.number_input("Số tiền")
    gio = st.number_input("Giờ", min_value=0, max_value=23, value=10,step=1, format=None, key=None)
    weekday = st.selectbox("Thứ",("Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ nhật"))
    ngay = st.number_input("Ngày", min_value=1, max_value=31, value=15, step=1, format=None, key=None)
    thang = st.selectbox("Tháng",("Tháng 1","Tháng 2","Tháng 3","Tháng 4","Tháng 5","Tháng 6","Tháng 7","Tháng 8","Tháng 9","Tháng 10","Tháng 11","Tháng 12"))
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction and store it in the variable result
    if st.button("Submit Transaction"):
        result = prediction(Amount, gio, weekday, thang, ngay)
    st.success('Is anormaly: {}'.format(result))
        
if __name__=='__main__':
    main() 
