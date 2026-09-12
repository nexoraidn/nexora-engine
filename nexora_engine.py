class NexoraEngine:
    def __init__(self):
        self.name = "Nexora Engine"
        self.version = "0.3"
        self.history = []

    def respond(self, message):
        message = message.lower().strip()

        if message == "/help":
            return (
                "Perintah Nexora Engine:\n"
                "/help - melihat bantuan\n"
                "/status - melihat status engine\n"
                "/clear - menghapus riwayat percakapan\n"
                "exit / quit / keluar - mematikan engine"
            )

        if message == "/status":
            return (
                f"{self.name} v{self.version}\n"
                f"Riwayat pesan: {len(self.history)}"
            )

        if message == "/clear":
            self.history.clear()
            return "Riwayat percakapan telah dihapus."

        self.history.append(message)

        if message in ["halo", "hai", "hello"]:
            return "Halo! Saya Nexora Engine v0.3 🤖"

        if "siapa kamu" in message:
            return (
                "Saya Nexora Engine, mesin AI eksperimen "
                "yang sedang dikembangkan oleh Nexora."
            )

        if "siapa penciptamu" in message:
            return (
                "Saya dikembangkan sebagai bagian dari proyek "
                "Nexora untuk membangun teknologi AI sendiri."
            )

        if "apa itu nexora" in message:
            return (
                "Nexora adalah proyek teknologi yang sedang "
                "mengembangkan sistem digital dan kecerdasan buatan."
            )

        if "terima kasih" in message or "makasih" in message:
            return "Sama-sama 🤖"

        if "selamat pagi" in message:
            return "Selamat pagi! Saya Nexora Engine v0.3 🤖"

        if "selamat malam" in message:
            return "Selamat malam! Saya Nexora Engine v0.3 🤖"

        return "Saya belum memahami pertanyaan itu."


if __name__ == "__main__":
    engine = NexoraEngine()

    while True:
        user_input = input("Kamu: ")

        if user_input.lower().strip() in ["exit", "quit", "keluar"]:
            print("Nexora Engine dimatikan.")
            break

        print("Nexora:", engine.respond(user_input))
