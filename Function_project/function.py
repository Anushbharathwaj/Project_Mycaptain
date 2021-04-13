## Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.
##  Use dictionaries.


A = input("Input : Please enter a string ")

all_freq = {}
for i in A:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
print("Output : ",str(sorted(all_freq.items(), key=lambda x : x[1],reverse=True)).strip("[]").replace(",","").replace("(","").replace(")","").replace("=",""))

## Expected Output
## Input : Please enter a string Mississippi
## Output :  'i' 4 's' 4 'p' 2 'M' 1
