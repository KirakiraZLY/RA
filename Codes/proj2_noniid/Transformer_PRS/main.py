"""
By now, I didn't make the code run on two different dataset, I'll do it later.
You should only prepare one genotype dataset and one phenotype dataset, and it will be split into train, validation, test
set automatically.
"""
import numpy as np
import argparse
import readPlink
import transformerprs
from sklearn.model_selection import train_test_split

def Args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bfile", type=str, help="the directory to read bfiles")
    parser.add_argument("--phenoFile", type=str, help="the directory to read phenotypes")
    parser.add_argument("--out", type=str, help="the directory to save the results")
    parser.add_argument("--modelSave", type=str, help="the directory to save the model")
    parser.add_argument("--modelLoad", type=str, help="the directory to load the model")
    parser.add_argument("--epoch", type=int, help="the directory to load the model")
    args = parser.parse_args()

    if hasattr(args, 'epoch'):
        args.epoch = int(args.epoch)
    return args

def main():
    args = Args()
    # print(args.bfile)
    # readPlink.tupletonp(args)

    bed_file = args.bfile + ".bed"
    bim_file = args.bfile + ".bim"
    fam_file = args.bfile + ".fam"
    
    try:
        X_seq = readPlink.ReadFilebyHail(bed_file, bim_file, fam_file)
        X_seq = X_seq[:,:,np.newaxis]
        print(X_seq.shape)
        print("Read plink files, done.")
    except FileNotFoundError:
        print(f"File not found: {args.bfile}")

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except Exception as e:
        print(f"An error occurred: {e}")
    # print(np.sum(X_seq, axis=(1, 2)))
    # print(X_seq.shape[1])
    # y_seq = np.sum(X_seq, axis=(1, 2)) + np.random.normal(0, 0.1, size=X_seq.shape[0])  # Regression task with noise
    

    y_file = args.phenoFile
    try:
        # Read data from the CSV file using NumPy
        y_seq = np.genfromtxt(y_file, delimiter=' ', skip_header=0)

        # Check the number of columns
        num_columns = y_seq.shape[1]
        print("Read phenotype files, done.")
        # If the number of columns is greater than 3, raise an exception
        if num_columns > 3:
            raise ValueError("Number of phenotype columns is greater than 3")

        # Display the first few rows of the NumPy array
        print(y_seq[:5])

    except FileNotFoundError:
        print(f"File not found: {y_file}")

    except ValueError as ve:
        print(f"ValueError: {ve}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    
    y_seq = y_seq[:,2]
    # print(y_seq[:5])
    # print(X_seq)

    print(X_seq.shape)
    print(y_seq.shape)
    X_seq = X_seq.transpose(1,0,2)
    
    

    
    X_train, X_temp, y_train, y_temp = train_test_split(X_seq, y_seq, test_size=0.4, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    # print(X_train)
    # print(y_train)
    print("Train set: 0.4, Validation set: 0.3, Test set: 0.3")
    

    
    transformerprs.DataPrepare(X_train, y_train, X_val, X_test, y_val, y_test, args)


    print("===================== Mission Completed =====================")


if __name__ == '__main__':

    main()