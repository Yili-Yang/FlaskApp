from flask import Flask, render_template, request
import pandas as pd
import numpy as np
app = Flask(__name__)


@app.route("/404")
def page404():
    return render_template("404.html")


@app.route("/",methods=['GET','POST'])
def display_data():
    if request.method == 'POST':
        df = pd.read_csv('cleaned_asha_data.csv')
        df = df.sort_values('ReplyCount',ascending=False)
        df.iloc[1,1]= request.form['text']
    else:
        df =pd.DataFrame(columns=['Name','PostTitle','PostDes','Date','Time','ReplyCount'])
    dataRow_L = list()
    for ind, item in df.iterrows():
        dataRow_L.append(item.tolist())
    col_list = df.columns.tolist()

    return render_template("index.html", cols=len(col_list), rows=len(df), dataRow_L=dataRow_L,columnName_L=col_list)

if __name__ == "__main__":
	app.run(debug =True)
