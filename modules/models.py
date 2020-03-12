from django.db import models


class LecturerInfo(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.TextField()

    # teaches = models.ManyToManyField('ModuleInfo')
    def __str__(self):
        return self.code + "-" + self.name


class ModuleInfo(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    title = models.TextField()
    year = models.CharField(max_length=4)
    semester = models.IntegerField()
    taughtBy = models.ManyToManyField('LecturerInfo')

    def __str__(self):
        return self.code + "-" + self.title


class Rating(models.Model):
    rating = models.IntegerField()
    module = models.ForeignKey('ModuleInfo', on_delete=models.CASCADE, default=None)
    lecturer = models.ForeignKey('LecturerInfo', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.module.code + "-" + self.lecturer.code + ": " + str(self.rating)
