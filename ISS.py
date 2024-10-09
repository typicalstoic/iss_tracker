import urllib.request
import json
import geocoder
import webbrowser
import turtle
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open('iss.txt', 'w')
file.write('There are currently ' + str(result['number']) + ' astronauts on board: \n\n')
people = result['people']
for p in people:
    file.write(p['name'] + ' - on board' + '\n')

g = geocoder.ip('me')
file.write('\nYour current lat / long are: ' + str(g.latlng))
file.close()

webbrowser.open('iss.txt')

screen = turtle.Screen()
screen.setup(1280, 700)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("D:/Hackaton_project/Worldmap.gif")
screen.register_shape("D:/Hackaton_project/ISS.gif")

iss = turtle.Turtle()
iss.shape("D:/Hackaton_project/ISS.gif")
iss.penup()

while True:
    try:     
        url1 = "http://api.open-notify.org/iss-now.json"
        response1 = urllib.request.urlopen(url1)
        result1 = json.loads(response1.read())
       
        location1 = result1['iss_position']
        lat1 = location1['latitude']
        lon1 = location1['longitude']  

        lat1 = float(lat1)
        lon1 = float(lon1)
        print(f'\nLatitude: {lat1}')
        print(f'Longitude: {lon1}')

        iss.goto(lon1, lat1)
     
        time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")
        break

turtle.done()
