"""
Vincent Lombardi
File for extracting fafsa sequences

"""
header = "country,sequence,accession,date\n"
name = "my_sequences10.csv"
outfile = open(name, "w")
outfile.write(header)



with open('data/spikeprot1104.fasta') as f:
    lines = f.readlines()
    seq = ""
    start = True
    temp = []
    for l in lines:
        if l[0] != '>': # get sequence
            if l[-1] == '\n':
                if l[-2] == '*':
                    seq = l[:-2]
                else:
                    seq = l[:-1]
            else:
                if l[-1] == '*':
                    seq = l[:-1]
                else:
                    seq = l

        else: # get header
            tl = l.split('|')

            if start:
                start = False
                seq += ''
                temp.append(tl[2].strip(","))

                temp.append(tl[3].strip(","))
                temp.append(tl[-1][:-1].strip(",\n"))

            else:
                date = temp[0]
                d = temp[0].split("-")

                if d[1] != "00" and d[2] != "00": # check for bad dates

                    if "," not in temp[2] and "," not in seq and "," not in temp[1] and not "," in date:
                        outfile.write(temp[2] + ',' + seq + ',' + temp[1] + ',' + date + '\n')


                seq = ''
                temp = []
                temp.append(tl[2])

                temp.append(tl[3])
                temp.append(tl[-1][:-1].strip("\n"))



    date = temp[0]
    d = temp[0].split("-")
    if d[1] != "00" and d[2] != "00":

        if "," not in temp[2] and "," not in seq and "," not in temp[1] and "," not in date:

            outfile.write(temp[2] + ',' + seq + ',' + temp[1] + ',' + date + '\n')


    f.close()

outfile.close()