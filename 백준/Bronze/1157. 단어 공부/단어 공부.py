word = input().upper()

letter_counts = {}

for letter in word:
  if letter in letter_counts:
    letter_counts[letter] += 1
  else:
    letter_counts[letter] = 1

max_count = max(letter_counts.values())
most_frequent_letters = [letter 
                         for 
                         letter, count in 
                         letter_counts.items() 
                         if count == max_count]

if len(most_frequent_letters) > 1:
  print('?')
else:
  print(most_frequent_letters[0])

