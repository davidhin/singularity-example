from singexample.helpers import ml_utils


def test_encoder_categorical():
    """Test onehot encoder helper for categorical labels."""
    onehot = ml_utils.EncoderHelper()
    y_train = ["apple", "orange"]
    onehot.fit(y_train)
    y_train = onehot.transform(y_train)
    assert (y_train == [[1, 0], [0, 1]]).all(), "One hot encoded form."
    y_train_inversed = onehot.inverse_transform(y_train)
    assert (y_train_inversed == ["apple", "orange"]).all(), "One hot decoded form."


def test_encoder_numerical():
    """Test onehot encoder helper for numerical labels."""
    onehot = ml_utils.EncoderHelper()
    y_train = [1, 5]
    onehot.fit(y_train)
    y_train = onehot.transform(y_train)
    assert (y_train == [[1, 0], [0, 1]]).all(), "One hot encoded form."
    y_train_inversed = onehot.inverse_transform(y_train)
    assert (y_train_inversed == [1, 5]).all(), "One hot decoded form."
