import re

text = """
The fast orange cat leaps over the sleepy dog.
Email: test.user456@mail.net, contact.me@webservice.com
Phone: +44-700-333-5678, (987) 654-3210
Address: 5678 Oak Avenue, Apt 890, Metropolis, NY 10001

Date: 06/15/2025, 2025-06-15, 15-06-2025
Time: 08:45, 06:15 PM, 00:00

Usernames:
- user_987
- SuperAdmin_77
- regexPro_456

Sentences with numbers:
- There are 87 oranges in the crate.
- The price of the phone is $799.50.
- My ID is B7654321.

Special characters: !@#$%^&*()_+={}[]|;:'\",.<>?/~`

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Suspendisse potenti. Sed euismod, nisi ac venenatis luctus, velit felis posuere lacus, at venenatis justo neque sed lorem.

Emily's email is emily.smith@test.com, and her backup is esmith.dev@workplace.io.
Call her at +44-600-987-1234 or her office line (600) 432-8765.
Her website is https://www.emilysmith.io, and her IP address is 10.0.0.1.
The price of the product is $24.99, but with a discount, it’s now $19.49.
Today's date is 25/08/2025, and another format is 2025-08-25.
Here’s some HTML: <span class=\"highlight\">Welcome, User!</span>
Watch out for special characters like !@#$%^&*()_+={}[]|:;\"'<>,.?/

A regular expression (or RE) specifies a set of strings that matches it;
the functions in this module let you check if a particular string matches a given regular expression
(or if a given regular expression matches a particular string, which comes down to the same thing).
Regular expressions can be concatenated to form new regular expressions;
if X and Y are both regular expressions, then XY is also a regular expression.
In general, if a string r matches X and another string s matches Y, the string rs will match XY.
This holds unless X or Y contain low precedence operations; boundary conditions between X and Y;
or have numbered group references.
Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here.
For details of the theory and implementation of regular expressions, consult the Cook book [Cook12],
or almost any textbook about compiler construction.
A brief explanation of the format of regular expressions follows.
For further information and a gentler presentation, consult the Regular Expression HOWTO.
Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like 'X', 'x', or '9', are the simplest regular expressions;
they simply match themselves. You can concatenate ordinary characters, so last matches the string 'last'.
(In the rest of this section, we’ll write RE’s in this special style, usually without quotes, and strings to be matched 'in single quotes'.)
"""

x = re.split(r"(?=[A-Z])", text)
print(x)