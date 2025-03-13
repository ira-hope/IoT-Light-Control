import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"  
TOPIC = "/student_group/light_control"

def on_message(client, userdata, message):
    command = message.payload.decode()
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

client = mqtt.Client()
client.connect(BROKER)
client.subscribe(TOPIC)
client.on_message = on_message

print("Listening for MQTT messages...")
client.loop_forever()
