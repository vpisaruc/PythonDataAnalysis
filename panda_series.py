import pandas as pd

# Part One: Panda Series Introduction
#_________________________________________________________________________________________________________________


# Create Series
lst = [2, 67, 44, 32]
print(pd.Series(lst), '\n')
lst_bool = [True, False, True, True, False]
print(pd.Series(lst_bool), '\n')

# You can pass in Series mix data type
lst_mix = ['I am in list', True, 23, 67, 23.6]
print(pd.Series(lst_mix), '\n')

# Manually fill Series
print(pd.Series(5, index=[0]), '\n')
print(pd.Series(5, index=[0, 1, 2, 3, 4]), '\n')

# Fill Series using list comprehension
print(pd.Series([x * 10 for x in range(10)]), '\n')

# Creating series by using dictionary
my_dic = {"John" : "+79690524677",
          "Mary" : "+79683125264",
          "Gram" : "+79852342154"}
print(pd.Series(my_dic), '\n')


# Part Two: Panda Series From CSV
#_________________________________________________________________________________________________________________

# Header uses for which element is interpreted like header
print(pd.read_csv('data_1.csv', header=None), '\n')
# Squeeze is used for name and datatype information
print(pd.read_csv('data_1.csv', header=None, squeeze=True), '\n')

file = pd.read_csv('data_1.csv', header=None, squeeze=True)

# file will be Series object
print(type(file), '\n')

# sep = which delimiter do we use, usecols = we chose what columns do we need
print(pd.read_csv('data_2.csv', sep=';', squeeze=True, usecols=['Open']))

# As we can see s is Seeries object
s = pd.read_csv('data_2.csv', sep=';', squeeze=True, usecols=['Open'])
print(type(s))

# Part Three: Series Attributes and Methods
#_________________________________________________________________________________________________________________

s = pd.read_csv('data_2.csv', sep=';', squeeze=True, usecols=['Open'])

# Some function

# We can see starting and last index
print(s.index, '\n')
# Redo all values from series to array
print(s.values, '\n')
# We can get type of Series object
print(s.dtypes, '\n')
# What dimensional object is that
print(s.ndim, '\n')
# If you want to find size
print(s.size, '\n')
# If you want to find all your element are unique or not
print(s.is_unique, '\n')

# Some methods

# Add prefix to your index
print(s.add_prefix('Panda'), '\n')
# Add suffix to your index
print(s.add_suffix('Panda'), '\n')
# Find some of all the values
print(s.sum(), '\n')

# Find the index of max/min value
print(s.idxmax(), '\n')
# Find max/min value
print(max(s), '\n')
# If you want some value from the top of the Series
print(s.head(5), '\n')
# If you want some values from the bottom of the Series
print(s.tail(4), '\n')
# Find average value
print(s.mean(), '\n')
# A lot of useful information about our data
print(s.describe(), '\n')


# Part Four: Label Indexing
#_________________________________________________________________________________________________________________

temperature = [11, 22, 32, 12, 23, 54, 32, 54, 23, 25, 11, 42]
months = ['Jun', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temp_by_months = pd.Series(temperature, index=months)
print(temp_by_months, '\n')


# Part Five: Inplace parameter, Sort Values, Sort indexes
#_________________________________________________________________________________________________________________

# Sort values, increase order made brand new series object, doesn't modify our series obj
print(temp_by_months.sort_values(), '\n')
# Sort values, decrease order made brand new series object, doesn't modify our series obj
print(temp_by_months.sort_values(ascending=False), '\n')
# if we wanna change our series object
temp_by_months.sort_values(ascending=False, inplace=True)
print(temp_by_months, '\n')

# If we wanna sort indexes, inplace apply permanent modification
temp_by_months.sort_index(inplace=True)
print(temp_by_months, '\n')

# Part Six: Apply Python built in Function on Series
#_________________________________________________________________________________________________________________


# We can make list of values from series
list(temp_by_months)
# We can make dictionary
dict(temp_by_months)

# Part Seven: Extract Values From Series
#_________________________________________________________________________________________________________________

# There are custom indexes in our Series object, but the also interpret like numeric indexes
print(temp_by_months[0], '\n')
# You can use slices
print(temp_by_months[1:4], '\n')
# You can take some specific values from Series
print(temp_by_months[[1, 2, 3]], '\n')
# We can take element by custom indexes
print(temp_by_months['Sep'], '\n')
# If we want more than 1 value
print(temp_by_months[['Sep', 'Oct', 'Nov']], '\n')


# Part Eight: value_couts, apply, map methods
#_________________________________________________________________________________________________________________


serMaleFem = pd.Series(['male', 'female', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'female'])

# value_counts find all uniq values and give us the count of each
print(serMaleFem.value_counts(), '\n')

# Assume that we want to convert celsius in farengeit and we have formula F = C * 1.8 +32 how we can solve it
def convertTemp(C):
    return ((C * 1.8) +32)
# After writing a function we must apply this function for each element and for this we must use apply method
print(temp_by_months.apply(convertTemp), '\n')

mapObj = {30 : 300,
          31 : 310,
          32 : 320,
          33 : 330}
# Change the elements == mapObj id other values change on NaN
print(temp_by_months.map(mapObj))