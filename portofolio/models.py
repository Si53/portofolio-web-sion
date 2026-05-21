from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.CharField(
        max_length=255,
        help_text="Contoh: images/net.png"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=120)
    period = models.CharField(max_length=100)
    image_path = models.CharField(
        max_length=255,
        help_text="Contoh: images/netsc.png"
    )
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class ExperiencePoint(models.Model):
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name="points"
    )
    label = models.CharField(max_length=100)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "label"]

    def __str__(self):
        return f"{self.experience.title} - {self.label}"


class ExperienceLink(models.Model):
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name="links"
    )
    title = models.CharField(max_length=100)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Education(models.Model):
    year = models.CharField(max_length=50)
    institution = models.CharField(max_length=120)
    major = models.CharField(max_length=120)
    logo_path = models.CharField(
        max_length=255,
        help_text="Contoh: images/telkom.png"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "year"]

    def __str__(self):
        return self.institution


class ContactLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(
        max_length=255,
        help_text="Contoh: mailto:sionmg93@gmail.com atau https://github.com/Si53"
    )
    icon_class = models.CharField(
        max_length=100,
        help_text="Contoh: fa-brands fa-github"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name