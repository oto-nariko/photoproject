from django.db import models
from accounts.models import CustomUser

class Category(models.Model):

    title = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=20)

    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    comment = models.TextField(
        verbose_name='コメント',  # フィールドのタイトル
        )
    image1 = models.ImageField(
        verbose_name='イメージ1',# フィールドのタイトル
        upload_to = 'photos'   # MEDIA_ROOT以下のphotosにファイルを保存  
        )
    image2 = models.ImageField(
        verbose_name='イメージ2',# フィールドのタイトル
        upload_to = 'photos',  # MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,            # フィールド値の設定は必須でない
        null=True              # データベースにnullが保存されることを許容
        )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True       # 日時を自動追加
        )
    
    def __str__(self):
        return self.title
    