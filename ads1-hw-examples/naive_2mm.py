def naive(p, t, mm):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = mm 
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match -= 1
        if match >= 0:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def naive_2mm(p, t):
    occurrences = naive(p, t, 2)
    return occurrences

