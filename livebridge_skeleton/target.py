# -*- coding: utf-8 -*-
#
# Copyright 2016 dpa-infocom GmbH
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
import logging
from livebridge.base import BaseTarget, TargetResponse


logger = logging.getLogger(__name__)


class MyTarget(BaseTarget):

    type = "skeleton" 

    def __init__(self, config):
        self.target_id = "{}-{}".format(self.type, config.get("target_id"))
        self.x_id = 0

    async def _do_action(self, url, data):
        logger.debug("Calling imaginary API with {} {}".format(url, data))
        self.x_id += 1
        demo_resp = {
            "status": "OK",
            "id": self.x_id,
            "body": "Demotext",
        }
        return demo_resp

    async def post_item(self, post):
        """Build your request to create post at service."""
        create_url = "/api/create"
        data = {"text": post.content}
        return TargetResponse(await self._do_action(create_url, data))

    async def update_item(self, post):
        """Build your request to update post at service."""
        update_url = "/api/update"
        data = {"text": post.content, "id": post.data.get("id")}
        return TargetResponse(await self._do_action(update_url, data))

    async def delete_item(self, post):
        """Build your request to update post at service."""
        delete_url = "/api/update"
        data = {"id": post.data.get("id")}
        return TargetResponse(await self._do_action(delete_url, data))

    async def handle_extras(self, post):
        """Do exta actions here if needed.
           Will be called after methods above."""
        return None

