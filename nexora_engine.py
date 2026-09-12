
class NexoraEngine:
    def __init__(self):
        self.name = "Nexora Engine"
        self.version = "1.2"
        self.history = []
        self.context = {}

    def respond(self, message):
        original_message = message.strip()
        message = original_message.lower()

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
                f"Riwayat pesan: {len(self.history)}\n"
                f"Konteks tersimpan: {len(self.context)}"
            )

        if message == "/clear":
            self.history.clear()
            self.context.clear()
            return "Riwayat dan konteks percakapan telah dihapus."

        self.history.append(original_message)

        # Menyimpan nama pengguna
        if message.startswith("nama saya "):
            user_name = original_message[10:].strip()

            if user_name:
                self.context["user_name"] = user_name
                return f"Senang mengenalmu, {user_name}!"

        # Menjawab nama pengguna
        if "siapa nama saya" in message or "nama saya siapa" in message:
            user_name = self.context.get("user_name")

            if user_name:
                return f"Nama kamu {user_name}."

            return "Kamu belum memberitahu nama kamu."

        # Menyimpan aktivitas pengguna
        if message.startswith("saya sedang "):
            activity = original_message[12:].strip()

            if activity:
                self.context["activity"] = activity
                return f"Baik, kamu sedang {activity}."

        # Menjawab aktivitas pengguna
        if "saya sedang apa" in message or "apa yang sedang saya lakukan" in message:
            activity = self.context.get("activity")

            if activity:
                return f"Kamu sedang {activity}."

            return "Kamu belum memberitahu aktivitasmu."

        # Ringkasan konteks pengguna
        if "ceritakan tentang saya" in message:
            user_name = self.context.get("user_name")
            activity = self.context.get("activity")

            if user_name and activity:
                return (
                    f"Nama kamu {user_name} "
                    f"dan kamu sedang {activity}."
                )

            if user_name:
                return f"Nama kamu {user_name}."

            if activity:
                return f"Kamu sedang {activity}."

            return "Saya belum memiliki informasi tentang kamu."

        # Sapaan
        if message in ["halo", "hai", "hello"]:
            return "Halo! Saya Nexora Engine v1.2 🤖"

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
            return "Selamat pagi! Saya Nexora Engine v1.2 🤖"

        if "selamat malam" in message:
            return "Selamat malam! Saya Nexora Engine v1.2 🤖"

        return "Saya belum memahami pertanyaan itu."


if __name__ == "__main__":
    engine = NexoraEngine()

    while True:
        user_input = input("Kamu: ")

        if user_input.lower().strip() in ["exit", "quit", "keluar"]:
            print("Nexora Engine dimatikan.")
            break

        print("Nexora:", engine.respond(user_input))
