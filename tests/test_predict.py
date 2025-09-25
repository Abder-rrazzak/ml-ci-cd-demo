from app.predict import predict

def test_prediction_shape():
    sample = [5.1, 3.5, 1.4, 0.2]
    output = predict(sample)
    assert isinstance(output, list)
    assert len(output) == 1
