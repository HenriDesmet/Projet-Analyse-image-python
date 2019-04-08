# Django imports
from django.db import models
from django.utils import timezone

class ReferenceImg(models.Model):
    img_name = models.CharField(max_length=100)
    img_desc = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date added")

    class Meta:
        verbose_name = "Image Reference"
        ordering = ['img_name']

    def __str__(self):
        return self.img_name


class ResourceAnalyse(models.Model):
    client = models.TextField(null=True, default="Default client infos")
    results = models.ManyToManyField('AnalyseResults')
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date created")

    class Meta:
        verbose_name = "Analyse Infos"
        ordering = ['id']

    def __str__(self):
        res = "Resource Analyse. Id: " + str(self.id) + " | Results :"
        for r in self.results.all():
            res += "\n- "
            res += str(r)

        return res

    def delete_results(self):
        for res in self.results.all():
            res.delete()

    def get_data(self, url):
        res = {
            "date": str(self.date),
            "client": self.client,
            "results": []
        }
        for result in self.results.all():
            res["results"].append(result.get_data(url))

        return res

class AnalyseResults(models.Model):
    image = models.ForeignKey('ReferenceImg', on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        verbose_name = "Analyse Result"
        ordering = ['id']

    def __str__(self):
        return "Analyse Result. Id: "+str(self.id)+" | Image: "+str(self.image.img_name)+" | Score: "+str(self.score)

    def get_data(self, url):
        res = {
            "image_url": url + self.image.img_name,
            "score": self.score
        }
        return res
