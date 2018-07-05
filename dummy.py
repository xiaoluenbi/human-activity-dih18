from sklearn.dummy import DummyClassifier


class DummyClassifierAdaptor:

    def __init__(self, *_):
        self.classifier = DummyClassifier(strategy='most_frequent')

    def fit(self, X, y, *_):
        self.classifier.fit(X, y)

        class History:
            history = {}

        return History()

    def __getattr__(self, item):
        return getattr(self.classifier, item)


cnn2d_model = cnn3d_model = DummyClassifierAdaptor