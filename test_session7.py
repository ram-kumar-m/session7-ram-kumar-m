import session7 as main
import pytest
import random
import os
import inspect
import re
import math
import functools
random_list = random.choices(range(1000), k=5)

def test_lambda_is_fibonacci():
    assert main.q1 == [0, 1, 2, 3, 5, 8], \
        'Lambda fibonacci function not working'

def test_lambda_is_prefect_square():
    assert main.lambda_is_prefect_square(25) == True, "Check prefect square function"

def test_q2_1():
    assert main.q2_1 == [3, 7], 'Check if Q2.1 logic is correct!'

def test_q2_2():
    assert main.q2_2 == 'ts', 'Check if Q2.2 logic is correct!'

def test_q2_3():
    assert main.q2_3 == [x if x >= 0 else 0 for x in main.vector ], 'Q2.3 Relu fuction not working'

def test_q2_4():
    sigmoid = lambda x:1/(1+math.exp(-x))
    assert main.q2_4 == [sigmoid(x) for x in main.vector],'Q2.4 Check sigmoid function'

def test_q2_5():
   text = 'eg'
   assert main.q2_5 == text, 'Q2.5 Check boundary condition'

def test_q3():
    assert main.q3 == [word for word in main.paragraph if word in main.swear_words], 'Q3 Cant find swear words.'

def test_q4_1():
    even_nos = [x for x in range(10) if x%2==0]
    assert main.q4_1 == sum(even_nos), 'Q4.1 Even numbers not getting added'

def test_q4_2():
    text = 'tsai'
    assert main.q4_2 == sorted(text)[-1],'Q4.2 Cant find larget char?'

def test_q4_3():
    assert main.q4_3 == sum(range(0,10,3)), 'Q4.3 Adding every third number?'

def test_q5():
    for plate in main.q5:
        dddd = int(plate[-4:])
        dd = int(plate[2:4])
        ka = plate[:2]
        assert dddd<=9999 and dddd>=1000 and dd>=10 and dd<=99 and ka =='KA',\
    'Check the DDDD and dd number range and check if Karnataka Reg.'
    
def test_q6_1():
    for plate in main.q6_1:
        dddd = int(plate[-4:])
        dd = int(plate[2:4])
        ka = plate[:2]
        assert dddd<=9999 and dddd>=1000 and dd>=10 and dd<=99 and ka =='DL',\
    'Check the DDDD and dd number range and check if Delhi Reg.'

def test_q6_2_partial_func():
    assert type(main.q6_2) == functools.partial ,'Is it not a partial func.'

def test_q6_2():
    for plate in main.q6_2('PB'):
        dddd = int(plate[-4:])
        dd = int(plate[2:4])
        ka = plate[:2]
        assert dddd<=9999 and dddd>=1000 and dd>=10 and dd<=99 and ka =='PB',\
    'Check the DDDD and dd number range and check if Punjab Reg.'   

def test_annotations_get_plates():
    assert main.get_plates.__annotations__ ,'Does your functions have annotations'

def test_docstring_get_plates():
    assert main.get_plates.__annotations__ ,'Does your functions have docstrings'


README_CONTENT_CHECK_FOR = [
    'KADDAADDDD',
    'fibonacci',
    'sigmoid'
    ]

CHECK_FOR_THINGS_NOT_ALLOWED = []



def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for count, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations at \
n'th postion {count+1} starting \n with {space}"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
