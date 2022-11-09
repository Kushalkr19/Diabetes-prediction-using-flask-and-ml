
from flask import Flask,request,render_template
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)  ## setting up flask name


model = pickle.load(open('Diabetes_prediction_Main.pkl', 'rb'))  ##loading model


@app.route('/')             ## Defining main index route
def home():
    return render_template("index.html")   ## showing index.html as homepage


@app.route('/predict',methods=['POST'])  ## this route will be called when predict button is called
def predict():
    #int_features=[float(x) for x in request.form.values()]
    text1 = request.form['1']      ## Fetching each input field value one by one
    text2 = request.form['2'] 
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    text9 = request.form['9']
    text10 = request.form['10']
    text11 = request.form['11']
    text12 = request.form['12']
    text13 = request.form['13']
    text14 = request.form['14']
    text15 = request.form['15']
    text16 = request.form['16']
    if len(text1)==3:
        text1=1
    else:
        text1=0
    if len(text2)==3:
        text2=1
    else:
        text2=0
    if len(text3)==3:
        text3=1
    else:
        text3=0
    if len(text4)==3:
        text4=1
    else:
        text4=0
    if len(text5)==3:
        text5=1
    else:
        text5=0
    if len(text6)==3:
        text6=1
    else:
        text6=0
    if len(text7)==3:
        text7=1
    else:
        text7=0
    if len(text8)==3:
        text8=1
    else:
        text8=0
    if len(text10)==3:
        text10=1
    else:
        text10=0
    if len(text11)==3:
        text11=1
    else:
        text11=0
    if len(text12)==3:
        text12=1
    else:
        text12=0
    if len(text13)==3:
        text13=1
    else:
        text13=0
    if len(text14)==3:
        text14=1
    else:
        text14=0
    if len(text15)==3:
        text15=1
    else:
        text15=0
    if len(text16)=='male':
        text16=0
    else:
        text16=1
    text9=int(text9)
    row_df=pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,
                                text13,text14,text15,text16])])
    
        
    ### Creating a dataframe using all the values
    print(row_df)
    output=model.predict_proba(row_df)
    #output=format([0][1], 2)    ## Formating output

    if output[0][1]>0.5:
        return render_template('index.html',pred='You have a chance of diabetes\nand Probability of having Diabetes is {}'.format(output[0][1])) ## Returning the message for use on the same index.html page
    else:
        return render_template('index.html',pred='You are safe\nand Probability of having Diabetes is {}'.format(output[0][1])) 

if __name__ == '__main__':
    app.run(debug=True)          ## Running the app as debug==True