from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    joblib.dump(model, "model.joblib")

if __name__ == "__main__":
    train_and_save_model()
