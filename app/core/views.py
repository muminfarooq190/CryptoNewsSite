from django.shortcuts import render
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def fetch_news(request):



    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b9712fec-4656-45af-8bf5-ce7681a3808b',
    }
    crypto_list = []
    session = Session()
    session.headers.update(headers)

    try:
         response = session.get(url, params=parameters)
         data = json.loads(response.text)

         for i in range(1,25):

              name = data['data'][i]['name']
              symbol = data['data'][i]['symbol']
              percentage_change_one_hour = data['data'][i]['quote']['USD']['percent_change_1h']
              percentage_change_24h = data['data'][i]['quote']['USD']['percent_change_24h']
              price = data['data'][i]['quote']['USD']['price']
              crypto = {
                'name': name,
                'symbol': symbol,
                'percentage1hr':percentage_change_one_hour,
                'price': price,
                'percentage24h':percentage_change_24h
              }

              crypto_list.append(crypto)


    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    return render(request, 'base.html', {'crypto_list':crypto_list})
