# A script that sends POST and GET requests to server
from flask import Flask, request, render_template, flash, url_for, jsonify
import time

class Flask_client:
    # initialize client's class
    def __init__(self, sending_delay):
        self.delay = sending_delay

    # send simple HTTP req to server
    def send_something_to_server(self, server_address):
        # make a POST request
        dictToSend = {'question': 'what is the answer?'}
        response = requests.post(server_address, json=dictToSend)
        print('response from server:', response.text)
        dictFromServer = response.json()
        print("received (json) : ", dictFromServer)


if __name__ == "__main__":
    # spawn client class
    fclient = Flask_client(sending_delay = 3)
    # define where the requests take place
    server_address = 'http://ita.eu.pythonanywhere.com:5000/test'

    # send msg continuously
    max_pings = 500
    for ping in range(0, max_pings):
        fclient.send_something_to_server(server_address)
        print(ping)
        time.sleep(fclient.delay)