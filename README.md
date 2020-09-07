# Assignment 7
**1.Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100**
```python
lambda_is_prefect_square = lambda x: x == int(math.sqrt(x))**2
lambda_is_fibonacci = lambda x: lambda_is_prefect_square(5*x*x + 4) or lambda_is_prefect_square(5*x*x - 4)

q1 = list(filter(lambda_is_fibonacci, range(10)))
```
**2.Using list comprehension (and zip/lambda/etc if required) write an expression that: PTS:100**
1. add 2 iterables a and b such that a is even and b is odd
2. strips every vowel from a string provided (tsai>>ts)
3. acts like a ReLU function for a 1D array
4. acts like a sigmoid function for a 1D array
5. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
   
```python 
q2_1 = [x+y for x,y in zip(a,b) if x%2==0 and y%2!=0]

text = 'tsai'
q2_2 = ''.join([x for x in text if x.lower() not in 'aeiou'])

vector = [random.uniform(-5,5) for _ in range(10)]
q2_3 = [x if x >= 0 else 0 for x in vector ]

sigmoid = lambda x:1/(1+math.exp(-x))
q2_4 = [sigmoid(x) for x in vector]

shift_n = 5
text='zb'
q2_5 = ''.join([chr(ord(x)+shift_n) if ord(x) + shift_n <= ord('z') else chr(ord(x)+ shift_n-26) for x in text])
```
**3.A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200**

```python 
with open('swear_words.txt','r') as f:
    swear_words = set(f.read().splitlines())

with open('paragraph_catcher_in_the_rye.txt', 'r', encoding='utf8') as f:
    paragraph = f.read()

paragraph = paragraph.split()

q3 = [word for word in paragraph if word in swear_words]
```
**4.Using reduce function: PTS:100**
 1. add only even numbers in a list
 2. find the biggest character in a string (printable ascii characters)
 3. adds every 3rd number in a list

```python
q4_1 = reduce(lambda x,y:x+y if y%2==0 else x, range(10)) 
text = 'tsai'
q4_2 = reduce(lambda x,y: x if ord(x)>ord(y) else y, text)

a= range(10)
q4_3 = reduce(lambda x,y: x+y,  a[::3])
```
**5.Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100**

```python
q5 = [f'KA{dd}{aa}{dddd}' for dd,aa,dddd in 
zip(
    [random.randint(10,99) for _ in range(15)], 
    [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(15)], 
    [random.randint(1000, 9999) for _ in range(15)]
    )]
```
**6.Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:100**
```python
def get_plates(state:str, start_dddd:int, end_dddd:int, num_plates:int=15) -> 'list of n number plates':
    """Returns n number plates (default 15)

    Args:
        state (str): KA, KL etc..
        start_dddd (int): start of range 4 digit number
        end_dddd (int): end of range 4 digit number
        num_plates (int, optional): number of plates to return. Defaults to 15.

    Returns:
        list of n number plates: default 15 plates
    """
    return [f'{state}{dd}{aa}{dddd}' for dd,aa,dddd in 
zip(
    [random.randint(10,99) for _ in range(num_plates)], 
    [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(num_plates)], 
    [random.randint(start_dddd, end_dddd) for _ in range(num_plates)]
    )]

q6_1 = get_plates('DL', 1000, 9999)
q6_2 = partial(get_plates, start_dddd=1000, end_dddd=9999)
```

## **Test Cases (Pytest)**
>The names of the tests are so that `'test_'` prefix is added to the function it tests, suffied by the what the test does.

### test_readme_exists
   Checks if there is a README.md file in the same folder.

### test_readme_contents
   Checks if the README.md file has alteast 500 words.

### test_readme_proper_description
   Checks if the required functions are present in the README.md file.

### test_readme_file_for_formatting
   Checks if there are adequete headings present in the README.md file.

### test_indentations
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

### test_function_name_had_cap_letter
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.
   
### ***Annotation tests***
tests if any of the functions have annotations:

1. `test_annotations_get_plates`


### ***Doc String tests***
tests if any of these functions have doc strings
1. `test_docstring_get_plates`

### test_lambda_is_fibonacci 
   Checks if the given number is present in the fibonacci series.

### test_lambda_is_prefect_square
   Checks if the given number is a perfect square

### test_q2_1
   Checks if Q2.1 logic is correct, ie add 2 iterables a and b such that a is even and b is odd

### test_q2_2
   Checks if Q2.2 logic is correct, ie strips every vowel from a string provided (tsai>>t s)

### test_q2_3
   Checks if Q2.3 logic is correct, ie acts like a ReLU function for a 1D array

### test_q2_4
   Checks if Q2.4 logic is correct, ie acts like a sigmoid function for a 1D array
   
### test_q2_5
   Checks if Q2.5 logic is correct, ie takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

### test_q3
   Checks if functions function finds any of swear words using the profanity list in the paragraph from catcher in the rye, and returns them if any.

### test_q4_1
Checks if only even numbers in a list are added.

### test_q4_2
Checks if char found is indeed the largest.

### test_q4_3
Checks if only 3rd number in a list are added

### test_q5
Check that the plates have DDDD and dd in the desirednumber range and check if Karnataka Reg.

### test_q6_1
Check that the plates have DDDD and dd in the desirednumber range and check if Delhi Reg.

### test_q6_2_partial_func
Checks if the function is a partial func.

### test_q6_2
Check that the plates have DDDD and dd in the desirednumber range and the partial function takes one input (here PB) and makes it the state of reg.