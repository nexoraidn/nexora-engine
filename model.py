import math
import random


class NexoraModel:
    """
    Nexora Engine V1.1

    Neural language model prototype dengan:
    - Token embedding
    - Hidden layer
    - ReLU activation
    - Softmax output
    - Cross-entropy loss
    - Backpropagation
    - Next-token prediction
    """

    def __init__(self, vocab_size, hidden_size=32, seed=42):
        self.vocab_size = vocab_size
        self.hidden_size = hidden_size

        # Reproducible initialization
        random.seed(seed)

        # Token embedding
        self.embedding = [
            [
                random.uniform(-0.1, 0.1)
                for _ in range(hidden_size)
            ]
            for _ in range(vocab_size)
        ]

        # Hidden layer
        self.w1 = [
            [
                random.uniform(-0.1, 0.1)
                for _ in range(hidden_size)
            ]
            for _ in range(hidden_size)
        ]

        self.b1 = [0.0 for _ in range(hidden_size)]

        # Output layer
        self.w2 = [
            [
                random.uniform(-0.1, 0.1)
                for _ in range(hidden_size)
            ]
            for _ in range(vocab_size)
        ]

        self.b2 = [0.0 for _ in range(vocab_size)]

    # --------------------------------------------------
    # ACTIVATION
    # --------------------------------------------------

    def relu(self, x):
        return max(0.0, x)

    # --------------------------------------------------
    # SOFTMAX
    # --------------------------------------------------

    def softmax(self, values):
        maximum = max(values)

        exp_values = [
            math.exp(x - maximum)
            for x in values
        ]

        total = sum(exp_values)

        if total == 0:
            return [
                1.0 / len(values)
                for _ in values
            ]

        return [
            x / total
            for x in exp_values
        ]

    # --------------------------------------------------
    # FORWARD PASS
    # --------------------------------------------------

    def forward(self, token_id):
        if token_id < 0 or token_id >= self.vocab_size:
            token_id = 1

        # Embedding
        x = self.embedding[token_id]

        # Hidden layer
        hidden = []

        for i in range(self.hidden_size):
            value = self.b1[i]

            for j in range(self.hidden_size):
                value += self.w1[i][j] * x[j]

            hidden.append(self.relu(value))

        # Output logits
        logits = []

        for i in range(self.vocab_size):
            value = self.b2[i]

            for j in range(self.hidden_size):
                value += self.w2[i][j] * hidden[j]

            logits.append(value)

        probabilities = self.softmax(logits)

        return probabilities

    # --------------------------------------------------
    # PREDICTION
    # --------------------------------------------------

    def predict_next(self, token_id):
        probabilities = self.forward(token_id)

        best_id = 0
        best_probability = probabilities[0]

        for i, probability in enumerate(probabilities):
            if probability > best_probability:
                best_id = i
                best_probability = probability

        return best_id, best_probability

    def train_step(
        self,
        token_id,
        target_id,
        learning_rate=0.01
    ):
        if token_id < 0 or token_id >= self.vocab_size:
            token_id = 1

        if target_id < 0 or target_id >= self.vocab_size:
            target_id = 1

        # Forward pass
        x = self.embedding[token_id]

        hidden = []

        for i in range(self.hidden_size):
            value = self.b1[i]

            for j in range(self.hidden_size):
                value += self.w1[i][j] * x[j]

            hidden.append(self.relu(value))

        logits = []

        for i in range(self.vocab_size):
            value = self.b2[i]

            for j in range(self.hidden_size):
                value += self.w2[i][j] * hidden[j]

            logits.append(value)

        probabilities = self.softmax(logits)

        # Cross-entropy loss
        target_probability = max(
            probabilities[target_id],
            1e-12
        )

        loss = -math.log(target_probability)

        # Output gradient
        output_gradient = probabilities[:]
        output_gradient[target_id] -= 1.0

        # Simpan W2 sebelum update
        old_w2 = [
            row[:]
            for row in self.w2
        ]

        # Hidden gradient
        hidden_gradient = [
            0.0
            for _ in range(self.hidden_size)
        ]

        for j in range(self.hidden_size):
            gradient = 0.0

            for i in range(self.vocab_size):
                gradient += (
                    output_gradient[i]
                    * old_w2[i][j]
                )

            if hidden[j] > 0:
                hidden_gradient[j] = gradient

        # Update output layer
        for i in range(self.vocab_size):

            for j in range(self.hidden_size):
                self.w2[i][j] -= (
                    learning_rate
                    * output_gradient[i]
                    * hidden[j]
                )

            self.b2[i] -= (
                learning_rate
                * output_gradient[i]
            )

        # Simpan W1 sebelum update
        old_w1 = [
            row[:]
            for row in self.w1
        ]

        # Update hidden layer
        for i in range(self.hidden_size):

            for j in range(self.hidden_size):
                self.w1[i][j] -= (
                    learning_rate
                    * hidden_gradient[i]
                    * x[j]
                )

            self.b1[i] -= (
                learning_rate
                * hidden_gradient[i]
            )

        # Embedding gradient
        embedding_gradient = [
            0.0
            for _ in range(self.hidden_size)
        ]

        for j in range(self.hidden_size):

            gradient = 0.0

            for i in range(self.hidden_size):
                gradient += (
                    hidden_gradient[i]
                    * old_w1[i][j]
                )

            embedding_gradient[j] = gradient

        # Update embedding
        for j in range(self.hidden_size):
            self.embedding[token_id][j] -= (
                learning_rate
                * embedding_gradient[j]
            )

        return loss


