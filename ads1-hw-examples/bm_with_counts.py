def boyer_moore_with_counts(p, p_bm, t):
    num_alignments = num_character_comparison = 0
    i = 0
    occurrences = []
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatch = False
        num_alignments += 1
        for j in range(len(p)-1, -1, -1):
            num_character_comparison += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(skip_bc, skip_gs)
                mismatch = True 
                break
        if not mismatch:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift
    return (occurrences, num_alignments, num_character_comparison)
