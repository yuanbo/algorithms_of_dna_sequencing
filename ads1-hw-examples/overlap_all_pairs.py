from overlap import overlap
def overlap_all_pairs(reads, k):
    k_mer_dic = {}
    for read in reads:
        i = 0
        while i+k < len(read):
            key = str(read[i:i+k])
            if key not in k_mer_dic:
                k_mer_dic[key] = set([read])
            else:
                #print(key, k_mer_dic[key])
                k_mer_dic[key].add(read)
            i += 1
            
    #print(k_mer_dic)
    all_pairs = set()
    for read in reads:
        key = str(read[-k:])
        if key not in k_mer_dic:
            continue
        for i in k_mer_dic[key]:
            if i == read or i.find(key) == -1 or overlap(read, i, k) < k:
                continue
            all_pairs.add((read, i))
    return list(all_pairs)