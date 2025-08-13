from evmotosentiment.wsentiment import wsentiment_score

def test_wsentiment_score():
    assert wsentiment_score('lights out at haasto') == -2