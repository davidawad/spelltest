# spelltest
A simple script that checks for any misspelled words in HTML content. It uses the power of the PyEnchant spellchecking library to determine any mispelled words you might be missing in a given directory.

It doesn't assume that misspelled words are errors, but it's worth taking a quick look at if you're worried about missing something! 


### Usage

You can use relative paths too and travis-ci as well! 
```shell
$ python spelltest.py -t ../../Web/arm-open.github.io
Looking for spelling errors in ../../Web/arm-open.github.io/templates/index.html
Looking for spelling errors in ../../Web/arm-open.github.io/templates/item-1.html
Looking for spelling errors in ../../Web/arm-open.github.io/templates/item-2.html
Looking for spelling errors in ../../Web/arm-open.github.io/templates/item-3.html
Looking for spelling errors in ../../Web/arm-open.github.io/templates/item-4.html
Mispelled Words: 50, Total Words: 716, Percentage Incorrect: 0.07%
____________________
['let’s', 'ARM’s', 'poor/working', 'millennials', 'boomers', 'Service:', 'support!', 'Bi-annual', 'Dinners:', '-3', '(Coats', 'etc)', 'Pay-it-Forward', 'wall:', '4c', 'Easton', 'out!', 'need!', 'Volunteer:', 'underserved', 'resource;', 'you!', '(Approx', '(1-2', 'week)', 'Volunteer:', '(law', 'etc)', 'don’t', 'work!', '(Approximate', '<', 'week)', 'Ambassador:', 'don’t', 'ARM’s', 'first!', '(Approximate', 'month)', 'Donor:', 'donation!', 'let’s', 'community!', 'Grounds:', 'brew!', '(http://thehiddengroundscom/)', 'Dogs:', 'all-star', 'DDogs', 'Balboa!']

```
