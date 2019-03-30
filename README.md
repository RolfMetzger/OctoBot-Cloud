# OctoBot-Cloud [0.0.1-alpha](https://github.com/Drakkar-Software/OctoBot-Cloud/tree/master/docs/CHANGELOG.md)

~~ **Project in development** ~~

### Description
OctoBot cloud runner is a web server dedicated run [OctoBot](https://github.com/Drakkar-Software/OctoBot) container in the cloud.

### Installation
- Prerequisites : 
  - [docker](https://docs.docker.com/install/)
  - [Python 3.7](https://www.python.org/downloads/)
```
git clone https://github.com/Drakkar-Software/OctoBot-Cloud
python3.7 -m pip install -r requirements
```

### Usage
```
python3.7 octobot_cloud/main.py
```

Implemented routes :
- Start a new OctoBot container : http://localhost:8080/run 
- Stop a running OctoBot container : http://localhost:8080/stop/<container_name>
