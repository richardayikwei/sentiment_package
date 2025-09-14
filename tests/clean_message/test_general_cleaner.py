from evmotosentiment.clean_message import preprocess_text

def test_preprocess_text():
    assert preprocess_text('Turning swap station off at Haatso') == 'turning swap station off haatso'