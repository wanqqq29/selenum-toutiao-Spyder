from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class groupList(models.Model):
    gName = models.CharField(max_length=100, blank=False, verbose_name=("账号名称"))
    gID = models.CharField(max_length=100, blank=False, verbose_name=("账号ID"))
    class Meta:
        db_table = 'groupList'

class artical(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(groupList, verbose_name=_("所属账号"), null=True, on_delete=models.SET_NULL, db_constraint=False)
    title = models.CharField(max_length=100, blank=False, verbose_name=("文章标题"))
    href = models.CharField(max_length=100, blank=False, verbose_name=("文章链接"))
    content = models.CharField(max_length=10000, blank=False, verbose_name=("文章内容"))
    class Meta:
        db_table = 'artical'

