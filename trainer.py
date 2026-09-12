class NexoraTrainer:
    def __init__(self, model, tokenizer=None):
        self.model = model
        self.tokenizer = tokenizer

    def train(self, dataset, epochs=10, learning_rate=0.01):
        eos_id = None

        if self.tokenizer is not None:
            eos_id = self.tokenizer.vocab.get("<EOS>")

        for epoch in range(epochs):
            total_loss = 0.0
            total_steps = 0

            for item in dataset:
                token_ids = item["input_ids"]

                if not token_ids:
                    continue

                for i in range(len(token_ids)):
                    token_id = token_ids[i]

                    if i + 1 < len(token_ids):
                        target_id = token_ids[i + 1]
                    elif eos_id is not None:
                        target_id = eos_id
                    else:
                        target_id = token_ids[i]

                    loss = self.model.train_step(
                        token_id,
                        target_id,
                        learning_rate
                    )

                    total_loss += loss
                    total_steps += 1

            average_loss = (
                total_loss / total_steps
                if total_steps > 0
                else 0.0
            )

            print(
                f"Epoch {epoch + 1}/{epochs} - "
                f"Loss: {average_loss:.6f}"
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

    trainer = NexoraTrainer(model, tokenizer)

    trainer.train(
        dataset,
        epochs=5,
        learning_rate=0.01
    )
