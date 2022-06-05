import requests

response = requests.get('http://ip-api.com/json?fields=status,message,country,countryCode,regionName,city,timezone,isp,proxy,query').json()

if response['status'] == 'fail':
    print(response['message'])
else:
    if response['proxy'] == True:
        print('Your IP address is:', response['query'], '(Proxy Detected)')
    else:
        print('Your IP Address:', response['query'])
    print('Country:', response['country'], ('(' + response['countryCode'] + ')'))
    print('Region:', (response['regionName'] + ', ' + response['city']))
    print('Time Zone:', response['timezone'])
    print('ISP:', response['isp'])