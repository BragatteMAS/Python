# -*- coding: utf-8 -*-
"""How_to_TestspeedNet.py

[Ref](https://github.com/bguerbas/SpeedTest)actor by @bragatte 202104012027 
"""

import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as np
from threading import Timer

#internet speed function saver .csv
def internet():
    df = pd.read_excel('data.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    date_now = datetime.now().strftime('%d/%m/%Y')
    hour_now = datetime.now().strftime('%H:%M')
    velocity = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [date_now, hour_now, velocity]
    df.to_excel('data.xlsx', sheet_name='base', index=False)
    Timer(1800, internet).start()

internet()