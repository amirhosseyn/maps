# Generated by Django 4.2.4 on 2023-10-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("village", "0003_village_addiction_recovery_camp_available_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="village",
            name="artistic_figures",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="شخصیت\u200cهای هنری"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="canal_water_available",
            field=models.BooleanField(default=False, verbose_name="آب کشاورزی (قنات)"),
        ),
        migrations.AlterField(
            model_name="village",
            name="climate",
            field=models.CharField(
                blank=True,
                default="",
                max_length=100,
                null=True,
                verbose_name="اقلیم آب و هوایی",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="cultural_figures",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="شخصیت\u200cهای فرهنگی"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="development_priorities",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="اولویت های اصلی توسعه"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="historical_tourism_background",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="پیشینه تاریخی و گردشگری",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="investment_opportunities",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="فرصت های اصلی سرمایه گذاری",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="issues_threats",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="مشکلات و تهدیدات اصلی"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="main_needs_solutions",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="راه\u200cحل فراهم کردن نیاز های اصلی",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="main_occupations",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="مشاغل اصلی افراد روستا"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="migration_reason",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="علت مهاجرت"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="opportunities_potentials",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="فرصت ها و پتانسیل های اصلی",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="people_needs_demands",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="خواسته و نیازهای اصلی مردم",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="processed_products_women",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="محصولات تبدیلی روستا (بانوان)",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="raw_products_men",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="محصولات خام روستا (آقایان)",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="religious_figures",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="شخصیت\u200cهای مذهبی"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="scientific_figures",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="شخصیت\u200cهای علمی"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="sports_figures",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="شخصیت\u200cهای ورزشی"
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="well_water_available",
            field=models.BooleanField(default=False, verbose_name="آب کشاورزی (چاه)"),
        ),
        migrations.AlterField(
            model_name="village",
            name="women_needs_demands",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="خواسته و نیازهای اصلی بانوان",
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="youth_needs_demands",
            field=models.TextField(
                blank=True,
                default="",
                null=True,
                verbose_name="خواسته و نیازهای اصلی جوانان",
            ),
        ),
    ]
