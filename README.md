# A Smartroom Digital Twin Application based on Zigbee2Mqtt
This repository provides source code and documentation for setting up an example smartroom management with [zigbee2mqtt](https://www.zigbee2mqtt.io/). To support the interaction with this smart room via Digital Twins, a dedicated API is created.

For the smart room, the following devices are used:  Motion sensors (RC7046), Müller LED strips, Lupus 12133 power plugs and the RC7054 remote. Other devices from the same category with the same data structure used in zigbee will also work. 


## Contents of the Repository
The overall smart room DT system is separated into three different layers (see figure below). The setup and usage of each layer is documented in more detail in a dedicated sub-folder of this repository, as described below.



1. Zigbee Layer:
The first layer is the zigbee network created by the Sonoff dongle. This network is not visible through the repository and is started as a component of the    zigbee2mqtt server. The devices are connected via the Sonoff dongle. 
2. Zigbee2MQTT Layer:   
The second layer is the [zigbee2mqtt server](https://github.com/cdl-mint/smartroom-usecase/tree/master/zigbee2mqtt-server). This server uses [mosquitto](https://mosquitto.org/) to relay messages going to and coming from the end devices. The zigbee2mqtt server and mosquitto broker are combined via separate docker        images in a docker compose file. 
3. Digital Twin Layer:
The [API](https://github.com/cdl-mint/smartroom-usecase/tree/master/smartroom-api) created with python fastAPI combined with a mosquitto publisher to transmit messages to devices, the mosquitto subscriber which listens for messages, Grafana, pgadmin and the timscaledb all running in their own containers combined via a docker-compose file. The API maintains devices and stores operational data of these devices. Both structural and operational data is persisted using a [timescale database](https://www.timescale.com/). This also enables to query the history of operational data using the provided API. Besides these device management and query capabilitiesMoreover, the API also to interact with connected devices via their DTs, e.g. to turn on particular devices, or change the color of a smart light.

![Layer Graphic](/assets/images/Architektur.png)

