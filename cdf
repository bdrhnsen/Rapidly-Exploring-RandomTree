from functools import partial
dups_in_source = partial(list_duplicates_of, source)

for c in "ABDEFS":
    print(c, dups_in_source(c))