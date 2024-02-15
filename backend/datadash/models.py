from django.db import models


class Channelsummary(models.Model):
    id = models.BigAutoField(primary_key=True)
    top = models.FloatField(
        db_column="Top", blank=True, null=True
    )  # Field name made lowercase.
    middle = models.FloatField(
        db_column="Middle", blank=True, null=True
    )  # Field name made lowercase.
    bottom = models.FloatField(
        db_column="Bottom", blank=True, null=True
    )  # Field name made lowercase.
    left = models.FloatField(
        db_column="Left", blank=True, null=True
    )  # Field name made lowercase.
    right = models.FloatField(
        db_column="Right", blank=True, null=True
    )  # Field name made lowercase.
    total = models.FloatField(
        db_column="Total", blank=True, null=True
    )  # Field name made lowercase.
    movingbedpercentcorrection = models.FloatField(
        db_column="MovingBedPercentCorrection", blank=True, null=True
    )  # Field name made lowercase.
    fk_qrev_data = models.ForeignKey(
        "QrevData", models.DO_NOTHING, db_column="fk_qrev_data"
    )

    class Meta:
        managed = False
        db_table = "channelsummary"


class Qrev(models.Model):
    id = models.BigAutoField(primary_key=True)
    meanwidth = models.FloatField(
        db_column="MeanWidth", blank=True, null=True
    )  # Field name made lowercase.
    widthcov = models.FloatField(
        db_column="WidthCOV", blank=True, null=True
    )  # Field name made lowercase.
    meanarea = models.FloatField(
        db_column="MeanArea", blank=True, null=True
    )  # Field name made lowercase.
    areacov = models.FloatField(
        db_column="AreaCOV", blank=True, null=True
    )  # Field name made lowercase.
    meanboatspeed = models.FloatField(
        db_column="MeanBoatSpeed", blank=True, null=True
    )  # Field name made lowercase.
    meanqovera = models.FloatField(
        db_column="MeanQoverA", blank=True, null=True
    )  # Field name made lowercase.
    meancoursemadegood = models.FloatField(
        db_column="MeanCourseMadeGood", blank=True, null=True
    )  # Field name made lowercase.
    meanflowdirection = models.FloatField(
        db_column="MeanFlowDirection", blank=True, null=True
    )  # Field name made lowercase.
    meandepth = models.FloatField(
        db_column="MeanDepth", blank=True, null=True
    )  # Field name made lowercase.
    maximumdepth = models.FloatField(
        db_column="MaximumDepth", blank=True, null=True
    )  # Field name made lowercase.
    maximumwaterspeed = models.FloatField(
        db_column="MaximumWaterSpeed", blank=True, null=True
    )  # Field name made lowercase.
    numberoftransects = models.IntegerField(
        db_column="NumberofTransects", blank=True, null=True
    )  # Field name made lowercase.
    duration = models.IntegerField(
        db_column="Duration", blank=True, null=True
    )  # Field name made lowercase.
    leftqper = models.FloatField(
        db_column="LeftQPer", blank=True, null=True
    )  # Field name made lowercase.
    rightqper = models.FloatField(
        db_column="RightQPer", blank=True, null=True
    )  # Field name made lowercase.
    invalidcellsqper = models.FloatField(
        db_column="InvalidCellsQPer", blank=True, null=True
    )  # Field name made lowercase.
    invalidensqper = models.FloatField(
        db_column="InvalidEnsQPer", blank=True, null=True
    )  # Field name made lowercase.
    userrating = models.TextField(
        db_column="UserRating", blank=True, null=True
    )  # Field name made lowercase.
    dischargeppdefault = models.FloatField(
        db_column="DischargePPDefault", blank=True, null=True
    )  # Field name made lowercase.
    fk_qrev = models.ForeignKey("QrevData", models.DO_NOTHING, db_column="fk_qrev")

    class Meta:
        managed = False
        db_table = "qrev"


class QrevData(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.TextField(blank=True, null=True)
    numberoftransects = models.IntegerField(
        db_column="NumberofTransects", blank=True, null=True
    )  # Field name made lowercase.
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    fk_siteinformation = models.ForeignKey(
        "Siteinformation", models.DO_NOTHING, db_column="fk_siteinformation"
    )

    class Meta:
        managed = False
        db_table = "qrev_data"


class Siteinformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    stationname = models.TextField(
        db_column="StationName", blank=True, null=True
    )  # Field name made lowercase.
    siteid = models.TextField(
        db_column="SiteID", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "siteinformation"


class SlSg(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.DateTimeField(blank=True, null=True)
    velocityx = models.FloatField(blank=True, null=True)
    velocityy = models.FloatField(blank=True, null=True)
    level = models.FloatField(blank=True, null=True)
    stderror1 = models.FloatField(blank=True, null=True)
    stderror2 = models.FloatField(blank=True, null=True)
    stderror3 = models.FloatField(blank=True, null=True)
    snr1 = models.FloatField(blank=True, null=True)
    snr2 = models.FloatField(blank=True, null=True)
    snr3 = models.FloatField(blank=True, null=True)
    signalamp1 = models.IntegerField(blank=True, null=True)
    signalamp2 = models.IntegerField(blank=True, null=True)
    signalamp3 = models.IntegerField(blank=True, null=True)
    noise1 = models.IntegerField(blank=True, null=True)
    noise2 = models.IntegerField(blank=True, null=True)
    noise3 = models.IntegerField(blank=True, null=True)
    icedetection = models.IntegerField(blank=True, null=True)
    heading = models.FloatField(blank=True, null=True)
    pitch = models.FloatField(blank=True, null=True)
    roll = models.FloatField(blank=True, null=True)
    stddevheading = models.FloatField(blank=True, null=True)
    stddevpitch = models.FloatField(blank=True, null=True)
    stddevroll = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)
    stddevpressure = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    cellbegin = models.FloatField(blank=True, null=True)
    cellend = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    direction = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    flow = models.FloatField(blank=True, null=True)
    fk_siteinformation = models.ForeignKey(
        Siteinformation,
        models.DO_NOTHING,
        db_column="fk_siteinformation",
        blank=True,
        null=True,
    )
    file_name = models.TextField(blank=True, null=True)
    linha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sl_sg"
        unique_together = (("data", "fk_siteinformation"),)
