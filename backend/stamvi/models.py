from django.db import models


class SetIndexVeldf(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    data = models.DateField()
    vazao = models.DecimalField(max_digits=20, decimal_places=3)
    velocityx = models.DecimalField(max_digits=20, decimal_places=3)
    level = models.DecimalField(max_digits=20, decimal_places=3)
    mean_q_over_a = models.DecimalField(
        max_digits=20, decimal_places=3, db_column="MeanQoverA"
    )  # Renaming the field to match the column name
    mean_area = models.DecimalField(
        max_digits=20, decimal_places=3, db_column="MeanArea"
    )  # Renaming the field to match the column name

    class Meta:
        managed = False  # To prevent Django from trying to manage this table
        db_table = "setindexveldf"  # Specify the name of your materialized view

    def __str__(self):
        return self.id
