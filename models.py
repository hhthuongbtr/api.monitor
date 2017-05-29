# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agent(models.Model):
    name = models.CharField(unique=True, max_length=45)
    ip = models.CharField(unique=True, max_length=45)
    descr = models.CharField(max_length=100)
    thread = models.IntegerField()
    cpu = models.IntegerField()
    mem = models.IntegerField()
    disk = models.IntegerField()
    last_update = models.IntegerField()
    active = models.IntegerField()
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'agent'


class Capture(models.Model):
    pid = models.IntegerField()
    profile_id = models.IntegerField()
    start_time = models.CharField(max_length=50)
    time = models.IntegerField()
    file_luu = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    server_id = models.IntegerField()
    flag = models.IntegerField()
    folder_id = models.IntegerField()
    user_id = models.IntegerField()
    days = models.CharField(max_length=15, blank=True, null=True)
    active = models.IntegerField()
    folder_upload = models.CharField(max_length=200, blank=True, null=True)
    ep = models.CharField(max_length=10, blank=True, null=True)
    ep_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'capture'


class Catv(models.Model):
    name = models.CharField(max_length=45)
    ip = models.CharField(max_length=45)
    chassis_id = models.IntegerField()
    descr = models.CharField(max_length=100)
    bitrate = models.IntegerField()
    status = models.IntegerField()
    check = models.IntegerField()
    last_update = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catv'


class Channel(models.Model):
    name = models.CharField(max_length=45)
    descr = models.CharField(max_length=100)
    group_id = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'channel'


class Chassis(models.Model):
    name = models.CharField(max_length=45)
    ip = models.CharField(max_length=45)
    descr = models.CharField(max_length=100)
    snmp_port = models.IntegerField()
    version = models.CharField(max_length=10)
    community = models.CharField(db_column='Community', max_length=45)  # Field name made lowercase.
    status = models.IntegerField()
    check = models.IntegerField()
    last_update = models.IntegerField()
    flag = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chassis'


class Command(models.Model):
    name = models.CharField(max_length=45)
    cmd = models.TextField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'command'


class Contact(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    priority = models.SmallIntegerField()
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'
        unique_together = (('id', 'email'),)


class Folder(models.Model):
    server_id = models.IntegerField()
    path = models.CharField(max_length=200)
    descr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folder'


class Group(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'group'


class Logs(models.Model):
    id = models.BigAutoField(primary_key=True)
    host = models.CharField(max_length=128, blank=True, null=True)
    facility = models.CharField(max_length=10, blank=True, null=True)
    priority = models.CharField(max_length=10, blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    program = models.CharField(max_length=15, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField()
    counter = models.IntegerField()
    fo = models.DateTimeField(blank=True, null=True)
    lo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class Mediainfo(models.Model):
    overall_bitrate_mode = models.CharField(max_length=40)
    overall_bitrate = models.IntegerField()
    critical_bitrate = models.IntegerField()
    video_format = models.CharField(max_length=20)
    video_format_profile = models.CharField(max_length=20)
    video_format_cabac = models.CharField(max_length=10)
    video_format_reframes = models.IntegerField()
    video_format_gop = models.CharField(max_length=20)
    width = models.IntegerField()
    height = models.IntegerField()
    display_aspect_ratio = models.CharField(max_length=10)
    scan_type = models.CharField(max_length=20)
    frame_rate = models.SmallIntegerField()
    video_bitrate_mode = models.CharField(max_length=20)
    video_bitrate = models.IntegerField()
    audio_format = models.CharField(max_length=10)
    audio_format_profile = models.CharField(max_length=20)
    channel_count = models.SmallIntegerField()
    audio_bitrate_mode = models.CharField(max_length=20)
    audio_bitrate = models.IntegerField()
    profile_id = models.IntegerField()
    check = models.IntegerField()
    last_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mediainfo'


class Profile(models.Model):
    id = models.AutoField(unique=True)
    ip = models.CharField(unique=True, max_length=100)
    descr = models.CharField(max_length=100)
    status = models.IntegerField()
    type = models.CharField(max_length=32)
    channel = models.ForeignKey(Channel, models.DO_NOTHING)
    protocol = models.CharField(max_length=10)
    graph = models.IntegerField()
    logo = models.IntegerField()
    check = models.IntegerField()
    sendmail = models.IntegerField()
    monitor = models.IntegerField()
    mediainfo = models.IntegerField()
    streamguru = models.IntegerField()
    last_update = models.IntegerField()
    change_status = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'
        unique_together = (('id', 'ip'),)


class ProfileAgent(models.Model):
    profile_id = models.IntegerField()
    agent_id = models.IntegerField()
    status = models.IntegerField()
    analyzer_status = models.IntegerField()
    dropframe = models.IntegerField()
    dropframe_threshold = models.IntegerField()
    discontinuity = models.IntegerField()
    discontinuity_threshold = models.IntegerField()
    check = models.IntegerField()
    video = models.IntegerField()
    audio = models.IntegerField()
    monitor = models.IntegerField()
    analyzer = models.IntegerField()
    last_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_agent'
        unique_together = (('profile_id', 'agent_id'),)


class ProfileGroup(models.Model):
    profile_id = models.IntegerField()
    permission = models.SmallIntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profile_group'
        unique_together = (('profile_id', 'group_id'),)


class Server(models.Model):
    name = models.CharField(unique=True, max_length=45)
    ip = models.CharField(unique=True, max_length=45)
    descr = models.CharField(max_length=100)
    os = models.CharField(max_length=32)
    cpu = models.IntegerField()
    mem = models.IntegerField()
    disk = models.IntegerField()
    last_update = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'server'


class Streamguru(models.Model):
    continuity_count_error = models.SmallIntegerField()
    profile_id = models.IntegerField()
    last_update = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'streamguru'


class Timeshift(models.Model):
    mode = models.IntegerField()
    pid = models.IntegerField()
    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    status_input = models.IntegerField()
    status_output = models.IntegerField()
    status_process = models.IntegerField()
    type_input = models.CharField(max_length=32)
    type_output = models.CharField(max_length=32)
    check_input = models.IntegerField()
    check_output = models.IntegerField()
    last_update = models.IntegerField()
    change_status = models.IntegerField()
    command_id = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'timeshift'


class Transcode(models.Model):
    pid = models.IntegerField()
    flag = models.IntegerField()
    status = models.IntegerField()
    active = models.IntegerField()
    command = models.ForeignKey(Command, models.DO_NOTHING)
    server = models.ForeignKey(Server, models.DO_NOTHING)
    output = models.CharField(max_length=100)
    input_id = models.IntegerField()
    last_reset = models.IntegerField()
    auto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'transcode'


class User(models.Model):
    type = models.IntegerField()
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
