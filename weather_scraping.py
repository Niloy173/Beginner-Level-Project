# Simple web scraping and find useful indormation 


import bs4,requests

try:

    res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78907000000004&lon=-122.39492999999999#.X4ffGdAzZPY')

    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    container = soup.find(id='seven-day-forecast-container')

    weekly_info = container.find_all(class_='tombstone-container')



    period_name = [item.find(class_='period-name').get_text() for item in weekly_info]

    desc_status = [item.find(class_='short-desc').get_text() for item in weekly_info]

    temparture_status = [item.find(class_='temp').get_text() for item in weekly_info]


    print(period_name)

    print(desc_status)

    print(temparture_status)


except Exception as e:
    print(e)
