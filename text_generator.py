from tokenizer import NexoraTokenizer
from data_processor import NexoraDataProcessor
from model import NexoraModel
from trainer import NexoraTrainer


class NexoraTextGenerator:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def generate(self, prompt, max_tokens=10):
        token_ids = self.tokenizer.encode(prompt)

        if not token_ids:
            return ""

        generated_ids = token_ids.copy()
        eos_id = self.tokenizer.vocab.get("<EOS>")

        for step in range(max_tokens):
            last_token_id = generated_ids[-1]

            next_token_id, probability = (
                self.model.predict_next(last_token_id)
            )

            if next_token_id == eos_id:
                break

            if next_token_id == last_token_id:
                break

            generated_ids.append(next_token_id)

        return self.tokenizer.decode(generated_ids)


if __name__ == "__main__":
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

    model = NexoraModel(vocab_size=len(tokenizer.vocab))
    trainer = NexoraTrainer(model, tokenizer)

    trainer.train(
        dataset,
        epochs=500,
        learning_rate=0.01
    )

    generator = NexoraTextGenerator(model, tokenizer)

    print("\n=== NEXORA TEXT GENERATOR ===")
    print("Prompt: halo")
    print("Output:", generator.generate("halo", max_tokens=10))
