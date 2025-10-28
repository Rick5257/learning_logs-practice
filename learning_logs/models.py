from django.db import models
from django.contrib.auth.models import User

#print(type(models))
# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #增加数据用户归属
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
    

#定义一个用户输入笔记的模型
class Entry(models.Model):
    """每一个学习笔记的具体内容"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    """ForeignKey（外键）：建立 Entry 与 Topic 模型的 “多对一” 关系（一个 Topic 可以对应多个 Entry，但一个 Entry 只能属于一个 Topic）。
第一个参数 Topic：指定关联的目标模型（即 Entry 属于哪个 Topic）。
on_delete=models.CASCADE：级联删除规则。表示当关联的 Topic 被删除时，所有属于该 Topic 的 Entry 会被自动删除（避免数据库中出现 “无主” 的 Entry）。"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta 是 Django 模型中一个特殊的内部类，用于定义模型的 “元数据”（即模型本身的额外属性，不直接对应数据库字段，但影响模型的行为和展示）。
这里的 Meta 配置：verbose_name_plural = 'entries'
verbose_name_plural：指定模型的 “复数名称”。
Django 默认会将模型名（Entry）的复数形式生成为 Entrys（直接加s），但英语中 Entry 的正确复数是 entries。
该配置的作用是：在 Django admin 后台、错误提示等场景中，当需要显示模型的复数名称时，会使用 entries 而不是默认的 Entrys，保证名称的正确性。"""
        verbose_name_plural = 'entries'

        def __str__(self):
            """"返回模型的字符串表示，方便识别和区分"""
            return f"{self.text[:50]}..."