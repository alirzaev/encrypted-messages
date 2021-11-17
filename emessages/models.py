from django.db import models


class EncryptedMessage(models.Model):
    encrypted_text = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Encrypted message created at {self.created_at}'
