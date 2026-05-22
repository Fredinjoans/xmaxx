# sample_file = open("textfile.txt", "w+")
# sample_file.write("this is some sample text in our sample file")
# sample_file.close()

#open the file for appending the text
sample_file = open("textfile.txt", "a+")

#WRITE SOME LINES
sample_file.write("this is some more text in our sample file")
sample_file.write("this is some more sample text in our sample file")

sample_file.close()
