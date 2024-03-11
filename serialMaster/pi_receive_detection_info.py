#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import socket
import pickle
import time



if __name__ == '__main__':
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('192.168.1.168', 12346)) #raspberry pi IP address
        server_socket.listen()

        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()

        try:
            print(f"Connection from {client_address}")

            while True:
                time.sleep(0.001)
                data = connection.recv(4096)
                if data:
                    info_dict = pickle.loads(data)
                    results_list = info_dict['result_list']
                    print("Results list: ", results_list)
                    xywhn_list = info_dict['xywhn_list']
                    print("xywhn_list: ", xywhn_list)
                    #print("Received dictionary: ", info_dict)
        except Exception as e:
            print(f"Error receiving data: {e}")

    except Exception as e:
        print("Closing connection")
        connection.close()
        server_socket.close()
        raise e