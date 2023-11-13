from django.db import models

# Create your models here.


class Barracks(models.Model):
    purpose_choise = [
        (1, "Для рядовых"),
        (2, "Для офицеров")
    ]

    number = models.IntegerField()
    capacity = models.IntegerField()
    purpose = models.IntegerField(choices=purpose_choise, default=1)

    def __str__(self):
        return f'Казарма №{self.number}'

    class Meta:
        verbose_name = 'Казарма'
        verbose_name_plural = 'Казармы'


class Weapon(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return f'Табельный номер оружия {self.number}'

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружие'


class Military(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    service_start_date = models.CharField(max_length=255)
    service_end_date = models.CharField(max_length=255, default='н.в.')
    barracks_number = models.ForeignKey(Barracks, on_delete=models.PROTECT)
    received_weapon = models.OneToOneField(Weapon, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    class Meta:
        verbose_name = 'Военный'
        verbose_name_plural = 'Военные'
