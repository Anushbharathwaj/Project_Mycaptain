# write a Python program to accept a filename from the user and print the extension of that.
Dict ={'py':'python',
       'txt':'text',
       'cpp':'c++',
       'mp4':'MPEG-4 Video File'}

File_name = input("Input the Filename: ")
split = File_name.split(".")
Extension = split[-1]
key = Dict[Extension]
print("The extension of the file is :"+repr(key))
#written by L.Anush bharathwaj
