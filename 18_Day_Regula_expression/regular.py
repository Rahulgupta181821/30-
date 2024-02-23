import re
# txt = 'I love to teache python and javascript.'
# match= re.match('I love to teach',txt,re.I)
# print(match)
# span = match.span()
# print(span)
# start, end = span
# substring = txt[start:end]
# print(substring)


# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# match = re.search('first',txt,re.I)
# print(match)
# start,end = match.span()
# print(txt[start:end])

# match= re.findall('language',txt, re.I)
# print(match)


# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# matches = re.sub('%', '', txt)
# print(matches)

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern,txt)
print(matches)
matches =re.findall(regex_pattern,txt,re.I)
print(matches)
regex_pattern= r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)