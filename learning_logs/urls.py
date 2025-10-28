"""定义 learning_logs的 URL 模式"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #主页
    path('',views.index,name='index'),

    #主题页
    path('topics/',views.topics,name='topics'),

    #某一主题下所有笔记详情页
    path('topics/<int:topic_id>/',views.topic,name='topic'),

    #用于添加新主题的页面
    path('new_topic/',views.new_topic,name='new_topic'),

    #用于添加新条目的页面,定义一个带参数的 URL 路径
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),

    #用于编辑条目的页面
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry')


]


"""这是 URL 的路径规则，用于匹配用户访问的具体 URL（如 http://网站域名/new_entry/3/）。
<int:topic_id> 是路径参数（Django 的路径转换器语法）：
int：指定参数类型为 “整数”（限制只能传递数字，非数字会匹配失败）。
topic_id：参数名称，用于标识 “要添加条目所属的主题 ID”（比如3表示第 3 个主题）。
作用：当用户访问 new_entry/5/ 时，Django 会自动提取5作为topic_id参数，传递给视图函数。"""