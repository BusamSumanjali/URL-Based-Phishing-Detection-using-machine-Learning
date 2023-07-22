from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import json
import requests

app = Flask(__name__)
with open('Phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/inspect")
def inspect():
    return render_template("inspect.html")


@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == 'POST':
        var1 = request.form["UsingIP"]
        var2 = request.form["PrefixSuffix-"]
        var3 = request.form["SubDomains"]
        var4 = request.form["HTTPS"]
        var5 = request.form["NonStdPort"]
        var6 = request.form["HTTPSDomainURL"]
        var7 = request.form["RequestURL"]
        var8 = request.form["AnchorURL"]
        var9 = request.form["LinksInScriptTags"]
        var10 = request.form["ServerFormHandler"]
        var11 = request.form["InfoEmail"]
        var12 = request.form["AbnormalURL"]
        var13 = request.form["WebsiteForwarding"]
        var14 = request.form["StatusBarCust"]
        var15 = request.form["DisableRightClick"]
        var16 = request.form["AgeofDomain"]
        var17 = request.form["DNSRecording"]
        var18 = request.form["WebsiteTraffic"]
        var19 = request.form["PageRank"]
        var20 = request.form["GoogleIndex"]
        var21 = request.form["StatsReport"]

        # Convert the input data into a numpy array
        predict_data = np.array([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, 
                                 var11, var12,var13,var14,var15,var16,var17,var18,var19,var20,var21]).reshape(1, -1)
        # Use the loaded model to make predictions
        predict = model.predict(predict_data)

        if (predict == 1):
            return render_template('output.html', predict="safe")
        elif (predict == -1):
            return render_template('output.html', predict= "Not safe")
        else:
            return render_template('output.html', predict="Suspicious")
    return render_template("output.html")

if __name__ == "__main__":
    app.run(debug=False)
