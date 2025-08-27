from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Store tags as a plain text string (comma-separated)
    tags = models.TextField(help_text="Comma-separated tags, e.g. Python,Django,ML")
    imageUrl = models.URLField()
    url = models.URLField(help_text="Link to project, e.g., GitHub or live demo")  # new field

    def get_tags(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    date = models.DateField()
    imageUrl = models.URLField()
    url = models.URLField(help_text="Link to full blog post, e.g., Medium URL")  # new field

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
