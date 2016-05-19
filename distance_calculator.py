#Slightly adapted from BV code for Python 3 (rather than 2)

import requests
requests.packages.urllib3.disable_warnings()
import csv
import sys

mode = 'driving' #driving, walking, bicycling, transit, https://developers.google.com/maps/documentation/distance-matrix/intro?hl=en#travel_modes

travel_file = 'input.txt'

api_key_1 = 'AIzaSyCTgMYtYf9RXkDLkMof6EKf7kkCpJb66qQ'
api_key_2 = 'AIzaSyDkjzfilC6YQHJmSSzuVrZCKgQka2JS4F4'
api_key_3 = 'AIzaSyD7vHv-iXn5vt5ajN5CHgC-4r01Hw-NMpM'
api_key_4 = 'AIzaSyAn4gOcAwsbBu9M5ORRNvsmka3-zdXMuuc'
api_key_5 = 'AIzaSyCTEujT4W3AxP5jnNxVuGGipFeHzc0KuTc' #node-poll
api_key_6 = 'AIzaSyBGlIo3YkqlYVxw5-dcyQaWBx1EakxwfZs' #wired-thoughts
api_key_7 = 'AIzaSyBxTmxtW-95NR1RgES_qHtjKoKz_KD50RI' #wired-thoughts

#api_key is limited to 2,500 requests a day

f = open(travel_file, 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        destination_city = row[0]
        destination_state = row[1]
        origin_city = row[2]
        origin_state = row[3]
        
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+str(origin_city)+','+str(origin_state)+'&destinations='+str(destination_city)+','+str(destination_state)+'&mode='+mode+'&units=imperial&language=en&key='+str(api_key_5)
        #print url

        response = requests.get(url)
        json_obj = response.json()
        #print json_obj
        status = json_obj['status']
        element = json_obj['rows'][0]['elements']
        
        try:
            destination_google = json_obj['destination_addresses'][0]
        except:
            destination_google = ''
        try:
            origin_google = json_obj['origin_addresses'][0]
        except:
            origin_google = ''
        try:
            duration_text = element[0]['duration']['text']
        except:
            duration_text = ''
        try:
            duration_value = element[0]['duration']['value']
        except:
            duration_value = ''
        try:
            distance_text = element[0]['distance']['text']
        except:
            distance_text = ''
        try:
            distance_value = element[0]['distance']['value']
        except:
            distance_value = ''
        
        try:
            distance_text_miles = distance_value*(0.62137/1000)
                
            if distance_text_miles > 2000.00 and destination_state == origin_state:
                error_flag = 1
            else:
                error_flag = 0
        except:
            distance_text_miles = 0.0
            error_flag = 0
        
        print(status)
        #print element
        print(destination_google.encode('utf-8'))
        print(origin_google.encode('utf-8'))
        print(duration_text)
        print(duration_value)
        print(distance_text)
        print(distance_value)
        print(error_flag)
        
        with open(r'output.txt', 'at') as txtfile:
            writer = csv.writer(txtfile, delimiter = '|', quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerow([
                destination_city,
                destination_state,
                origin_city,
                origin_state,
                status,
                duration_text,
                duration_value,
                distance_text,
                distance_text_miles,
                distance_value,
				destination_google,
                #destination_google.encode('utf-8').strip(),
                origin_google,
				#origin_google.encode('utf-8').strip(),
                error_flag
            ])
        txtfile.close()

finally:
    f.close()
