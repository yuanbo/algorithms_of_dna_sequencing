#/Users/yuanbofan/anaconda3/bin/python

def naive_with_counts(p, t):
    num_alignments = num_character_comparison = 0
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        num_alignments += 1
        for j in range(len(p)):
            num_character_comparison += 1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return (occurrences, num_alignments, num_character_comparison)
