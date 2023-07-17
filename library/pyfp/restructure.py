import glob
import os
import shutil
from pathlib import Path
import pandas as pd
import numpy as np


def filling(li:list, i:int):
    sz:int = len(li)
    if i < sz:
        return li[i]
    else:
        return ''

class Restructure:

    def __init__(self, dirpath:str):
        self.dir = Path(dirpath)
        self.files = glob.glob(str(self.dir/"+*"))
        self.table_files = None


    def restructure(self) -> None:
        self.make_structure()
        ind = self.table_files['term1'].to_numpy()
        upper_dir = np.unique(ind)

        out_path = self.dir / "out_files"
        os.makedirs(str(out_path), exist_ok=True)

        for d in upper_dir:
            os.makedirs(str(out_path / d), exist_ok=True)

        for f in self.table_files.values:
            os.makedirs(str(out_path/'/'.join(f[:-1])), exist_ok=True)
            shutil.move(self.dir/f[-1], out_path/'/'.join(f))


    def make_structure(self) -> pd.DataFrame:

        table_files = pd.DataFrame(
            sorted(self.files), columns=['files'], index=None
        )
        table_files = table_files['files'].str.split('/').apply(lambda x: x[-1]).to_frame()
        term = []
        for i in range(2):
            exec(f"term{i+1} = table_files['files'].str.split('.').apply(lambda x: filling(x, {i}))")
            exec(f"table_files['term{i+1}'] = term{i+1}")
            term.append(f'term{i+1}')

        self.table_files = table_files.reindex(columns=term + ['files'])
        self.table_files.sort_values(term)
        return self.table_files


if __name__ == '__main__':
    dirpath = os.getcwd()
    files = Restructure(dirpath).restructure()