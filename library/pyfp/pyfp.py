import re
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class FindData:
    def __init__(self, filepath:str) -> None:
        # initial and shared values
        self.filepath:str = filepath
        self.energys = None
        self.col = None

        assert os.path.isfile(self.filepath), f"No such file or directori {self.filepath}"


    def energy_plot(self) -> None:
        # get table which are discribed several energy from fplo.out
        self.find_energys()
        fig = plt.figure(figsize=(6, 10), dpi=100)

        # plot
        for i, key in enumerate(self.energys.keys()):
            ax = fig.add_subplot(len(self.col), 1, i+1)
            ax.plot(self.energys[key], '--', label=key)
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc:int(x)))
            plt.legend()

        plt.xlabel('number of iterat')


    def find_energys(self) -> pd.DataFrame: 
        # open file from the given Path(self.filepath)
        with open(self.filepath, 'r', encoding='utf8') as f:
            data = f.read()
        datas = data.split('\n')
        energy = []

        # find the energy data from fplo.out; trigger is "EE:"
        for i, l in enumerate(datas):
            if "EE" in l: 
                self.col = re.split(r'  +', datas[i-1])
                egs = re.split(r'  +', l)
                energy.append(egs)
            else:
                pass
        
        # transform to DataFrame and drop the unnecessary columns
        energys = pd.DataFrame(energy, columns=self.col, index=None, )
        energys = energys.drop(columns='')
        self.energys = energys.astype(float)

        return energys

