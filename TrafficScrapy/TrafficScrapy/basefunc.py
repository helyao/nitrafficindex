# -*- coding: utf-8 -*-
import datetime

# Get current timestamp
def GetTimeStamp():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return timestamp
