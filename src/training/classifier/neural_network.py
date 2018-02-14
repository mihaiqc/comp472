from training.classifier.abstract_classifier import AbstractClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from util.file import File
from sklearn.neural_network import MLPClassifier


class NeuralNetwork(AbstractClassifier):
    def __init__(self, dataset):
        AbstractClassifier.__init__(self, dataset)

    def train(self):
        """

        """
        x_total, y_total = self.reshape_dataset()
        x_train, x_test, y_train, y_test = train_test_split(
            x_total, y_total, test_size=0.20, random_state=42)
        print("Sample size: {}".format(len(x_total)))
        print("Train size: {}".format(len(x_train)))
        print("Test size: {}".format(len(x_test)))

        print("Training Classifier using Neural Networks")
        clf = MLPClassifier(max_iter=1000, hidden_layer_sizes=(37,16,10))
        self.model = clf.fit(x_train, y_train)
        self.test(x_test, y_test)

    def test(self, x_test, y_test):
        # Test
        print("Testing Classifier")
        y_predict = self.model.predict(x_test)
        num_correct = np.sum(y_predict == y_test)
        (precision, recall, f1, _) = precision_recall_fscore_support(y_test, y_predict)
        print('Test accuracy: {}%'.format(
            num_correct * 100.0 / len(y_test)))
        print('Precision: {}'.format(precision))
        print('Recall: {}'.format(recall))
        print('F1: {}'.format(f1))

    def evaluate_best_parameters(self):
        """
        Evaluate several different parameter combinations and
        returns the best combination.
        returns: a dict containing the most optimal parameter
                 combination
        """
        x_total, y_total = self.reshape_dataset()
        x_total = x_total[:4000]
        y_total = y_total[:4000]

        parameters = {
            'hidden_layer_sizes': ((37,16), (37,16,10)),
        }

        nn = MLPClassifier(max_iter=1000, hidden_layer_sizes=(37,16,10))
        clf = GridSearchCV(nn, parameters)
        clf.fit(x_total, y_total)
        print(clf.best_params_)


