from flask import Flask, render_template, request
import pandas as pd
import numpy as np
app = Flask(__name__)


@app.route("/")
def test():
    age = {"Sam": 20, "Ken": 30, "Grace": 23, "Peter": 29}
    return render_template("test.html", ages=age)


@app.route("/404")
def page404():
    return render_template("404.html")


@app.route("/dataframe")
def display_data():
    df = pd.read_csv('cleaned_asha_data.csv')
    dataRow_L = list()
    for ind, item in df.iterrows():
        dataRow_L.append(item.tolist())
    col_list = df.columns.tolist()
    return render_template("tables.html", cols=len(col_list), rows=len(df), dataRow_L=dataRow_L,columnName_L=col_list)


if __name__ == "__main__":
	app.run(debug =True)
