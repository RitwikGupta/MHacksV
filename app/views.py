from flask import render_template, flash, redirect, request
from app import app
import urllib2
import xmltodict
from string import split

@app.route('/')
@app.route('/index')
def index():
    return render_template("main.html")

@app.route('/two.html', methods=['POST'])
def index_post():
    text = request.form['inputcountry']
    disDic = dict()
    statesGlobalVar = list(text)
    def query(q, key="PA5U8P-6XX65RA456"):
        return urllib2.urlopen('http://api.wolframalpha.com/v2/query?appid=%s&input=%s&format=plaintext' % (key,urllib2.quote(q))).read()

    def state_query(group_name, states=statesGlobalVar):
        results = {s: xmltodict.parse(query('%s of %s?' % (group_name, s))) for s in states}
        results = {s: [p for p in v['queryresult']['pod'] if p['@title'] == 'Result'][0]['subpod']['plaintext'] for s,v in results.items()}
        results = {s: float(split(v)[0])*(1000000 if 'million' in v else 1) for s,v in results.items()}
        return result

    #pop = state_query('population')

    with open("app/code/dataout.csv", "r") as f:
        for line in f:
            arr = line.strip().split(",")
            arr[1] = arr[1].strip()
            if "Congenital" in arr[0] or "Neonatal" in arr[0]:
                continue
            if "Rubella" in arr[0]:
                arr[0] += " - MMR/MMRV"
            elif "encephalitis" in arr[0]:
                arr[0] += " - Ixiaro"
            elif "Measles" in arr[0]:
                arr[0] += " - MMR/MMRV"
            elif "Mumps" in arr[0]:
                arr[0] += " - MMR/MMRV"
            elif "Poliomyelitis" in arr[0]:
                arr[0] += " - IPV/OPV"
            elif "Tuberculosis" in arr[0]:
                arr[0] += " - BCG"
            elif "Diphtheria" in arr[0]:
                arr[0] += " - DTaP/Td/Tdap"
            elif "Tetanus" in arr[0]:
                arr[0] += " - DTaP/Td/Tdap"
            elif "Pertussis" in arr[0]:
                arr[0] += " - DTaP/Td/Tdap"
            elif "Yellow" in arr[0]:
                arr[0] += " - Yellow Fever Vaccine"
            elif "Meningitis" in arr[0]:
                arr[0] += " - Meningococcal Polysaccharide/conjugate vaccines"
            elif "H5N1" in arr[0]:
                arr[0] += " - H5N1 Monovalent"
            else:
                arr[0] += " - None available"
            if arr[1] in disDic.keys():
                if arr[0] not in disDic[arr[1]]:
                    disDic[arr[1]].append(arr[0])
            else:
                disDic[arr[1]] = list()
                disDic[arr[1]].append(arr[0])

    return render_template("two.html", country=text, disDic=disDic)

# dataset = dataout.csv
# datarisk = dataout_risk.csv
# datadisease = dataout_disease.csv

@app.route('/diseases', methods=['GET', 'POST']) #necessary?

# country == raw_input("Please enter the name of a country") #or input from Dan

#output country name

def disease_output(country):
    for a in datadisease:
        if country == a:
            disease = a[key]
            def cleanup(disease):
                cleanlist = disease.split()
                newlist = list()
                for b in cleanlist:
                    if b != "-" or "number" or "of" or "reported" or "cases":
                        newlist.append(b)
                disease_list = " ".join(newlist)
            print disease_list

def risk_output(country):
    #call wolfram api here?
    #http://api.wolframalpha.com/v2/query?appid=xxx&input=population%20of%20countries&format=image,plaintext
    #call the population of each country based on the api
    for a in datarisk:
        if country == a:
            risk == a[key]#population of country
            if risk >= 0.0004:
                print "High risk"
            elif risk >= 0.00015:
                print "Moderate risk"
            else:
                print "Low risk"
