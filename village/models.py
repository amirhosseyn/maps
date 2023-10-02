from django.db import models


class Village(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام روستا")
    latitude = models.FloatField(verbose_name="عرض جغرافیایی")
    longitude = models.FloatField(verbose_name="طول جغرافیایی")
    population = models.IntegerField(default=0, verbose_name="جمعیت")
    household_count = models.IntegerField(
        default=0, verbose_name="تعداد خانوار")
    climate = models.CharField(
        default="",blank=True, null=True, max_length=100, verbose_name="اقلیم آب و هوایی")
    employment_percentage = models.FloatField(
        default=0, verbose_name="درصد اشتغال")
    historical_tourism_background = models.TextField(
        default="",blank=True, null=True, verbose_name="پیشینه تاریخی و گردشگری")
    scientific_figures = models.TextField(
        default="",blank=True, null=True, verbose_name="شخصیت‌های علمی")
    cultural_figures = models.TextField(
        default="",blank=True, null=True, verbose_name="شخصیت‌های فرهنگی")
    religious_figures = models.TextField(
        default="",blank=True, null=True, verbose_name="شخصیت‌های مذهبی")
    artistic_figures = models.TextField(
        default="",blank=True, null=True, verbose_name="شخصیت‌های هنری")
    sports_figures = models.TextField(
        default="",blank=True, null=True, verbose_name="شخصیت‌های ورزشی")
    migration_percentage = models.FloatField(
        default=0, verbose_name="درصد مهاجرت")
    migration_reason = models.TextField(default="",blank=True, null=True, verbose_name="علت مهاجرت")
    main_occupations = models.TextField(
        default="",blank=True, null=True, verbose_name="مشاغل اصلی افراد روستا")
    raw_products_men = models.TextField(
        default="",blank=True, null=True, verbose_name="محصولات خام روستا (آقایان)")
    processed_products_women = models.TextField(
        default="",blank=True, null=True, verbose_name="محصولات تبدیلی روستا (بانوان)")
    women_income = models.FloatField(
        default=0, verbose_name="آورده مالی بانوان در روستا")

    drinking_water_available = models.BooleanField(
        default=False, verbose_name="آب آشامیدنی")
    well_water_available = models.BooleanField(
        default=False, verbose_name="آب کشاورزی (چاه)")
    canal_water_available = models.BooleanField(
        default=False, verbose_name="آب کشاورزی (قنات)")
    telephone_available = models.BooleanField(
        default=False, verbose_name="تلفن")
    mobile_antenna_available = models.BooleanField(
        default=False, verbose_name="آنتن موبایل")
    village_council_building_available = models.BooleanField(
        default=False, verbose_name="ساختمان دهیاری و شورا")
    imam_available = models.BooleanField(
        default=False, verbose_name="امام جماعت")
    school_available = models.BooleanField(default=False, verbose_name="مدرسه")
    number_of_students = models.PositiveIntegerField(
        default=0, verbose_name="تعداد دانش‌آموزان")
    post_office_available = models.BooleanField(
        default=False, verbose_name="دفاتر پیشخوان / پست بانک / عابر بانک")
    bank_available = models.BooleanField(
        default=False, verbose_name="دفاتر پیشخوان / پست بانک / عابر بانک")
    addiction_recovery_camp_available = models.BooleanField(
        default=False, verbose_name="کمپ ترک اعتیاد")
    bakery_available = models.BooleanField(
        default=False, verbose_name="نانوایی")
    electricity_available = models.BooleanField(
        default=False, verbose_name="برق")
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
    pathways_available = models.BooleanField(
        default=False, verbose_name="کانال خبری و اطلاع رسانی")
    news_channel_available = models.BooleanField(
        default=False, verbose_name="کانال خبری و اطلاع رسانی")
    park_available = models.BooleanField(default=False, verbose_name="پارک")
    historical_buildings_available = models.BooleanField(
        default=False, verbose_name="ابنیه تاریخی")
    welfare_committee_coverage = models.PositiveIntegerField(
        default=0, verbose_name="درصد تحت پوشش کمیته و بهزیستی نسبت به جمعیت")
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
    proximity_to_city = models.PositiveIntegerField(
        default=0, verbose_name="میزان وابستگی به نزدیکترین شهر")

    opportunities_potentials = models.TextField(
        default="",blank=True, null=True, verbose_name="فرصت ها و پتانسیل های اصلی")
    issues_threats = models.TextField(
        default="",blank=True, null=True, verbose_name="مشکلات و تهدیدات اصلی")
    development_priorities = models.TextField(
        default="",blank=True, null=True, verbose_name="اولویت های اصلی توسعه")
    investment_opportunities = models.TextField(
        default="",blank=True, null=True, verbose_name="فرصت های اصلی سرمایه گذاری")
    people_needs_demands = models.TextField(
        default="",blank=True, null=True, verbose_name="خواسته و نیازهای اصلی مردم")
    women_needs_demands = models.TextField(
        default="",blank=True, null=True, verbose_name="خواسته و نیازهای اصلی بانوان")
    youth_needs_demands = models.TextField(
        default="",blank=True, null=True, verbose_name="خواسته و نیازهای اصلی جوانان")
    main_needs_solutions = models.TextField(
        default="",blank=True, null=True, verbose_name="راه‌حل فراهم کردن نیاز های اصلی")
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self),field.get_internal_type()) for field in self._meta.fields]
