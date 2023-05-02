# GVE DevNet Meraki Licensing Assignment
This repository contains code that will assign licenses to unlicensed devices in a Meraki organization. The code accomplishes this by gathering all the devices and all the licenses in the organization. Then, the code checks all the licenses to make sure we only assign unassigned licenses to unlicensed devices. The unassigned licenses are then aggregated by license type which corresponds to the different device models. After all the unassigned licenses are aggregated, the code goes through the unlicensed devices and assigns the appropriate license to each one.

![/IMAGES/workflow.png](/IMAGES/workflow.png)

## Contacts
* Danielle Stacy

## Solution Components
* Python 3.11
* Meraki SDK

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).

## Installation/Configuration
1. Clone this repository with `git clone [repository name]`
2. Add Meraki API key and oranization that you are adding licenses to environment variables
```python
API_KEY = "API key goes here"
ORG_NAME = "org name goes here"
```
3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
4. Install the requirements with `pip3 install -r requirements.txt`

## Usage
To run the program, use the command:
```
$ python3 assign_licenses.py
```

# Screenshots

If a license is successfully assigned, it will print out this message.
![/IMAGES/successful_assignment.png](/IMAGES/successful_assignment.png)

If a license is not successfully assigned, it will print out an error message. In this case, there were no more licenses left of that device model.
![IMAGES/no_more_licenses.png](/IMAGES/no_more_licenses.png)

In the organization used for testing purposes, there were three licenses assigned to devices that could not be found in the organization via API call. In that case, this error message is printed out.
![/IMAGES/assigned_devices_not_in_org.png](/IMAGES/assigned_devices_not_in_org.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
