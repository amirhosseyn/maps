from django.db import models


class Village(models.Model):
    # Group : General Information
    name = models.CharField(max_length=255, verbose_name="نام روستا")
    latitude = models.FloatField(verbose_name="عرض جغرافیایی")
    longitude = models.FloatField(verbose_name="طول جغرافیایی")
    population = models.IntegerField(default=0, verbose_name="جمعیت")
    employment_percentage = models.FloatField(
        default=0, verbose_name="درصد اشتغال")
    historical_tourism_background = models.TextField(
        default="", blank=True, null=True, verbose_name="پیشینه تاریخی و گردشگری")
    scientific_figures = models.TextField(
        default="", blank=True, null=True, verbose_name="شخصیت‌های علمی,فرهنگی,مذهبی,هنری,ورزشی")
    migration_reason = models.TextField(
        default="", blank=True, null=True, verbose_name=" درصد و علت مهاجرت ")
    main_occupations = models.TextField(
        default="", blank=True, null=True, verbose_name="مشاغل اصلی افراد روستا")
    raw_products_men = models.TextField(
        default="", blank=True, null=True, verbose_name="محصولات روستا (آقایان)")
    processed_products_women = models.TextField(
        default="", blank=True, null=True, verbose_name="محصولات تبدیلی روستا (بانوان)")
    production_workshop = models.TextField(
        max_length=255, default="", blank=True, null=True, verbose_name=" کارگاههای تولیدی کشاورزی و مدیران آنها")
    brand = models.CharField(
        max_length=255, default="", blank=True, null=True, verbose_name="برند روستا")
    welfare_committee_coverage = models.PositiveIntegerField(
        default=0, verbose_name="درصد تحت پوشش کمیته و بهزیستی نسبت به جمعیت")

    # Group: Infrastructure of the village
    drinking_water_available = models.BooleanField(
        default=False, verbose_name="آب آشامیدنی")
    well_water_available = models.BooleanField(
        default=False, verbose_name="آب کشاورزی")
    telephone_available = models.BooleanField(
        default=False, verbose_name="تلفن")
    mobile_antenna_available = models.BooleanField(
        default=False, verbose_name="آنتن موبایل")
    village_council_building_available = models.BooleanField(
        default=False, verbose_name="ساختمان دهیاری و شورا")
    school_available = models.BooleanField(default=False, verbose_name="مدرسه")
    post_office_available = models.BooleanField(
        default=False, verbose_name="دفاتر پیشخوان / پست بانک / عابر بانک")
    bank_available = models.BooleanField(
        default=False, verbose_name="بانک")
    addiction_recovery_camp_available = models.BooleanField(
        default=False, verbose_name="کمپ ترک اعتیاد")
    bakery_available = models.BooleanField(
        default=False, verbose_name="نانوایی")
    electricity_available = models.BooleanField(
        default=False, verbose_name="برق ( تکفاز/ سه فاز)")
    gas_available = models.BooleanField(default=False, verbose_name="گاز")
    television_antenna_available = models.BooleanField(
        default=False, verbose_name="آنتن تلویزیون")
    internet_available = models.BooleanField(
        default=False, verbose_name="اینترنت")
    village_head_available = models.BooleanField(
        default=False, verbose_name="دهیار")
    basij_sister_available = models.BooleanField(
        default=False, verbose_name="پایگاه بسیج (خواهران)")
    basij_brother_available = models.BooleanField(
        default=False, verbose_name="پایگاه بسیج (برادران)")
    mosque_available = models.BooleanField(
        default=False, verbose_name="مسجد و حسینیه")
    police_available = models.BooleanField(default=False, verbose_name="پلیس")
    sports_hall_available = models.BooleanField(
        default=False, verbose_name="سالن ورزشی / باشگاه")
    teacher_house_available = models.BooleanField(
        default=False, verbose_name="خانه معلم")
    road_available = models.BooleanField(
        default=False, verbose_name="جاده و راه ارتباطی")
    asphalt_available = models.BooleanField(
        default=False, verbose_name="آسفالت، مسیر و معابر")
    news_channel_available = models.BooleanField(
        default=False, verbose_name="کانال خبری و اطلاع رسانی")
    park_available = models.BooleanField(default=False, verbose_name="پارک")
    historical_buildings_available = models.BooleanField(
        default=False, verbose_name="ابنیه تاریخی")
    shop_available = models.BooleanField(default=False, verbose_name="فروشگاه")
    production_workshop_available = models.BooleanField(
        default=False, verbose_name="کارگاه تولیدی و کشاورزی")
    beautification_plan_available = models.BooleanField(
        default=False, verbose_name="طرح هادی و زیبا سازی روستا")
    fuel_station_available = models.BooleanField(
        default=False, verbose_name="جایگاه سوخت")
    transportation_services_available = models.BooleanField(
        default=False, verbose_name="سرویس ایاب ذهاب")
    ecotourism_infrastructure_available = models.BooleanField(
        default=False, verbose_name="بوم گردی و زیرساخت گردشگری")
    doctor_available = models.BooleanField(default=False, verbose_name="پزشک")
    nurse_available = models.BooleanField(default=False, verbose_name="بهیار")
    health_center_available = models.BooleanField(
        default=False, verbose_name="مرکز بهداشت / خانه بهداشت / درمانگاه / بیمارستان")
    youth_involvement = models.BooleanField(
        default=False, verbose_name="از جوانان در مدیریت استفاده شده است؟")
    women_involvement = models.BooleanField(
        default=False, verbose_name="از بانوان در مدیریت استفاده شده است؟")

    # Group: Other
    opportunities_potentials = models.TextField(
        default="", blank=True, null=True, verbose_name="فرصت ها و پتانسیل های اصلی")
    issues_threats = models.TextField(
        default="", blank=True, null=True, verbose_name="مشکلات و تهدیدات اصلی")
    development_priorities = models.TextField(
        default="", blank=True, null=True, verbose_name="اولویت های اصلی توسعه")
    investment_opportunities = models.TextField(
        default="", blank=True, null=True, verbose_name="فرصت های اصلی سرمایه گذاری")
    people_needs_demands = models.TextField(
        default="", blank=True, null=True, verbose_name="خواسته و نیازهای اصلی مردم")
    main_needs_solutions = models.TextField(
        default="", blank=True, null=True, verbose_name="راه‌حل فراهم کردن نیاز های اصلی")
    proposed_entrepreneurship_plan = models.TextField(
        default="", null=True, blank=True, verbose_name="طرح کارآفرینی  پیشنهادی برای روستا")
    unfinished_projects = models.TextField(
        default="", null=True, blank=True, verbose_name="پروژه های نیمه تمام")
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self),field.get_internal_type()) for field in self._meta.fields]
