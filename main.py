from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)
vacancy = " "
region = " "

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/contacts/')
def contacts():
    author_name = 'Nadya Shanshay'
    phone_number = '+7 999 999 99 99'
    e_mail = 'shanshay@com...'
    return render_template('contacts.html', author_name=author_name, phone_number=phone_number, e_mail=e_mail)


@app.route('/form/', methods=['post', 'get'])
def form():
    global vacancy, region
    vacancy = request.form.get('vacancy')
    region = request.form.get('region')
    params = {
        'text': f'{vacancy} AND {region}'
    }
    # params = {
    #     'text': vacancy,
    #     'region': region,
    #     'page': 5
    # }
    if vacancy == None:
        vacancy = "Set the vacancy parameter"
    if region == None:
        region = "Set the city parameter"
    url = 'https://api.hh.ru/vacancies'
    results = requests.get(url, params=params).json()
    print(results)
    pprint.pprint(results)
    #count_vac = results['found']
    data = []
    for datas in range(len(results)):
        temp = {'name': results['items'][datas]['name'], 'alternate_url': results['items'][datas]['alternate_url']}
        data.append(temp)
    print(data)
    print(type(data))
    # names = []
    # alternate_urls = []
    # for items in range(len(results)):
    #     names.append(results['items'][items]['name'])
    #     alternate_urls.append(results['items'][items]['alternate_url'])
    return render_template('form.html', vacancy=vacancy, region=region, results=results, data=data)



if __name__ == "__main__":
    app.run(debug=True)

