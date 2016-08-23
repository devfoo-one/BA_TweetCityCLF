from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# http://stackoverflow.com/questions/35876508/evaluate-multiple-scores-on-sklearn-cross-val-score

class PrintingScorer:
    """
    A scorer for scikit-learn cross validation needs to be an instance of a class since scikit is internally pickling stuff.
    This seems to be necessary for threading.
    """

    def __init__(self):
        pass

    def __call__(self, estimator, X, y):
        """
        According to sklearn documentation, this is how an scorer method is build.
        This is necessary because sklearn does not allow calculating more than one score in one run :(
        Printing those scores is a dirty workaround, but it works for now.
        :param estimator: Estimator to test
        :param X: data
        :param y: ground truth
        :return: f1_weighted score, this is necessary for comparison if this scorer is used in a grid search.
        """
        y_predicted = estimator.predict(X)
        precision_micro = precision_score(y, y_predicted, average='micro')
        precision_macro = precision_score(y, y_predicted, average='macro')
        precision_weighted = precision_score(y, y_predicted, average='weighted')
        recall_micro = recall_score(y, y_predicted, average='micro')
        recall_macro = recall_score(y, y_predicted, average='macro')
        recall_weighted = recall_score(y, y_predicted, average='weighted')
        f1_micro = f1_score(y, y_predicted, average='micro')
        f1_macro = f1_score(y, y_predicted, average='macro')
        f1_weighted = f1_score(y, y_predicted, average='weighted')
        print('--- PrintingScorer ---')
        print("Precision:\tmicro={}\tmacro={}\tweighted={}".format(precision_micro, precision_macro, precision_weighted))
        print("Recall:\t\tmicro={}\tmacro={}\tweighted={}".format(recall_micro, recall_macro, recall_weighted))
        print("F-Measure:\tmicro={}\tmacro={}\tweighted={}".format(f1_micro, f1_macro, f1_weighted))
        return f1_weighted
