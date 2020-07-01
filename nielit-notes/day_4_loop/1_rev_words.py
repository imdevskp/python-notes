sent = raw_input('Enter the sentence :')

split_sent = sent.split()

rev_list = split_sent[::-1]

print(' '.join(rev_list))
