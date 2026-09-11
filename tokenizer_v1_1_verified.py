class NexoraTokenizer:
    def __init__(self):
        self.vocab = {
            "<PAD>": 0,
            "<UNK>": 1,
            "<BOS>": 2,
            "<EOS>": 3
        }

    def tokenize(self, text):
        text = text.lower().strip()
        return text.split()

    def build_vocab(self, texts):
        for text in texts:
            tokens = self.tokenize(text)

            for token in tokens:
                if token not in self.vocab:
                    self.vocab[token] = len(self.vocab)

    def encode(self, text):
        tokens = self.tokenize(text)

        return [
            self.vocab.get(token, self.vocab["<UNK>"])
            for token in tokens
        ]

    def decode(self, token_ids):
        reverse_vocab = {
            value: key
            for key, value in self.vocab.items()
        }

        return " ".join(
            reverse_vocab.get(token_id, "<UNK>")
            for token_id in token_ids
        )


if __name__ == "__main__":
    tokenizer = NexoraTokenizer()

    data = [
        "halo nexora",
        "siapa kamu",
        "saya adalah nexora engine",
        "nexora adalah teknologi"
    ]

    tokenizer.build_vocab(data)

    text = "halo nexora"

    print("Text:", text)
    print("Tokens:", tokenizer.tokenize(text))
    print("Encoded:", tokenizer.encode(text))
    print("Decoded:", tokenizer.decode(tokenizer.encode(text)))
