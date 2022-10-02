from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=40, verbose_name="Название роли")

    def __str__(self):
        return self.role_name


class Team(models.Model):
    f_name = models.CharField(max_length=20, verbose_name="Имя")
    l_name = models.CharField(max_length=20, verbose_name="Фамилия")
    slug = models.SlugField(max_length=90, db_index=True, unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="Роль в команде")
    tasks = models.TextField(verbose_name="Задачи в рамках проекта", blank=True)
    projects = models.TextField(verbose_name="Проекты, в которых принимал(а) участие", blank=True)

    def __str__(self):
        return self.f_name, self.l_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('person_slug', kwargs={'slug': self.slug})


class about_project(models.Model):
    project_name = models.CharField(max_length=90, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта", blank=True)

    def __str__(self):
        return self.project_name


class project_changes(models.Model):
    person_who_made_changes = models.ForeignKey(Team, on_delete=models.PROTECT,
                                                verbose_name="Участник, который внёс последние изменения")
    number_of_lines = models.IntegerField(verbose_name="Количество строк")
    commits = models.TextField(verbose_name="Коммиты", blank=True)

    def __str__(self):
        return self.number_of_lines
