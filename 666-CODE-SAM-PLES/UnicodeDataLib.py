import unicodedata

#  • lookup()—Takes a case-insensitive name and returns a Unicode character
#  • name()—Takes a Unicode character and returns an uppercase name

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}", name="{name}", value2="{value2}"')


unicode_test('@') # => value="@", name="COMMERCIAL AT", value2="@"
unicode_test('\u2603') #=> value="☃", name="SNOWMAN", value2="☃"
#unicode_test('A') #=> value="A", name="LATIN CAPITAL LETTER A", value2="A
#unicode_test('$') #=> value="$", name="DOLLAR SIGN", value2="$"




                # fun shit #
#  Encoding name         Description
#  'ascii'              Good old seven-bit ASCII
#  'utf-8'              Eight-bit variable-length encoding, and what you almost always want to use
#  'latin-1'            Also known as ISO 8859-1
#  'cp-1252'            A common Windows encoding
#  'unicode-escape'     Python Unicode literal format, `\u`xxxx or `\U`xxxxxxxx
                # fun shit #