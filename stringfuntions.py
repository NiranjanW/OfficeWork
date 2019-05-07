
import pytest
import unittest
class TestString(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse(word) ,'nayan' ,'Should be nayan')
        self.assertEqual(reverseString(word),'nayan')

def reverse(str):

    return str[::-1]

def reverseString (str):
    strNew= ''
    for chr in str:
        strNew = chr + strNew

    return strNew

def anagram ( s1, s2) :
    if sorted(s1) == sorted(s2):
        return True

    return False

@pytest.fixture(params = ['nodict' , 'dict'])

def generate_initial_transform(request):

    test_input = {'w1':'nayan' ,
                   'w2':'baba'}

    expected_output = {
        'w1' :'nayan',
         'w2':'baba'
    }
    if request.param == 'dict':
        test_input['original'] = {
            'words' : ['nayan' ,'baba']
        }
        test_input['reversed'] = {
            'words': ['nayan', 'baba']
        }
    return test_input , expected_output


def setWord(word):

    return  word

def test_reverse(generate_initial_transform):
    test_input = generate_initial_transform[0]
    expected_output = generate_initial_transform[1]
    assert reverse(test_input) == expected_output
#
# @pytest.fixture
# def func(request):
#
#     return request.param


#
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
if __name__ == '__main__':
    word = 'nayan'
    unittest.main()
    test_reverse(word)

# assert word == reverse(word), "test passed"