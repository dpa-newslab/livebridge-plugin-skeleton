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
from datetime import datetime
from livebridge.base import BasePost

logger = logging.getLogger(__name__)

class MyPost(BasePost):

    source = "skeleton"

    @property
    def id(self):
        """Return ID of post."""
        return self.data.get("id")

    @property
    def source_id(self):
        """Return ID of the source."""
        return self.data.get("source_id")

    @property
    def created(self):
        """Return created datetime of post."""
        return datetime.strptime(self.data["created"], "%Y-%m-%dT%H:%M:%S+00:00")

    @property
    def updated(self):
        """Return updated datetime of post."""
        return datetime.strptime(self.data["updated"], "%Y-%m-%dT%H:%M:%S+00:00")

    @property
    def is_update(self):
        """Return boolean if post was updated."""
        return bool(self.get_action() == "update")

    @property
    def is_deleted(self):
        """Return boolean if post was deleted."""
        return bool(self.get_action() == "delete")

    @property
    def is_sticky(self):
        """Return boolean if post was set to sticky."""
        return False

    def get_action(self):
        """Return action (create|update|delete|ignore) of post."""
        return "update" if self.get_existing() else "create"

