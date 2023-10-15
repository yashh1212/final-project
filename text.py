# import bluetooth

# # MAC address of your Fireboltt Legacy smartwatch
# smartwatch_mac_address = "E6:EC:86:CB:92:06"

# def connect_to_smartwatch(mac_address):
#     try:
#         # Create a Bluetooth socket and connect to the smartwatch
#         sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#         sock.connect((mac_address, 1))
#         return sock
#     except Exception as e:
#         print("Error:", e)
#         return None

# def fetch_data_from_smartwatch(sock):
#     try:
#         # Send a command to the smartwatch to request data
#         sock.send("GET_DATA")

#         # Receive and print the data from the smartwatch
#         data = sock.recv(1024)
#         print("Data from Fireboltt Legacy Smartwatch:", data.decode("utf-8"))

#     except Exception as e:
#         print("Error:", e)

# def main():
#     # Connect to the smartwatch
#     smartwatch_socket = connect_to_smartwatch(smartwatch_mac_address)

#     if smartwatch_socket:
#         # Fetch data from the smartwatch
#         fetch_data_from_smartwatch(smartwatch_socket)

#         # Close the Bluetooth connection
#         smartwatch_socket.close()

# if __name__ == "__main__":
#     main()

# import pygatt

# Replace with the Bluetooth address of your smartwatch
from flask import Flask, render_template, send_file

app1 = Flask(__name__)

@app1.route('/')
def index():
    return render_template('text1.html')

@app1.route('/download')
def download_file():
    # Specify the path to the file you want to serve for download
    file_path = 'static/harshal_appointment.pdf'

    # Use Flask's send_file function to send the file to the client as an attachment
    return send_file(file_path, as_attachment=True, download_name='harshal_appointment.pdf')

if __name__ == '__main__':
    app1.run(debug=True)

