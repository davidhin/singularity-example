import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


class EncoderHelper:
    """One hot encode labels."""

    def __init__(self):
        """Initialise label encoder and onehot encoder."""
        self.label_encoder = LabelEncoder()
        self.onehot_encoder = OneHotEncoder(sparse=False, handle_unknown="error")

    def fit(self, y: np.ndarray):
        """Fit label encoder and onehot encoder."""
        self.label_encoder.fit(y)
        integer_encoded = self.label_encoder.transform(y)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        self.onehot_encoder.fit(integer_encoded)

    def transform(self, y: np.ndarray):
        """One hot encode labels."""
        return self.onehot_encoder.transform(
            self.label_encoder.transform(y).reshape(len(y), 1)
        )

    def inverse_transform(self, y: np.ndarray):
        """Inverse labels."""
        return self.label_encoder.inverse_transform([np.argmax(i) for i in y])
