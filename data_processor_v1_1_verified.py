class NexoraDataProcessor:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def prepare_text(self, text):
        if not isinstance(text, str):
            raise TypeError("Input harus berupa string.")

        return text.strip()

    def encode_text(self, text):
        text = self.prepare_text(text)
        return self.tokenizer.encode(text)

    def build_dataset(self, texts):
        dataset = []

        for text in texts:
            encoded = self.encode_text(text)

            dataset.append({
                "text": text,
                "tokens": self.tokenizer.tokenize(text),
                "input_ids": encoded
            })

        return dataset


if __name__ == "__main__":
    from tokenizer import NexoraTokenizer

    tokenizer = NexoraTokenizer()

    data = [
        "halo nexora",
        "siapa kamu",
        "saya sedang belajar AI",
        "nexora adalah teknologi"
    ]

    tokenizer.build_vocab(data)

    processor = NexoraDataProcessor(tokenizer)
    dataset = processor.build_dataset(data)

    for item in dataset:
        print(item)
