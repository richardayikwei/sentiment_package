from motoevsentiment.wsentiment import wdataframe
import pandas as pd

def test_wdataframe(tmp_path):

    # Create a temporary text file
    test_file = tmp_path / "sample.txt"
    test_file.write_text("29/09/2023, 7:49 am - john doe: ok\n30/09/2023, 8:49 am - john doe: ok2")

    # Call the function
    df = wdataframe(test_file)

    #Assertions
    assert isinstance(df,pd.DataFrame)
    assert list(df.columns == [
        'datetime', 'sender', 'message'
        ])
    assert df.loc[0,'datetime'] == pd.Timestamp('2023-09-29 07:49:00')
    assert df.loc[0,'sender'] == 'john doe'
    assert df.loc[0,'message'] == 'ok'