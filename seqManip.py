A1DNA="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"

print(A1DNA)
aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg

#Assignment 1 original DNA sequence

print(len(A1DNA)) #Length of original DNA sequence
620

A1RNA = A1DNA.replace('t','u')
Out[19]: 'aaaagcuaucgggcccauaccccaaacauguugguuaaaccccuuccuuugcuaauuaauccuuacgcuaucuccaucauuaucuccagcuuagcccugggaacuauuacuacccuaucaagcuaccauugaauguuagccugaaucggccuugaaauuaacacucuagcaauuauuccucuaauaacuaaaacaccucacccucgagcaauugaagccgcaacuaaauacuucuuaacacaagcagcagcaucugccuuaauucuauuugcaagcacaaugaaugcuugacuacuaggagaaugagccauuaauacccacauuaguuauauuccaucuauccuccucuccaucgcccuagcgauaaaacugggaauugcccccuuucacuucugacuuccugaaguccuacaaggauuaaccuuacaaaccggguuaaucuuaucaacaugacaaaaaaucgccccaauaguuuuacuuauucaacuaucccaaucuguagaccuuaaucuaauauuauuccucggcuuacuuucuacaguuauuggcggaugaggagguauuaaccaaacccaaauucguaaaguccuagcauuuucaucaaucgcccaccuaggcug'

>>> ComplementA1DNA = A1DNA.translate(A1DNA)
>>> ComplementA1DNA
'ttttcgatagcccgggtatggggtttgtacaaccaatttggggaaggaaacgattaattaggaatgcgatagaggtagtaatagaggtcgaatcgggacccttgataatgatgggatagttcgatggtaacttacaatcggacttagccggaactttaattgtgagatcgttaataaggagattattgattttgtggagtgggagctcgttaacttcggcgttgatttatgaagaattgtgttcgtcgtcgtagacggaattaagataaacgttcgtgttacttacgaactgatgatcctcttactcggtaattatgggtgtaatcaatataaggtagataggaggagaggtagcgggatcgctattttgacccttaacgggggaaagtgaagactgaaggacttcaggatgttcctaattggaatgtttggcccaattagaatagttgtactgttttttagcggggttatcaaaatgaataagttgatagggttagacatctggaattagattataataaggagccgaatgaaagatgtcaataaccgcctactcctccataattggtttgggtttaagcatttcaggatcgtaaaagtagttagcgggtggatccgac'

>>> def reverse(dna):
    #Reversing the sequence string by creating a list
    List_nucleotides=list(dna)
    #Creating a list of the nucleotides; each nucleotide is a single variable in the list
    List_nucleotides.reverse()
    #Reversing the list of nucleotides
    return ''.join(List_nucleotides)
    #Making the list back into a string without separation

>>> RComplementA1DNA=reverse(ComplementA1DNA)

>>> RComplementA1DNA
Out[43]: 'cagcctaggtgggcgattgatgaaaatgctaggactttacgaatttgggtttggttaatacctcctcatccgccaataactgtagaaagtaagccgaggaataatattagattaaggtctacagattgggatagttgaataagtaaaactattggggcgattttttgtcatgttgataagattaacccggtttgtaaggttaatccttgtaggacttcaggaagtcagaagtgaaagggggcaattcccagttttatcgctagggcgatggagaggaggatagatggaatataactaatgtgggtattaatggctcattctcctagtagtcaagcattcattgtgcttgcaaatagaattaaggcagatgctgctgcttgtgttaagaagtatttagttgcggcttcaattgctcgagggtgaggtgttttagttattagaggaataattgctagagtgttaatttcaaggccgattcaggctaacattcaatggtagcttgatagggtagtaatagttcccagggctaagctggagataatgatggagatagcgtaaggattaattagcaaaggaaggggtttaaccaacatgtttggggtatgggcccgatagctttt'

>>> def codons(dna):
    #Codon partitioning in DNA sequence
    end = len(dna) - (len(dna)%3)-1
    codons = [dna[i:i+3] for i in range(0,end,3)]
    return codons

>>> List_codons=codons('aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg')

>>> List_codons
Out[16]: 
['aaa',
 'agc',
 'tat',
 'cgg',
 'gcc',
 'cat',
 'acc',
 'cca',
 'aac',
 'atg',
 'ttg',
 'gtt',
 'aaa',
 'ccc',
 'ctt',
 'cct',
 'ttg',
 'cta',
 'att',
 'aat',
 'cct',
 'tac',
 'gct',
 'atc',
 'tcc',
 'atc',
 'att',
 'atc',
 'tcc',
 'agc',
 'tta',
 'gcc',
 'ctg',
 'gga',
 'act',
 'att',
 'act',
 'acc',
 'cta',
 'tca',
 'agc',
 'tac',
 'cat',
 'tga',
 'atg',
 'tta',
 'gcc',
 'tga',
 'atc',
 'ggc',
 'ctt',
 'gaa',
 'att',
 'aac',
 'act',
 'cta',
 'gca',
 'att',
 'att',
 'cct',
 'cta',
 'ata',
 'act',
 'aaa',
 'aca',
 'cct',
 'cac',
 'cct',
 'cga',
 'gca',
 'att',
 'gaa',
 'gcc',
 'gca',
 'act',
 'aaa',
 'tac',
 'ttc',
 'tta',
 'aca',
 'caa',
 'gca',
 'gca',
 'gca',
 'tct',
 'gcc',
 'tta',
 'att',
 'cta',
 'ttt',
 'gca',
 'agc',
 'aca',
 'atg',
 'aat',
 'gct',
 'tga',
 'cta',
 'cta',
 'gga',
 'gaa',
 'tga',
 'gcc',
 'att',
 'aat',
 'acc',
 'cac',
 'att',
 'agt',
 'tat',
 'att',
 'cca',
 'tct',
 'atc',
 'ctc',
 'ctc',
 'tcc',
 'atc',
 'gcc',
 'cta',
 'gcg',
 'ata',
 'aaa',
 'ctg',
 'gga',
 'att',
 'gcc',
 'ccc',
 'ttt',
 'cac',
 'ttc',
 'tga',
 'ctt',
 'cct',
 'gaa',
 'gtc',
 'cta',
 'caa',
 'gga',
 'tta',
 'acc',
 'tta',
 'caa',
 'acc',
 'ggg',
 'tta',
 'atc',
 'tta',
 'tca',
 'aca',
 'tga',
 'caa',
 'aaa',
 'atc',
 'gcc',
 'cca',
 'ata',
 'gtt',
 'tta',
 'ctt',
 'att',
 'caa',
 'cta',
 'tcc',
 'caa',
 'tct',
 'gta',
 'gac',
 'ctt',
 'aat',
 'cta',
 'ata',
 'tta',
 'ttc',
 'ctc',
 'ggc',
 'tta',
 'ctt',
 'tct',
 'aca',
 'gtt',
 'att',
 'ggc',
 'gga',
 'tga',
 'gga',
 'ggt',
 'att',
 'aac',
 'caa',
 'acc',
 'caa',
 'att',
 'cgt',
 'aaa',
 'gtc',
 'cta',
 'gca',
 'ttt',
 'tca',
 'tca',
 'atc',
 'gcc',
 'cac',
 'cta',
 'ggc']
 
 >>> print(List_codons[12:14])
['aaa', 'ccc']
 
>>> VertMitCodonsUp="TTTTTCTTATTGTCTTCCTCATCGTATTACTAATAGTGTTGCTGATGGCTTCTCCTACTGCCTCCCCCACCGCATCACCAACAGCGTCGCCGACGGATTATCATAATGACTACCACAACGAATAACAAAAAGAGTAGCAGAAGGGTTGTCGTAGTGGCTGCCGCAGCGGATGACGAAGAGGGTGGCGGAGGG"

>>> VertmitCodons=VertMitCodonsUp.lower()

>>> print(VertmitCodons)
tttttcttattgtcttcctcatcgtattactaatagtgttgctgatggcttctcctactgcctcccccaccgcatcaccaacagcgtcgccgacggattatcataatgactaccacaacgaataacaaaaagagtagcagaagggttgtcgtagtggctgccgcagcggatgacgaagagggtggcggaggg

>>> List_VertmitCodons=codons(VertmitCodons)

>>> print(List_VertmitCodons)
['ttt', 'ttc', 'tta', 'ttg', 'tct', 'tcc', 'tca', 'tcg', 'tat', 'tac', 'taa', 'tag', 'tgt', 'tgc', 'tga', 'tgg', 'ctt', 'ctc', 'cta', 'ctg', 'cct', 'ccc', 'cca', 'ccg', 'cat', 'cac', 'caa', 'cag', 'cgt', 'cgc', 'cga', 'cgg', 'att', 'atc', 'ata', 'atg', 'act', 'acc', 'aca', 'acg', 'aat', 'aac', 'aaa', 'aag', 'agt', 'agc', 'aga', 'agg', 'gtt', 'gtc', 'gta', 'gtg', 'gct', 'gcc', 'gca', 'gcg', 'gat', 'gac', 'gaa', 'gag', 'ggt', 'ggc', 'gga', 'ggg']

>>> definitions={"F":[List_VertmitCodons[0],List_VertmitCodons[1]],"L":[List_VertmitCodons[2],List_VertmitCodons[3],List_VertmitCodons[16],List_VertmitCodons[17],List_VertmitCodons[18],List_VertmitCodons[19]],"S":[List_VertmitCodons[4],List_VertmitCodons[5],List_VertmitCodons[6],List_VertmitCodons[7],List_VertmitCodons[44],List_VertmitCodons[45]],"Y":[List_VertmitCodons[8],List_VertmitCodons[9]],"*":[List_VertmitCodons[10],List_VertmitCodons[11],List_VertmitCodons[46], List_VertmitCodons[47]],"C":[List_VertmitCodons[12],List_VertmitCodons[13]],"W":[List_VertmitCodons[14],List_VertmitCodons[15]],"P":[List_VertmitCodons[20],List_VertmitCodons[21],List_VertmitCodons[22],List_VertmitCodons[23]],"H":[List_VertmitCodons[24],List_VertmitCodons[25]],"Q":[List_VertmitCodons[26],List_VertmitCodons[27]],"R":[List_VertmitCodons[28],List_VertmitCodons[29],List_VertmitCodons[30],List_VertmitCodons[31]],"I":[List_VertmitCodons[32],List_VertmitCodons[33]],"M":[List_VertmitCodons[34],List_VertmitCodons[35]],"T":[List_VertmitCodons[36],List_VertmitCodons[37],List_VertmitCodons[38],List_VertmitCodons[39]],"N":[List_VertmitCodons[40],List_VertmitCodons[41]],"K":[List_VertmitCodons[42],List_VertmitCodons[43]],"V":[List_VertmitCodons[48],List_VertmitCodons[49],List_VertmitCodons[50],List_VertmitCodons[51]],"A":[List_VertmitCodons[52],List_VertmitCodons[53],List_VertmitCodons[54],List_VertmitCodons[55]],"D":[List_VertmitCodons[56],List_VertmitCodons[57]],"E":[List_VertmitCodons[58],List_VertmitCodons[59]],"G":[List_VertmitCodons[60],List_VertmitCodons[61],List_VertmitCodons[62],List_VertmitCodons[63]]}

>>> AAindex=definitions

>>> AAindex
Out[65]: 
{'*': ['taa', 'tag', 'aga', 'agg'],
 'A': ['gct', 'gcc', 'gca', 'gcg'],
 'C': ['tgt', 'tgc'],
 'D': ['gat', 'gac'],
 'E': ['gaa', 'gag'],
 'F': ['ttt', 'ttc'],
 'G': ['ggt', 'ggc', 'gga', 'ggg'],
 'H': ['cat', 'cac'],
 'I': ['att', 'atc'],
 'K': ['aaa', 'aag'],
 'L': ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'],
 'M': ['ata', 'atg'],
 'N': ['aat', 'aac'],
 'P': ['cct', 'ccc', 'cca', 'ccg'],
 'Q': ['caa', 'cag'],
 'R': ['cgt', 'cgc', 'cga', 'cgg'],
 'S': ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'],
 'T': ['act', 'acc', 'aca', 'acg'],
 'V': ['gtt', 'gtc', 'gta', 'gtg'],
 'W': ['tga', 'tgg'],
 'Y': ['tat', 'tac']}
 
 #At this point I couldn't figure out how to apply the dictionary that I made to the list I made of the codons from the original sequence, nor did I actually know if that was possible to do. I found code on http://www.petercollingridge.co.uk/book/export/html/474 and utilized it for assistance. 
 
>>> bases = ['t', 'c', 'a', 'g'] #Creates a list of bases, each base as an individual variable

>>> codons = [a+b+c for a in bases for b in bases for c in bases] #Puts together codons (sets of 3)

>>> amino_acids='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG' #Vertebrate mitochondrial sequence

>>> codon_table=dict(zip(codons,amino_acids)) #creates a codon table, which is dictionary equating the codons to the amino acids.
 
>>> def translateAA(seq):
    peptide = '' 
    end = len(seq) - (len(seq)%3)-1 #From earlier code, defining the end of the sequence if it is not divisible by 3
    for i in range(0, end, 3):     #Indicating the length of a codon (beginning at i ending at 3 characters)
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*') #Calling the codon_table dictionary
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break 
    	#If else statement here indicates that if the amino acid does not equal (!=) a * (i.e., stop codon) then the peptide is concatenated (maybe? not sure what += is) with the amino acid, or else there should be a break.
    return peptide


>>> translateAA(A1DNA) #Apply translate function
Out[111]: 'KSYRAHTPNMLVKPLPLLINPYAISIIISSLALGTITTLSSYH'