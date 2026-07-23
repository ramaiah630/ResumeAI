import reflex as rx


class ResumeState(rx.State):
    full_name: str = "Dhasaradha Ramaiah"
    email: str = "ramaiah@example.com"
    phone: str = "7207805637"
    summary: str = "Passionate software engineer..."

    def set_full_name(self, value: str):
        self.full_name = value

    def set_email(self, value: str):
        self.email = value

    def set_phone(self, value: str):
        self.phone = value

    def set_summary(self, value: str):
        self.summary = value