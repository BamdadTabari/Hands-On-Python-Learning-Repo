import unicodedata

#  • lookup()—Takes a case-insensitive name and returns a Unicode character
#  • name()—Takes a Unicode character and returns an uppercase name

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}", name="{name}", value2="{value2}"')


unicode_test('@')