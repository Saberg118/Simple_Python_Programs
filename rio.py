# This program will filter the list of Forst Files and output only the ones assocaited with Rio to a new file.

try:
    output_file = open("RioForestFires.txt", 'w')
except: 
    print("File Not Found")
else:
    count = 0
    with open("forestFires.txt", 'r') as input:
        for line in input:
            field = line.split ()
            if field[1] == "Rio":
                output_file.write(line)
                count = count + 1
    print("The total number of records is ", count)
    output_file.close()
    input.close()

# The second part of this program will look at the data from the new file created and find out what
# month had the most forest fires and how many there were
try:
    file = open("RioForestFires.txt", 'r')
except:
    print("File Not Found")
else: 
    count = 717
    JanTotal = 0
    FebTotal = 0
    MarTotal = 0
    AprTotal = 0
    MayTotal = 0
    JunTotal = 0
    JulTotal = 0
    AugTotal = 0
    SepTotal = 0
    OctTotal = 0
    NovTotal = 0
    DecTotal = 0
    
    #Get the total number of Fires for Each month and save it to a variable
    #named MonthTotal
    for line in file:
        field = line.split()
        line = line.strip()
        if field[2] == "Janeiro":
            JanTotal = JanTotal + int(field[3])
        if field[2]  == "Fevereiro":
            FebTotal = FebTotal + int(field[3])
        if field[2]  == "Março":
            MarTotal = MarTotal + int(field[3])
        if field[2]  == "Abril":
            AprTotal = AprTotal + int(field[3])
        if field[2]  == "Maio":
            MayTotal = MayTotal + int(field[3])
        if field[2]  == "Junho":
            JunTotal = JunTotal + int(field[3])
        if field[2]  == "Julho":
            JulTotal = JulTotal + int(field[3])
        if field[2]  == "Agosto":
            AugTotal = AugTotal + int(field[3])
        if field[2]  == "Setembro":
            SepTotal = SepTotal + int(field[3])
        if field[2]  == "Outubro":
            OctTotal = OctTotal + int(field[3]) 
        if field[2]  == "Novembro":
            NovTotal = NovTotal + int(field[3])
        else:
            if field[2] == "Dezembro":
                DecTotal = DecTotal + int(field[3])
    
    file.close()
    #This part of the program will find the month with the most amount of fires in Rio using the File Created
    maxFires = 0 
    months = 12
    TotalMonths = [JanTotal, FebTotal, MarTotal, AprTotal, MayTotal, JunTotal, JulTotal, AugTotal, SepTotal, OctTotal, NovTotal, DecTotal]
    for months in TotalMonths:
        if JanTotal > maxFires:
            maxFires = JanTotal
            month = "Janeiro"
        if FebTotal > maxFires:
            maxFires = FebTotal
            month = "Fevereiro"
        if MarTotal > maxFires:
            maxFires = MarTotal
            month = "Março"
        if AprTotal > maxFires:
            maxFires = AprTotal
            month = "Abril"
        if MayTotal > maxFires:
            maxFires = MayTotal
            month = "Maio"
        if JunTotal > maxFires:
            maxFires = JunTotal
            month = "Junho"
        if JulTotal > maxFires:
            maxFires = JulTotal
            month = "Julho"
        if AugTotal > maxFires:
            maxFires = AugTotal
            month = "Agosto"
        if SepTotal > maxFires:
            maxFires = SepTotal
            month = "Setembro"
        if OctTotal > maxFires:
            maxFires = OctTotal
            month = "Outubro"
        if NovTotal > maxFires:
            maxFires = NovTotal
            month = "Novembro"
        if DecTotal > maxFires:
            maxFires = DecTotal
            month = 'Dezembro'
    
    #Display the Results to the User
    print("The month of", month, "had the most fires with", maxFires, "in the state of Rio")
  
    
        
