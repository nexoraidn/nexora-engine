class NexoraTrainer:
    def __init__(self, model):
        self.model = model

    def train(self, dataset, epochs=10, learning_rate=0.01):
        for epoch in range(epochs):
            total_loss = 0.0

            for item in dataset:
                token_ids = item["input_ids"]

                if not token_ids:
                    continue

                # Target sederhana untuk tahap awal:
                # setiap token dianggap sebagai target positif.
                targets = [1] * len(token_ids)

                loss = self.model.train_step(
                    token_ids,
                    targets,
                    learning_rate
                )

                total_loss += loss

            print(
                f"Epoch {epoch + 1}/{epochs} - "
                f"Loss: {total_loss}"
            )


if __name__ == "__main__":
    from tokenizer import NexoraTokenizer
    from data_processor import NexoraDataProcessor
    from model import NexoraModel

    data = [
        "halo nexora",
        "siapa kamu",
        "saya adalah nexora engine",
        "nexora adalah teknologi"
    ]

    tokenizer = NexoraTokenizer()
    tokenizer.build_vocab(data)

    processor = NexoraDataProcessor(tokenizer)
    dataset = processor.build_dataset(data)

    model = NexoraModel(
        vocab_size=len(tokenizer.vocab)
    )

    trainer = NexoraTrainer(model)

    trainer.train(
        dataset,
        epochs=5,
        learning_rate=0.01
    )
