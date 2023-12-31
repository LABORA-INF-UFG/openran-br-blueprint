# ==================================================================================
#
#       Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==================================================================================

from os import getenv
from ricxappframe.xapp_frame import Xapp, rmr
from time import sleep
import signal

from .utils.constants import Constants
from .manager import *

from .handler import *
from mdclogpy import Logger
from mdclogpy import Level

class OverheadXapp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._xapp = Xapp(
            self._loop,
            rmr_port=4560,
            use_fake_sdl=bool(fake_sdl)
        ) # Registers xApp
        
        # Flag for shutting down the xApp
        self.shutdown = False

        # Registering handlers for signals
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGQUIT, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        self._xapp.logger.set_level(Level.DEBUG)

    def _handle_signal(self, signum: int, frame):
        """
        Function called when a Kubernetes signal is received that stops the xApp execution.
        """
        self._xapp.logger.info("Received signal {} to stop the xApp".format(signal.Signals(signum).name))
        self.stop()

    def _loop (self, xapp):
        """
        Function that runs in loop from the xApp start until its end
        """
        i = 1
        while not self.shutdown:
            xapp.logger.info("Looped {} times".format(i))
            i+=1
            sleep(1)

    def start(self):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """
        self._xapp.run()

    def stop(self):
        """
        can only be called if thread=True when started
        TODO: could we register a signal handler for Docker SIGTERM that calls this?
        """
        self.shutdown = True
        self._xapp.stop()
