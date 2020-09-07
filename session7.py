import random
import math
import operator
import string
from functools import partial, reduce

a = [ 2 , 3 ,4]
b = [1,2,3]

lambda_is_fibonacci = lambda x: lambda_is_prefect_square(5*x*x + 4) or lambda_is_prefect_square(5*x*x - 4)
lambda_is_prefect_square = lambda x: x == int(math.sqrt(x))**2

q1 = list(filter(lambda_is_fibonacci, range(10)))

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

with open('swear_words.txt','r') as f:
    swear_words = set(f.read().splitlines())

with open('paragraph_catcher_in_the_rye.txt', 'r', encoding='utf8') as f:
    paragraph = f.read()

paragraph = paragraph.split()

q3 = [word for word in paragraph if word in swear_words]


#reduce
q4_1 = reduce(lambda x,y:x+y if y%2==0 else x, range(10)) 
text = 'tsai'
q4_2 = reduce(lambda x,y: x if ord(x)>ord(y) else y, text)

a= range(10)
q4_3 = reduce(lambda x,y: x+y,  a[::3])

#KADDAADDDD
#10<<DD<<99 & 1000<<DDDD<<9999
q5 = [f'KA{dd}{aa}{dddd}' for dd,aa,dddd in 
zip(
    [random.randint(10,99) for _ in range(15)], 
    [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(15)], 
    [random.randint(1000, 9999) for _ in range(15)]
    )]

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
