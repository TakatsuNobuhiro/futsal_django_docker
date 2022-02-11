from django.db import models


class Club(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'チーム'
        verbose_name_plural = 'チーム'
        db_table = 'club'
        ordering = 'name'

    name = models.CharField("チーム名", max_length=32,
                            help_text="（例）東京工業大学フットサル部 Tokyo Tech")
    homepage_url = models.URLField("ホームページ（URL）")

    # image
    # category
    # twitter
    # instagram
    # facebook

class Player(models.Model):
    def __str__(self):
        return self.last_name + self.first_name
    class Meta:
        verbose_name = '選手'
        verbose_name_plural = '選手'
        db_table = 'player'
        ordering = 'birth_day'

    club = models.ForeignKey(to=Club, on_delete=models.CASCADE)
    last_name = models.CharField("苗字（漢字）", max_length=32,
                                 help_text="(例) 森岡")
    first_name = models.CharField("名前（漢字）", max_length=32, help_text="（例）薫")
    uniform_number = models.IntegerField("背番号",
                                         help_text="所属チームでの背番号")
    birth_day = models.DateField("誕生日", help_text="（例）1998-06-22")

    POSITION_LIST = (
        (1, "フィクソ（FIXO）"),
        (2, "アラ（ALA）"),
        (3, "ピヴォ（PIVO）"),
        (4, "ゴレイロ（GOLEIRO）")
    )
    position = models.IntegerField("ポジション", choices=POSITION_LIST)
    # profile = models.TextField("プロフィール")

    # image
    # twitter
    # instagram
    # facebook
