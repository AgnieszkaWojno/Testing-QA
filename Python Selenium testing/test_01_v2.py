#1. pip install pytest
#2. Settings->Tools->Python Integrated Tools      Testing->Default: pytest


#dla testów automatycznych:
#3. pip install selenium

def vowel_count(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for ch in string:
        ch = ch.lower()
        if ch in vowels:
            count += 1
    return count

def test_with_my_first_name():
    assert vowel_count('Agnieszka') == 4

def test_with_my_sur_name():
    assert vowel_count('WOJNO') == 2