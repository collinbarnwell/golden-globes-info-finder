sim_lists = [
    ['film', 'motion picture', 'movie', 'picture'],
    ['tv-series', 'tv series', 'miniseries', 'mini-series', 'tv', 'series'],
    ['musical or comedy', 'musical', 'comedy']
]

def award_name_gen(name):
    names_genned = []
    name = name.lower()
    for sims in sim_lists:
        for word in sims:
            if word in name:
                for sub in sims:
                    if sub == word:
                        continue
                    names_genned.append(name.replace(word, sub))
                break

    return names_genned



# if len([x for x in award_name_gen(name) if x in tweet]) > 0: # then it is contained in tweet
