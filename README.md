MQTT Light Control Project

This project simulates an IoT light control system using MQTT.

Features

Web interface with ON/OFF buttons

MQTT communication via WebSockets

Python script simulating an IoT device

Setup Instructions

Prerequisites

Ensure you have the following installed:

Node.js

Python

Backend Setup

Clone the repository:

git clone https://github.com/ira-hope/IoT-Light-Control.git
cd IoT-Light-Control

Install Node.js dependencies:

npm install

Start the server:

node server.js

Frontend Setup

Open index.html in a web browser.

Ensure you are connected to the MQTT broker.

MQTT Broker

This project uses a public MQTT broker: wss://test.mosquitto.org:8081/mqtt

Running the IoT Simulation

Install Python dependencies:

pip install paho-mqtt

Run the light simulation script:

python light_simulation.py

Usage

Click "Turn ON" to send an MQTT message to turn the light on.

Click "Turn OFF" to send an MQTT message to turn the light off.

The UI updates based on the last command sent.

Contributing