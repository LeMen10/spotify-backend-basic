from django.db import models
from .user import User

class GroupMessage(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "group_messages"

class GroupMember(models.Model):
    group = models.ForeignKey(GroupMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "group_members"

class PrivateChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_chats")
    ai = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ai_chats")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "private_chats"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupMessage, on_delete=models.CASCADE)
    private_chat = models.ForeignKey(
        PrivateChat, null=True, blank=True, on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
