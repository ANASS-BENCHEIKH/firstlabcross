
from flask  import Flask,render_template, request
import json

app = Flask(__name__)

@app.route('/', methods =['GET'])
def index():
    return(render_template('index.html'))

@app.route('/', methods =['POST'])
def result():
    country1 = request.form['country1']
    country2 = request.form['country2']
    country3 = request.form['country3']
    print(country1, country2, country3)
    datesCountry1 = getDates(country1)
    casesCountry1 = getCases(country1)
    deathsCounty1 = getDeaths(country1)
    print(datesCountry1)
    return(render_template('index.html',deathsCounty1=deathsCounty1,country1=country1, country2=country2, country3=country3,datesCountry1=datesCountry1,casesCountry1=casesCountry1,))

def getDates(country):
    listDates = ['12/11/2020','13/11/2020','14/11/2020','15/11/2020','16/11/2020','17/11/2020']
    return(listDates)

def getCases(country):
    listCases = [1, 3, 12, 9, 15, 10]
    return(listCases)

def getDeaths(country1):
    listDeaths = [1, 2, 1, 4, 1, 8]
    return(listDeaths)

if __name__=='__main__':
    app.run(debug= True)

