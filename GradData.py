'''PART1: For all applications (records) with research experience 
and a GRE score greater than 310:
1.) Save/write only the application’s (record’s) serial number 
and the cumulative-grade-point-average (CGPA) to a new file.
2.) When all records have been processed, display (to the user 
in the Python shell) the number of records written to the file 
and provide the name of the file that was written to.
'''
try:
    output_file = open('Results.txt', 'w')
except: 
    print('File not found')
else:
    count = 0
    with open('GradAdmissions.txt', 'r') as input:
        for line in input:
            field = line.split()
            if ((field[7] == '1') and (field[1] > '310')):
                count = count + 1
                result = (field[0], field[6])
                output_file.write(str(result))
                output_file.write("\n")
        print('Number of Entries Recorded: ', count)
        print("The recorded serial number and CGPA were written to the file called Results.txt")

    output_file.close()

'''
PART 2: Determine and display (to the user in the Python shell) 
the average GRE and TOEFL scores for this dataset. 
For part 2 use the original, full dataset to determine the averages.
'''

try:
    file1 = open('GradAdmissions.txt', 'r')
except: 
    print('File not found')
else:
    count = 0
    GRE_Total = 0
    TOEFL_Total = 0
    # This will will skip the first line because it is not a number 
    # Since it a letter mathmatical functions cannot be performed
    line = file1.readline()[1:]
    for line in file1:
        field = line.split()
        GRE = (field[1].strip("\n"))
        TOEFL = (field[2].strip("\n"))

        #recusively add up the total for entries
        count = count + 1

        #recusively add up the total for GRE scores
        GRE_Total = GRE_Total + int(GRE)
        #recusively add up the total for TOEFL scores
        TOEFL_Total = TOEFL_Total + int(TOEFL)
    #calculate average of GRE
    GRE_Average = GRE_Total / count
    #calculate average of TOEFL
    TOEFL_Average = TOEFL_Total / count
    
    print("The average for the GRE scores is", GRE_Average)
    print("The average for the TOEFL scores is", TOEFL_Average)

    file1.close()