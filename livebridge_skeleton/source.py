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
import asyncio
import logging
from datetime import datetime
from .post import MyPost
from livebridge.base import StreamingSource


logger = logging.getLogger(__name__)


class MySource(StreamingSource):

    type = "skeleton"

    def __init__(self, config):
        logger.debug("Skeleton config: {}".format(config))
        self.stopped = False
        self.x_id = 1

    async def listen(self, callback):
        """Implement here your stream source, and call
           'callback' with every new post."""
        while self.stopped == False:
            self.x_id += 1
            new_post = MyPost({
                "source_id": "mystream",
                "id": self.x_id,
                "text": "skeleton for id {}".format(self.x_id),
                "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                "updated": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            })
            await callback([new_post])
            await asyncio.sleep(10)
        return True

    async def stop(self):
        """Signal stream to be stopped."""
        logger.debug("Stopping skeleton source")
        self.stopped = True
        return True
