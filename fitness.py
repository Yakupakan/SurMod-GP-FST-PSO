import gplearn
import fstpso


def _fstpso_loss(y, y_pred, w):
    diffs = np.abs(np.divide((np.maximum(0.001, y) - np.maximum(0.001, y_pred)),
                             np.maximum(0.001, y)))
    return 100. * np.average(diffs, weights=w)


fstpso_loss = make_fitness(_fstpso_loss, greater_is_better=False)
