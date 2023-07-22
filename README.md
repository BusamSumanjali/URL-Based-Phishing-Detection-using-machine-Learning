# URL-Based-Phishing-Detection-using-machine-Learning
I develop this URL-based Phishing Detection Using Machine Learning.
![image](https://github.com/BusamSumanjali/URL-Based-Phishing-Detection-using-meachine-Learning/assets/140227579/5ad7b31d-dc4e-408e-93bf-a7ace241c64a)
![image](https://github.com/BusamSumanjali/URL-Based-Phishing-Detection-using-meachine-Learning/assets/140227579/addff844-ff2c-4f02-8054-8603a9283b06)
![image](https://github.com/BusamSumanjali/URL-Based-Phishing-Detection-using-meachine-Learning/assets/140227579/57ceb552-c7e2-45ec-8d50-ef2046577f1c)
![image](https://github.com/BusamSumanjali/URL-Based-Phishing-Detection-using-meachine-Learning/assets/140227579/522c8746-14ed-48cd-8fc6-63b2712cc2c2)


## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)

## Introduction

The Internet has become an indispensable part of our life, However, It also has provided opportunities to anonymously perform malicious activities like Phishing. Phishers try to deceive their victims by social engineering or creating mockup websites to steal information such as account ID, username, password from individuals and organizations. Although many methods have been proposed to detect phishing websites, Phishers have evolved their methods to escape from these detection methods. One of the most successful methods for detecting these malicious activities is Machine Learning. This is because most Phishing attacks have some common characteristics which can be identified by machine learning methods. To see project click [here]("/").


## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Directory Tree 
```
![image](https://github.com/BusamSumanjali/URL-Based-Phishing-Detection-using-meachine-Learning/assets/140227579/357e20a3-8488-451d-bffb-81a04c8256f9)

```
## Technologies Used
* Numpy
* pandas
* matplotlib.pyplot
* sklearn
* seaborn
* flask

## Result
Accuracy of various model used for URL detection

![image](https://github.com/BusamSumanjali/URL-Based-Phishing-Detection-using-meachine-Learning/assets/140227579/9d31ccb4-5977-4002-adfb-ed2d32ba15ce)

## Conclusion
1. The final take away form this project is to explore various machine learning models, perform Exploratory Data Analysis on phishing dataset and understanding their features. 
2. Creating this notebook helped me to learn a lot about the features affecting the models to detect whether URL is safe or not, also I came to know how to tuned model and how they affect the model performance.
3. The final conclusion on the Phishing dataset is that the some feature like "HTTTPS", "AnchorURL", "WebsiteTraffic" have more importance to classify URL is phishing URL or not. 
4. Gradient Boosting Classifier correctly classify URL upto 94.01% respective classes and hence reduces the chance of malicious attachments.


