import pandas as pd
import os


# creating a sample dataset

data = {'name': ['Surya','Ashish', 'Vikas'],
      'age' : [26,25,28],
      'rank' : [1,2,3]}

df = pd.DataFrame(data)

#adding new row in the data

new_row_loc = {'name': "Deepesh", 'age': 26, 'rank' : 4}

df.loc[len(df.index)] = new_row_loc


#creating a folder and then making a directory

myfolder = 'Profile'

os.makedirs(myfolder, exist_ok = True)

file_path = os.path.join(myfolder, 'samples.csv')

#writing the data to the define file_path

df.to_csv(file_path, index = False)