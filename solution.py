#!/usr/bin/python
import sys
import pandas as pd
import numpy as np

def main():
    # print command line arguments
    input_dir, output_dir = sys.argv[1:]
    predicted_result = []
    df = np.loadtxt(input_dir + '/data.data')
    df = pd.DataFrame(df, columns=['column 1', 'column 2'])
    df['result'] = 424242
    np.savetxt(output_dir + '/data.predict', np.array(df['result']))
    return 0

if __name__ == "__main__":
    main()
