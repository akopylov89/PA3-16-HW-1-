L = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
my_email = 'cilicium_2@mail.ru'

L = L + my_email
print('Length of L is {}'.format(len(L)))
vowels = ['a','e','y','u','i','o',]
count_of_vowels = 0
for i in L:
    if i.lower() in vowels:
        count_of_vowels +=1
    else:
        continue
print('Count of vowels in L is {}'.format(count_of_vowels))
count = 0
for i in L:
    count +=1
    if count%18 == 0:
        print('%d%s' % (count, i))


