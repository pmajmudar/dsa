s = 'leebobleefredalicebobbobleeboblee'

k = 3
# Find all k-length substrings
# could be a generator to reduce space complexity
# Time complexity is O(K*N)
# Note: Slice operation is O(K) and we are doing that N times
substrs = [s[i:i+k] for i in range(len(s) - k + 1)]

# options are Counter, Ordereddict etc.

from collections import Counter
c = Counter(substrs).most_common(1)
print(c)

# If I need to preserve order - I could maintain a queue / list of keys
keys = []
counts = {}
for s in substrs:
    if s not in counts:
        keys.append(s)
        counts[s] = 1
    else:
        counts[s] += 1

# Sorting will be NlogN - so not ideal
sorted(keys, key=lambda x: counts[x], reverse=True)

# I can also alternatively store a tie break in dict?

counts_tie = {}
order = 0
for s in substrs:
    if s not in counts_tie:
        counts_tie[s] = (1, -order)
        order += 1
    else:
        counts_tie[s] = (counts_tie[s][0] + 1, counts_tie[s][1])

print(counts_tie)
max_item = ((0,0), '')
for k,v in counts_tie.items():
    max_item = max(max_item, (v, k))
print("This tie-breaker max: ", max_item)

# Do I need a min or max HEAP?

# Can I reduce from O(K*N) to O(N) ? sliding window with a deque?
window = list(s[:k])
substrs = [''.join(window)]
for i in range(k, len(s)):

# Could do Robin-Karp hashing - sliding window algo?




