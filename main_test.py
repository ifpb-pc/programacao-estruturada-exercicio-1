import mock
import builtins
import main


def test_q1(capfd):
    input_output = {
        '2':'Par\n',
        '3': 'Impar\n',
        '20':'Par\n',
        '33':'Impar\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q1()
            out, err = capfd.readouterr()
            assert out == v

def test_q2(capfd):
    input_output = {
        'abcdef':'def\n',
        'texto': 'to\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q2()
            out, err = capfd.readouterr()
            assert out == v

def test_q3(capfd):
    input_output = {
        '5':'5 10 15 20 25 30 35 40 45 50 ', 
        '7': '7 14 21 28 35 42 49 56 63 70 '
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q3()
            out, err = capfd.readouterr()
            assert out == v

def test_q4(capfd):
    input_output = {
        'romulo junior':'Romulo Junior\n', 
        'zé da manga': 'Zé da Manga\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q4()
            out, err = capfd.readouterr()
            assert out == v

def test_q5(capfd):
    input_output = {
        '222':'equilátero\n',
        '322': 'isósceles\n',
        '345': 'escaleno\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q5()
            out, err = capfd.readouterr()
            assert out == v
