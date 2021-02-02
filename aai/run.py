#/usr/bin/python3

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
  
#   Licensed under the Apache License, Version 2.0 (the "License").
#   You may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
  
#       http://www.apache.org/licenses/LICENSE-2.0
  
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from aai import logger
import logging

# from utils import aws
# from utils import doc
# from utils import converter

# import config as config
# from python import language_server  # noqa will suppress the linting message for this line

log = logging.getLogger('aai.main')


# def get_inventory(region_name, inventory):
#     response = aws.get(region_name=region_name, inventory=inventory)
#     dic = converter.flatten_list(response, '.')
#     return dic


def get_filters(f):
    if not f:
        return []
    filters=[]
    for od in f:
        dct={}
        for k, v in od.items():
            dct[k]=v
        filters.append(dct)
    return filters


def Execute():
    log.info('Started: AWS Auto Inventory')

    # inventories = config.settings.get_inventories()
    # regions = config.settings.config['aws']['region'].get()

    # data=[]
    # for region in regions:
    #     for inventory in inventories:
    #             result = get_inventory(region_name=region, inventory=inventory)
    #             data.append({'Inventory': inventory, 'Result': result})
    
    # doc.write_data(data)

    log.info('Finished: AWS Auto Inventory')
