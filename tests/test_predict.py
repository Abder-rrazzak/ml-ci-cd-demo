from app.predict import predict

def test_prediction_output():
    sample = [5.1, 3.5, 1.4, 0.2]
    result = predict(sample)
    assert isinstance(result, list)
    assert len(result) == 1
