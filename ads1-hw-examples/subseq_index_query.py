from naive_2mm import naive_2mm
def query_subseq(p, t, subseq_ind):
    #hits = []
    occurrences = set()
    total_hits = 0
    for i in range(3):
        hits = subseq_ind.query(p[i:])
        total_hits += len(hits)
        for hit in hits:
            if naive_2mm(p, t[hit-i:hit-i+len(p)]):
                occurrences.add(hit-i)
    return list(occurrences), total_hits
