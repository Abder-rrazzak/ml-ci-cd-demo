import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.predict import predict

def test_prediction_shape():
    sample = [5.1, 3.5, 1.4, 0.2]
    output = predict(sample)
    assert isinstance(output, list)
    assert len(output) == 1
