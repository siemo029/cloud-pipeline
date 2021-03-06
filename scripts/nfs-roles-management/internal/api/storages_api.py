# Copyright 2017-2019 EPAM Systems, Inc. (https://www.epam.com/)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .base import API
from ..model.storage_model import StorageModel


class Storages(API):
    def __init__(self, config=None):
        super(Storages, self).__init__(config)

    def list(self, page, page_size):
        response_data = self.call('datastorage/permission?page={}&pageSize={}'.format(page, page_size), None)
        storages = []
        total_count = 0
        if 'payload' in response_data:
            if 'entityPermissions' in response_data['payload']:
                for storage_json in response_data['payload']['entityPermissions']:
                    storage = StorageModel.load(storage_json)
                    if storage is not None:
                        storages.append(storage)
            if 'totalCount' in response_data['payload']:
                total_count = int(response_data['payload']['totalCount'])
        return storages, total_count
