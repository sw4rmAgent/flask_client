# A script that sends POST and GET requests to server
from flask import Flask, render_template, flash, url_for, jsonify
import requests
import time

class Flask_client:
    # initialize client's class
    def __init__(self, sending_delay):
        self.delay = sending_delay

    ### ---------- POST requests ----------
    # send simple HTTP req to server
    def send_req_to_server(self, server_url):
        # make data structure
        dictToSend = {'variable_name': 'variable_value'}
        # make a POST request
        response = requests.post(server_url, json=dictToSend)
        # parse and display response
        print('response from server:', response.text)
        dictFromServer = response.json()
        print("received (json) : ", dictFromServer)

    # send json data to server via HTTP req
    def post_json_to_server(self, server_url, var_name, var_value):
        response = requests.post(server_url, json={"variable_name": var_name, "variable_value": var_value})
        if respsonse.status_code != 200:
            print("failed to send request")
        else:
            print("request successfully sent")

    ### ---------- GET requests ----------
    # retrieve json data from server via HTTP req
    def post_json_to_server(self, server_url):
        data = request.get_json()
        # further process data here


if __name__ == "__main__":
    # spawn client class
    fclient = Flask_client(sending_delay = 3)
    # define where the requests take place
    server_address = 'http://ita.eu.pythonanywhere.com:5000'
    topic_url = '/test'
    server_url = server_address + topic_url

    # send msg continuously
    max_pings = 500
    for ping in range(0, max_pings):
        # test raw msg req
        fclient.send_req_to_server(server_address + test_url)
        print(ping)
        time.sleep(fclient.delay)

        # test json msg req
        fclient.post_json_to_server(server_address + json_test_url, 'a', 10)
        # TODO : make nested json structure w. variable inputs


