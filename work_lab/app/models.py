from django.db import models

# Create your models here.


class Barracks(models.Model):
    purpose_choise = [
        (1, "Для рядовых"),
        (2, "Для офицеров")
    ]

    number = models.IntegerField(verbose_name='Номер')
    capacity = models.IntegerField(verbose_name='Вместимость')
    purpose = models.IntegerField(choices=purpose_choise, default=1, verbose_name='Назначение')
    for_choise_barrak = ("Казарма №"+str(number))

    def __str__(self):
        return f'Казарма №{self.number}'

    class Meta:
        verbose_name = 'Казарма'
        verbose_name_plural = 'Казармы'


class Weapon(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    brand = models.CharField(max_length=255, verbose_name='Марка')
    number = models.IntegerField(verbose_name='Табельный номер')

    def __str__(self):
        return f'Табельный номер оружия {self.number}'

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружие'


class Military(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    service_start_date = models.CharField(max_length=255, verbose_name='Начало службы')
    service_end_date = models.CharField(max_length=255, default='н.в.', verbose_name='Окончание службы')
    barracks_number = models.ForeignKey(Barracks, on_delete=models.PROTECT, verbose_name='Номер казармы')
    received_weapon = models.OneToOneField(Weapon, on_delete=models.PROTECT, verbose_name='Табельный номер оружия')

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    class Meta:
        verbose_name = 'Военный'
        verbose_name_plural = 'Военные'
