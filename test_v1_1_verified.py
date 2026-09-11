from tokenizer import NexoraTokenizer
from data_processor import NexoraDataProcessor
from model import NexoraModel
from trainer import NexoraTrainer


data = [
    "halo nexora",
    "siapa kamu",
    "saya adalah nexora engine",
    "nexora adalah teknologi"
]


print("=== NEXORA ENGINE TEST ===")

# 1. Tokenizer
tokenizer = NexoraTokenizer()
tokenizer.build_vocab(data)

print("\n[1] Vocabulary:")
print(tokenizer.vocab)

# 2. Data Processor
processor = NexoraDataProcessor(tokenizer)
dataset = processor.build_dataset(data)

print("\n[2] Dataset:")
for item in dataset:
    print(item)

# 3. Model
model = NexoraModel(
    vocab_size=len(tokenizer.vocab)
)

print("\n[3] Initial Prediction:")
print(model.predict_next(dataset[0]["input_ids"][-1]))

# 4. Trainer
trainer = NexoraTrainer(model)

print("\n[4] Training:")
trainer.train(
    dataset,
    epochs=3,
    learning_rate=0.01
)

# 5. Test setelah training
print("\n[5] Prediction After Training:")
print(model.predict_next(dataset[0]["input_ids"][-1]))

print("\n=== TEST SELESAI ===")
