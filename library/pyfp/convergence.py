import re
import os
import pathlib
from pathlib import Path
from glob import glob

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

class FindData:
    """_summary_
    this is a module for plotting energy data and checking its convergence. 
    The data is obtained from a standard output file.
    The only variable needed is the filepath of the standard output where the data is written.
    """

    def __init__(self, filepath:str) -> None:
        # initial and shared values
        # filepath: path of a standard output file.
        self.filepath:str = filepath
        self.table_energy = None
        self.col = None

        # Cobandnfirm existence of file
        assert os.path.isfile(self.filepath), f"No such file or directori {self.filepath}"


    def energy_plot(
        self, save_on:pathlib.PosixPath=None
        ) -> None:
        # get table which are discribed several energy from fplo.out
        self.find_energys()
        fig = plt.figure(figsize=(6, 10), dpi=100)

        # plot for each energy
        for i, key in enumerate(self.table_energy.keys()):
            ax = fig.add_subplot(len(self.col), 1, i+1)
            ax.plot(self.table_energy[key], '--', label=key)
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc:f"{x:.2f}"))
            plt.legend()

        plt.xlabel('number of iterat')

        # save figure
        plt.savefig(str(save_on / "energys.png"))
        plt.close()


    def find_energys(self) -> pd.DataFrame: 
        # open file from the given Path(self.filepath)
        with open(self.filepath, 'r', encoding='utf8') as f:
            data = f.read()

        # data: split all sentences by line -> list[str, str, ...],  
        # energy:energy for each iterator -> list
        datas = data.split('\n')
        energy = []

        # find the energy data from fplo.out; trigger is "EE:"
        for i, l in enumerate(datas):
            if "EE" in l: 
                self.col = re.split(r' {2,}', datas[i-1])
                egs = re.split(r' {2,}', l)
                energy.append(egs)
            else:
                pass
        
        # transform to DataFrame and drop the unnecessary columns
        table_energy = pd.DataFrame(energy, columns=self.col)
        table_energy = table_energy[table_energy != r'EE:'].dropna(axis=1)

        # transform str -> float
        self.table_energy = table_energy.astype(float)

        return table_energy

if __name__ == '__main__':

    # get curent directory
    dirpath = Path(os.getcwd())
    found_path = glob(str(dirpath / "fplo.out"))

    # plot and save figures
    FindData(found_path[0]).energy_plot(save_on=dirpath)

