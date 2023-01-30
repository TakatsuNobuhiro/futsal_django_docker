from django.db import models


class Club(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'チーム'
        db_table = 'club'
        ordering = ['name']

    name = models.CharField("チーム名", max_length=32,
                            help_text="（例）東京工業大学フットサル部 Tokyo Tech")
    homepage_url = models.URLField("ホームページ（URL）", blank=True, null=True)

    # image
    # category
    # twitter
    # instagram
    # facebook


class Member(models.Model):
    def __str__(self):
        return self.last_name + self.first_name

    class Meta:
        verbose_name_plural = '選手'
        db_table = 'member'
        ordering = ['birth_day']

    club = models.ForeignKey(to=Club, on_delete=models.CASCADE)
    MEMBER_TYPE = (
        (1, "プレイヤー"),
        (2, "スタッフ"),
        (3, "スタッフ兼プレイヤー"),
    )
    type = models.IntegerField("種類", choices=MEMBER_TYPE)
    last_name = models.CharField("苗字（漢字）", max_length=32,
                                 help_text="(例) 森岡")
    first_name = models.CharField("名前（漢字）", max_length=32, help_text="（例）薫")
    uniform_number = models.IntegerField("背番号",
                                         help_text="所属チームでの背番号")
    birth_day = models.DateField("誕生日", help_text="（例）1998-06-22", blank=True,
                                 null=True)

    POSITION_LIST = (
        (1, "フィクソ（FIXO）"),
        (2, "アラ（ALA）"),
        (3, "ピヴォ（PIVO）"),
        (4, "ゴレイロ（GOLEIRO）")
    )
    position = models.IntegerField("ポジション", choices=POSITION_LIST)
    profile = models.TextField("プロフィール", blank=True, null=True)

    # image
    # twitter
    # instagram
    # facebook


class League(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "リーグ"
        db_table = 'league'

    name = models.CharField("リーグ名", max_length=32)
    teams = models.ManyToManyField("Club")

class Season(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "シーズン"
        db_table = 'season'

    league = models.ForeignKey(to=League, on_delete=models.CASCADE)
    name = models.CharField("シーズン名", max_length=32)


class Category(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "カテゴリー"
        db_table = "category"
        ordering = ["part_number"]

    season = models.ForeignKey(to=Season, on_delete=models.CASCADE)
    name = models.CharField("カテゴリー名", max_length=32)
    part_number = models.IntegerField("部数", help_text="２部リーグ→2")


class Node(models.Model):
    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name_plural = "節"
        db_table = "node"
        ordering = ["number"]

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    number = models.IntegerField("節")


class Place(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "場所"
        db_table = "place"

    name = models.CharField("名前", max_length=32)
    address = models.TextField("住所")


class Referee(models.Model):
    class Meta:
        verbose_name_plural = "審判"
        db_table = "referee"

    last_name = models.CharField("苗字（漢字）", max_length=32,
                                 help_text="(例) 森岡")
    first_name = models.CharField("名前（漢字）", max_length=32, help_text="（例）薫")


class Game(models.Model):
    def __str__(self):
        return str(
            self.node_id) + "節 " + self.home.name + "VS" + self.away.name + self.date.strftime(
            '%Y/%m/%d %H:%M:%S') + " Kick off"

    class Meta:
        verbose_name_plural = "試合"
        db_table = "game"
        ordering = ["date"]

    home = models.ForeignKey(verbose_name="ホームチーム", to=Club,
                             on_delete=models.CASCADE, related_name="home_team")
    away = models.ForeignKey(verbose_name="アウェイチーム", to=Club,
                             on_delete=models.CASCADE, related_name="away_team")
    node = models.ForeignKey(verbose_name="節", to=Node,
                             on_delete=models.CASCADE)
    date = models.DateTimeField("キックオフ時刻")
    place = models.ForeignKey(verbose_name="場所", to=Place,
                              on_delete=models.CASCADE)
    goals = models.ManyToManyField(Member, through="Goal", related_name="goals")
    shoots = models.ManyToManyField(Member, through="Shoot",
                                    related_name="shoots")
    warnings = models.ManyToManyField(Member, through="Warning",
                                      related_name="warnings")
    members = models.ManyToManyField(Member, through="RegisteredMember",
                                     related_name="members")
    staffs = models.ManyToManyField(Member, through="Staff",
                                    related_name="staffs")
    first_referee = models.OneToOneField(to=Referee, on_delete=models.PROTECT,
                                         related_name="first_referee")
    second_referee = models.OneToOneField(to=Referee, on_delete=models.PROTECT,
                                          related_name="second_referee")
    third_referee = models.OneToOneField(to=Referee, on_delete=models.PROTECT,
                                         related_name="third_referee")


class Goal(models.Model):
    class Meta:
        verbose_name_plural = "ゴール"
        db_table = "goal"

    time = models.IntegerField("時間")

    HALF_CHOICES = (
        (False, "前半"),
        (True, "後半")
    )
    half = models.BooleanField("前半or後半", choices=HALF_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Member, on_delete=models.CASCADE)


class Shoot(models.Model):
    class Meta:
        verbose_name_plural = "シュート"
        db_table = "shoot"

    # time = models.IntegerField("時間")

    HALF_CHOICES = (
        (False, "前半"),
        (True, "後半")
    )
    half = models.BooleanField("前半or後半", choices=HALF_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Member, on_delete=models.CASCADE)


class Warning(models.Model):
    class Meta:
        verbose_name_plural = "警告"
        db_table = "warning"

    time = models.IntegerField("時間")

    HALF_CHOICES = (
        (False, "前半"),
        (True, "後半")
    )
    half = models.BooleanField("前半or後半", choices=HALF_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Member, on_delete=models.CASCADE)


class RegisteredMember(models.Model):
    class Meta:
        verbose_name_plural = "登録メンバー"
        db_table = "registered_member"

    REGISTER_MEMBER_CHOICES = (
        (False, "ベンチ"),
        (True, "先発")
    )
    starting_member = models.BooleanField("先発orベンチ",
                                          choices=REGISTER_MEMBER_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Member, on_delete=models.CASCADE)


class Staff(models.Model):
    class Meta:
        verbose_name_plural = "役員（スタッフ）"
        db_table = "staff"

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
