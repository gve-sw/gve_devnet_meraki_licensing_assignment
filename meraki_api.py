#!/usr/bin/env python3
"""
Copyright (c) 2022 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
import meraki
import os, sys
from dotenv import load_dotenv

# load all environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.meraki.com/api/v1"
DASHBOARD = meraki.DashboardAPI(api_key=API_KEY, base_url=BASE_URL,
                                print_console=False,
                                suppress_logging=True)


# API calls
# Organizations
def get_organizations():
    organizations = DASHBOARD.organizations.getOrganizations()

    return organizations


# Get specific organization ID
def get_org_id(org_name):
    organizations = get_organizations()
    for org in organizations:
        if org["name"] == org_name:
            return org["id"]

    return None


# Retrieve org devices
def get_org_devices(org_id):
    devices = DASHBOARD.organizations.getOrganizationDevices(org_id,
                                                             total_pages="all")

    return devices


# Retrieve organization licenses
def get_licenses(org_id):
    licenses = DASHBOARD.organizations.getOrganizationLicenses(org_id,
                                                               total_pages="all")

    return licenses


# Assign organization licenses
def assign_license(org_id, license_id, serial):
    response = DASHBOARD.organizations.updateOrganizationLicense(org_id,
                                                                 license_id,
                                                                 deviceSerial=serial)


def main(argv):
    print("This file is for defining functions. Please don't run it on its own. It doesn't do anything.")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
