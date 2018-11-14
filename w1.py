def line_concat(result_list):
    #convert a list of integers into multiple lines
    for x in range(len(result_list)):
        print (result_list[x])

def dict_concat(result_dict):
    for key, value in result_dict.items():
        if len(value)>0:
            #for x in result_dict):
            str = ""
            for i in value:
                str += ","+i
            str = str[1:]
            print (key, "->", str)


def StringComposition(k,text):
    results = []
    for i in range(len(text)-k+1):
        results.append(text[i:i+k])
    return results


k=100
text = "CACTAAGAGTACGACGGGACATGCATATACCACAACGAACTCATGTGCGCCACCCTCATGCAGGTGTATCACTCCACCTGTCACTGGCGAATCCAGAACGTTGTTAGCCGCTGTGTGAACCATTATTTGGGAAGAGACCGTAGCAAGTGACCAACTCGCACCACGATCCCAAGGTGATAAATGTTCGATGGATTCCTGGAGTGGATAGCGTGGGCTACAGCATGTCTGTTACGGCCAAGACAGGCGTATAACGCCGGGAAATTAGACGACCGGTATCGTTCGAAAGGGGGCGGTCACGGATTAAAGCCTTTGGTGTGGGGCCGATCTTCCACGGTTGGAACCAAATGCAGGTTTCTGGTGTGGTAACTTAAGATAGCCCGCCCCGTAAGTGGCGACGGCGCCCAAATTAGTAGAGTTTACACATTTCCGCTTTGTAACTTGTCAATCTACAACCGCCATGAAGGTCCGAGTCTGGGCGAAATATTTGCACTTCGGGATCATCCTTATTAGCGTGACAACTTCTAAAGCTTCGTCCAGCCACCGGTTACGGCATGCCATAATGCCAGACAATTAGGTTCACCGCTATTCAGGCTGCATGACGCGAGCATCGCTTACCCTCATCTTAGATAATGACGCTACTGAGATGATTCGCCACCGCAAAATTTCGGCGTTGCTCAATAGGGGCCCTTCTGCATGTCCCTCTAAAGCGGGTTCAAAGTAAACAAGTGCACGCCCTATTACCTTCACAACCATATTTATAGTCTAAAAATCGTGTAGAAGCGACATACTTGCTTGCTATCCTCTTGTCGCCCGTTGCGGTTTCCGTGGGGGTCGCACATTTGGTTAGTTAGCGGACGAACCACTGAGCTTATTCCAGAGTGTTATGGGTCTGCTCAGCCTGAGGCCATATTCCGAGGATCACCTCTTCGCAGTTAAAGAAAAATTCCCGGTTTCATAGGAACTGTCCTCGAGACACCACGGGGCGATCCAAGCCTTCCCGGCTGCTGCTTTCTCCTGAAGCCCATCCGCATTGCTAAACGAAGTGATGCGAGCCGAGGGTGGAACTCTGTGGCCTTGAGGCGCCGAATGGGTAAATGGGAGACAGAGTCATTCGTAAACTGGGTTTTCCGGTCCTCCCAGCGCCGCACTCTCCGCCACGTAGCGCACTTATGTCAGGACGCACGCTAGCTACAGCTATTGTTGCCCCACAACTCGTGCCCAGCCATAGTCCCCAAGCACGATTCCAAATTAGCGGACTCCGTTCTCGCTACGCTTAGCCCTCGATGTGCACAGAAAACCACGTAACGGCCCACTCTTAAGCCGGTAAAATAATGCAGCCTCCAACGTCGAAAAAGGTATAGCTGCTACAAGTTGTAGTAATATACCGCTGTGAGTGGATGTTCATATATCCGCTTAGAATTACACGTAGGGTTTTCAATAGGCTCATAGTTACCTCCAGAGACAGCAATGGCGATCTGACCCAACATAACAGTGCAAGCTGCCCCCAGTTTAGGTGCAAAGGTACGTCGAGTCCCACCGCAGCGTCCCCCACATTTCCGCTTGACGAATGAGAGTGAATTAGTGATCAGAGACGCACTGGCGCTTAATACACATCACTCGAACTGTCTCAACCTGCTGGGGGGCCTCCTGAAGTAAGACTGATTTTATTCTAGTAAACCATAGCGTGTGCCAAGCTCGGTCCTCGAAGCCTTTACTCGCCGCTCATCGTGACCGACTGGCGAGTGCCCGTCGTACTAATGACACCTCATTCGCACTTTAGGTCATTGGACGCTAAAATAGCAGACGGACTGGTGAGGTCTCGTCCCCACACGATCCGCATAGCCTTTCGGGGTGGTAATAATCTGTAAGCCACCGTCAGTGCCGTCAGTTACTCCGGATGAGGCGATGCATTCAACGTATGACTAGCATTTAGGCACTGCGGCGCACATAACGTGACCTAAGTCAATTACGGAGACCCAGAGCAATATGTTCACGGGGCGTTATCAGAAGGAATCGGCGTCGGATTTGACAGCGAAACTGAACGCACTGTTGCAGTGGAGTAAGCACATCTACAGCCGCATACCACAGCACTAGACCGTGTTCAATGTGATTTTCGCCATCCAATGGTCTCCGGAGCCTTGAAAAACACCTTCTCCGTGTCATGTCCTCATTAGAGAACGCTGAGGGACGATCGTGTATCCCCCTGCTACACGACGACCTCGCATCGTCGAGGCCAGGGGAGCGATGCGAGGACTCTGGGCAGTCGTACGGCATCAGTCAGTAGACGGCACATCCCACAAACGGAGAAGTTTCCACACAAGATAGAAAAGTCCAGTCAACGGCCGCACACGTGTGTGAGCATATTCCAACTGCGACGGACAATAATTTGCAATGCGATGTTTCTGGGATAAGGGCAGGCTAGCTTGTCAACAGATTACAAGCAATGCTGGAATATGATGTCCGCTAGGTGGGCGACTGAACTGGACTTGTGTAACCGCGAGGGATTTGCGGGTCTGCAACACCAATGGAGGATAATAGGTACCCACGCTCAAGCGCAGCACGATCTAGAGGTAGACAAACATTGATAGTGGAGATTTAACGCCGTACCAGCGGGGGGGCTCAAGTGACTACAAGTCTTATAGTGCGGCGGACTTATTCTACTGGTAATAACTCGATAGGCTAACTCTATACTCAGGTGAGCTAGGTCAAGCCTGACTTTGCGTGGTTGATGTAAGACGGCTGTAACGTAAAAGAAAGGAAGTTTGCGGTGTACTAGGTCGAAGAGTTCAACTATACTGGAGAAAAGAATGCCCGTTGAAGGTATGGGTTCGCGCCGGGGTGTGGCTTTTGTCTAGGCTTTAGTGTGTGGGGAAGTAGGCGACGGTTGCAAGGCGCGTCGGCCTAGTACTGTAAGGCTCCTCCGCGCCCCGTGTTTGCGCGAGTGTTTCTGACAGAATAGGATCCAGACAGACTGTGCAGGCATACGGACAGGCTGATGATCGGGATCCCACGAGGGGGTTCGCGTATCGGAACTCAAGCTGCGTGCGTATTACAGCAAGTCCTAAGATGTCCCGAAACCTTTTCCGGCCGGAAATTAAGCTAAGACCATGTTGTTACCAATTAAAGTAACGCAGTTCATCAGCAGGCCACGGTATGCAGCAAACAGTAATCGGTCAATTCTCGTCTGTACAGCCCGAAATGGCTTAAATCCATGCCGAAAGAGGAATAGCTACCGGACATTCGTTACAAATGCGGCTGATATATCACGTAGTAATACGAGCCGGCGAAATGTGGATTGATTCCAACCGTGGCCGGCCACTTTTCTAGCGGCGACTTACGTTAGCGGAGTTGGAGGTTTCGCTCCGCCTTGGAATCGGAGCCTAGTTCCACTCCAGGCAGGTCTTTTTAAAACAAGGACTAGCAAGCACGAAGGGTAACCGCCTCCTGGGATCTTGTGGTTCCTACCTGGGGTTCCTGTTCAAGCAACGCTCCCAGTGGCGGGGGTTCTACAAGTGTCGCCACCTTCTCACCTAAACGCTTCTGTATCTAGCTGAATCTAGACCAAAGATAAATGTTTCGACCGCTCACACAGGATAGACCGGTGGTACCATCAGCAGCTACTGGATATACATATGTACGGACTTTGCCAACTGGAGGAATATTCGTCGACCCTAGTAGGTGGGTCTTTCCCTCCCGGTCTCAGAGCCTAGGGTCAACGAGGTGCTCGACTGGTGGCTCAACTAATCCATTGTCTTAATCCCGGCGCATCCCTGAGCTTTAGTACTTGATCACCCATACTCATCCCCCGACATTGCCCCGGCATAAGAACACTTCCCTAGAAGCTACATTTCTAGGACGGTGGGACCTCGCCGATAACACGCTAAGTCGTAACCTGTAAATCAGTCCTTTCATTTCCAACCCGTATTTCCGTGATTAATCATGTCATCAATTCCCATTGTATAGATATATACACCATATCGGCGGTCTAACCCTTGCAGGAACTTTGTTCGCGGGTGTGTTCGGCTTTACGTCTACAAATCCAACTAAGGTGTGCCCTTGGAGTTTACGTTCGTTCAGACGGACCAACAGGCATACTAATAAAAAACCCATGACACCCCTCTGCGCCGATGCTGGCAACAATCGGACTTCCGTAGAACCTATCCGACTGAGACGTTGGCGTCCCGCATATTTATAACAATGGGCAGGTTGTGAAAGCGAGAGTCATAGTTGCCTAAGTTAATTTTTTCATTATATCAAACGTCATTATCAGCATATCACCGCACTTTGCGGTATTGGCAATTTTCATTTCTATCTCAGTCGCGGCACAGTCGGGCGCTCGTAGGCCTACCGGATGGACAATGTGCGGGGCTGCTTAAGGAGGATCGCACACGCGAAGTACCACTACTGGTAAACGTGCACGTTGCAACCGGCTCGTCTATCTGCCTAACAACTGCTGAGTAATTAATCGCAAGCCCTGTTAAGAGGCAGCCACCGGAGGTGGCAGAGTATATATCCTGTCCCTATACACCAGGTGGCTAGCGCGATTGCGTGAAGCCAGAATGTACAATGTCACAAGGAAAAACTAGTCGGCTTATCCGTCCTCTTGTAACAATCGTCACTGCTAGTCAATAGAACTCGTCGTTTCTCGCGGCGGATGCGAGACGGGAAAGTAGAAGACACTGTCGTATGTTCTCAGCTAGGCAGGAAGCTTAGAGCTTAGGAGCCGATCGCCCCTGCTCCCATATGGATACGAATGGCACGAGTGCGGAGGAACGCGATCCTACGTGATGATCGACAGCTGCAAATGGACACCGGTGGTAAGAACACGAATCCTAGAAAATTGTTTACGTGTGGTTTATTCTCTAGAAATTTACTTACGTACATGTGGCTTGGGTTAAGCTTATCCGCCTGGCAATACGAACTAAAGGATGCTTAACACGTAAAATCCCGGGGAGTGGCGTGTATGCCACTCAGAGGTGTACCCAGTCTCTGATCAACGT"
#line_concat(StringComposition(k,text))

def StringSpelledbyGenomePathProblem(kmers):
    k = len(kmers[0])
    result = kmers[0]
    for i in range(1,len(kmers)):
        if kmers[i][:-1] == kmers[i-1][1:]:
            result += (kmers[i][-1])
    return result

'''
line_num = 0
lines_to_skip = 0
DNA = []
with open('dataset_198_3.txt','r') as f: #dataset_161_5 #randomized_motif_search
    for line in f:
        line_num += 1
        read_line = line.rstrip('\n')
        if line_num <= lines_to_skip:
            continue
        elif read_line=='Output:':
            break
        elif line_num >= lines_to_skip+1:
            DNA.append(read_line)
        else:
            break
    f.close()
print (StringSpelledbyGenomePathProblem(DNA))
'''

def OverlapGraphProblem(kmerList):
    '''Construct the overlap graph of a collection of k-mers.
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns).
     '''
    results = {}
    for kmer in kmerList:
        suffix = kmer[1:]
        matches = []
        for i in kmerList:
            if i == kmer:
                continue #dont need to compare the kmer to itself
            if suffix == i[:-1]: #if suffix of the kmer matches the prefix of this i, add i to the dict
                matches.append(i)
        if len(matches)>0:
            results[kmer] = matches
    return results

#dna = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT','GGCAC']
#dict_concat(OverlapGraphProblem(dna))
'''line_num = 0
lines_to_skip = 0
DNA = []
with open('dataset_198_10.txt','r') as f: #dataset_161_5 #randomized_motif_search
    for line in f:
        line_num += 1
        read_line = line.rstrip('\n')
        if line_num <= lines_to_skip:
            continue
        elif read_line=='Output:':
            break
        elif line_num >= lines_to_skip+1:
            DNA.append(read_line)
        else:
            break
    f.close()
dict_concat(OverlapGraphProblem(DNA))'''


def DeBruijnGraphfromString(k,text):
    results = {}
    for i in range(len(text)-k+1):
        node = text[i:i+k-1]
        if node in results:
            results[node].append(text[i+1:i+k])
        else:
            results[node]=[text[i+1:i+k]]
    return results

#dict_concat(DeBruijnGraphfromString(4,'AAGATTCTCTAAGA'))
'''line_num = 0
with open('dataset_199_6.txt','r') as f: #dataset_161_5 #randomized_motif_search
    for line in f:
        line_num += 1
        read_line = line.rstrip('\n')
        if line_num == 1:
            k = int(read_line)
        else:
            DNA = read_line
    f.close()
dict_concat(DeBruijnGraphfromString(k, DNA))'''

'''k = 2
print (k)
dict_concat(DeBruijnGraphfromString(k,'TAATGCCATGGGATGTT'))

k = 3
print (k)
dict_concat(DeBruijnGraphfromString(k,'TAATGCCATGGGATGTT'))

k = 4
print (k)
dict_concat(DeBruijnGraphfromString(k,'TAATGCCATGGGATGTT'))

print ('TAATGCCATGGGATGTT')
dict_concat(DeBruijnGraphfromString(3,'TAATGCCATGGGATGTT'))
print ('TAATGGGATGCCATGTT')
dict_concat(DeBruijnGraphfromString(3,'TAATGGGATGCCATGTT'))'''


def DeBruijnGraphfromKmers(patterns):
    results = {}
    for kmer in patterns:
        prefix = kmer[:-1]
        if prefix in results:
            results[prefix].append(kmer[1:])
        else:
            results[prefix] = [kmer[1:]]
    return results

patterns = ['GAGG',
'CAGG',
'GGGG',
'GGGA',
'CAGG',
'AGGG',
'GGAG']
#dict_concat(DeBruijnGraphfromKmers(patterns))
DNA = []
with open('dataset_200_8.txt','r') as f: #dataset_161_5 #randomized_motif_search
    for line in f:
        read_line = line.rstrip('\n')
        DNA.append(read_line)
    f.close()
dict_concat(DeBruijnGraphfromKmers(DNA))