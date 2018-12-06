from django.db import models

# Create your models here.


class phySemSubject(models.Model):
    subject_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=50)
    syllabus = models.CharField(max_length=100)
    image = models.FileField(null=True)
    link = models.CharField(default='#', max_length=100)

    def __str__(self):
        return self.subject_name


class chemSemSubject(models.Model):
    subject_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=50)
    syllabus = models.CharField(max_length=100)
    image = models.FileField(null=True)
    link = models.CharField(default='#', max_length=100)

    def __str__(self):
        return self.subject_name


class cpAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class cpNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class cpEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class cpQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class cpPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class chemAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class chemNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class chemEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class chemQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class chemPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class mathsAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class mathsNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class mathsEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class mathsQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class mathsPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class physicsAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class physicsNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class physicsEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class physicsQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class physicsPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class eeAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class eeNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class eeEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class eeQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class eePractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class emAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class emNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class emEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class emQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class emPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class edAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class edNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class edEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class edQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class edPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class ssAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class ssNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class ssEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class ssQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class ssPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class csAssignment(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class csNote(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title


class csEbook(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)

    def __str__(self):
       return self.title


class csQpaper(models.Model):
      title = models.CharField(max_length=100)
      file = models.FileField()

      def __str__(self):
          return self.title


class csPractical(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.title