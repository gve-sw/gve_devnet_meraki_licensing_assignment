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
import meraki_api
import os, sys
from dotenv import load_dotenv
from collections import defaultdict
from pprint import pprint

# load all environment variables
load_dotenv()

ORG_NAME = os.getenv("ORG_NAME")


def usage():
    print("Usage: assign_licenses.py", file=sys.stderr)
    sys.exit(1)


def main(argv):
    # get org id
    org_id = meraki_api.get_org_id(ORG_NAME)

    # make sure org id exists
    if org_id is None:
        print("No org id was found for the given org name. Check the organization name again.")

        return

    # get devices in the given organization
    devices = meraki_api.get_org_devices(org_id)
    # organize devices to be retrievable by serial number
    device_by_serial = {}
    device_by_model = defaultdict(list)
    for device in devices:
        serial = device["serial"]
        model = device["model"]
        device_by_serial[serial] = device
        device_by_model[model].append(device)

    # get licenses in the given orgainzation
    licenses = meraki_api.get_licenses(org_id)
    # aggregate licenses according to license type
    license_by_type = defaultdict(list)
    for lic in licenses:
        lic_type = lic["licenseType"]
        lic_id = lic["id"]
        # if licence is not currently active, add it to the dict that we will go through to assign licenses
        if lic["state"] != "active":
            license_by_type[lic_type].append(lic_id)
        # otherwise check which device the license is assigned to and then remove that device from the dict of devices we will be assigning licenses to
        else:
            serial = lic["deviceSerial"]
            if serial in device_by_serial:
                del device_by_serial[serial]
            else:
                # I don't understand why a license would be assigned to a device with a serial number that doesn't return when I make the API call to get all the devices
                print("Cannot find a device with  " + serial + " that is assigned to license " + lic_id + " in this organization.")

    # loop through all the devices without licenses and assign them the appropriate license
    for serial in device_by_serial:
        model = device_by_serial[serial]["model"]
        # if device is MR model, we need ENT license assigned to it
        if "MR" in model:
            try:
                lic = license_by_type["ENT"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # if device is an MX64, then it needs an MX64-ENT license assigned to it
        elif model == "MX64":
            try:
                lic = license_by_type["MX64-ENT"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # if device is an MX64W, then it needs an MX64w-ENT license assigned to it
        elif model == "MX64W":
            try:
                lic = license_by_type["MX64W-ENT"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # if device is an MX67, then it needs an MX67-ENT license assigned to it
        elif model == "MX67":
            try:
                lic = license_by_type["MX67-ENT"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # if device is an MX250, then it needs an MX250 license assigned to it
        elif model == "MX250":
            try:
                lic = license_by_type["MX250-ENT"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # if device is an MS120-8FP, then it needs an MS120-8FP license assigned to it
        elif model == "MS120-8FP":
            try:
                lic = license_by_type["MS120-8FP"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # if device is an MS120-24P, then it needs an MS120-24P license assigned to it
        elif model == "MS120-24P":
            try:
                lic = license_by_type["MS120-24P"].pop()
                meraki_api.assign_license(org_id, lic, serial)
                print("License " + lic + " is assigned to " + serial + " which is a " + model)
            except Exception as e:
                print("There was an issue trying to assign the license " + lic + " to " + serial + " which is a " + model)
                print(e)
        # device is model that has no corresponding license
        else:
            print("No license found for device with model " + model)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
