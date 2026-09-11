class NexoraModel:
    def __init__(self, vocab_size):
        self.vocab_size = vocab_size
        self.weights = {}

    def initialize(self, token_ids):
        for token_id in token_ids:
            if token_id not in self.weights:
                self.weights[token_id] = 0.0

    def predict(self, token_ids):
        predictions = []

        for token_id in token_ids:
            weight = self.weights.get(token_id, 0.0)

            if weight >= 0:
                predictions.append(1)
            else:
                predictions.append(0)

        return predictions

    def train_step(self, token_ids, targets, learning_rate=0.01):
        self.initialize(token_ids)

        loss = 0.0

        for token_id, target in zip(token_ids, targets):
            prediction = self.predict([token_id])[0]

            error = target - prediction

            self.weights[token_id] += learning_rate * error

            loss += abs(error)

        return loss


if __name__ == "__main__":
    model = NexoraModel(vocab_size=10)

    token_ids = [1, 2, 3, 2]
    targets = [1, 1, 0, 1]

    print("Initial prediction:", model.predict(token_ids))

    loss = model.train_step(token_ids, targets)

    print("Training loss:", loss)
    print("Prediction after training:", model.predict(token_ids))
