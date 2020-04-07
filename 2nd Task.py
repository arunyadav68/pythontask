sentance = input("Enter Your Sentance: ")
sentance_split = sentance.split(' ')

word_container = []
for i in sentance_split:
    if i not in word_container:
        word_container.append(i)
    else:
        continue

def sorting_sentance(lst):
   
    if not lst:
        return []
    return (sorting_sentance([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            sorting_sentance([x for x in lst[1:] if x >= lst[0]]))

result = sorting_sentance(word_container)
print((' ').join(result))
