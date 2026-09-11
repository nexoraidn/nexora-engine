class NexoraEngine:
    def __init__(self):
        self.name = "Nexora Engine"
        self.version = "0.1"

    def respond(self, message):
        message = message.lower().strip()

        if message in ["halo", "hai", "hello"]:
            return "Halo! Saya Nexora Engine v0.1 🤖"

        if "siapa kamu" in message:
            return "Saya Nexora Engine, mesin AI eksperimen milik Nexora."

        if "siapa penciptamu" in message:
            return "Saya diciptakan dan dikembangkan oleh Nexora."

        if "nexora" in message:
            return "Nexora adalah teknologi yang sedang saya pelajari."

        return "Saya menerima pesan: " + message


if __name__ == "__main__":
    engine = NexoraEngine()

    while True:
        user_input = input("Kamu: ")

        if user_input.lower() in ["exit", "quit", "keluar"]:
            print("Nexora Engine dimatikan.")
            break

        print("Nexora:", engine.respond(user_input))
