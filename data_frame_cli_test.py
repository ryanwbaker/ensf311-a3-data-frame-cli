import data_frame_cli as cli
import pandas as pd
import numpy as np

def test_print_shape(capsys):

    expected_out = ['df.shape', 'test.csv', '(5, 2)']

    cli.print_shape('test.csv', pd.DataFrame(np.random.randn(5, 2)))
    captured = capsys.readouterr()
    result = captured.out

    for element in expected_out:
        assert element in result

def test_print_info(capsys):

    expected_out = ['df.info', '5 non-null', 'int']

    cli.print_info(True, pd.DataFrame(np.random.randint(0, 10, size=(5, 2)),
                                      columns=['col_a', 'col_b']))
    captured = capsys.readouterr()
    result = captured.out

    for element in expected_out:
        assert element in result

def test_print_head(capsys):

    expected_out = ['df.head', '10', '40']

    cli.print_head(True, pd.DataFrame(data=[[10, 20], [30, 40]], 
                                      columns=['col_a', 'col_b']))
    captured = capsys.readouterr()
    result = captured.out

    for element in expected_out:
        assert element in result

def test_print_describe_none_column(capsys):

    expected_out = ['describe', 'bla not found']

    cli.print_describe('bla', pd.DataFrame(data=[[10, 20], [30, 40]], 
                                      columns=['col_a', 'col_b']))
    captured = capsys.readouterr()
    result = captured.out

    for element in expected_out:
        assert element in result