# Generated by Django 4.1.5 on 2023-03-09 02:46

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Antibiotic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("initial_date", models.CharField(max_length=100)),
                ("antibiotic", models.CharField(max_length=100)),
                ("loading_dose", models.IntegerField()),
                ("maintenance_dose", models.IntegerField()),
                ("route", models.CharField(max_length=100)),
                ("frequency", models.IntegerField()),
                ("duration", models.IntegerField()),
                ("end_date", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="AntibioticSensitivity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "antibiotic",
                    models.CharField(
                        choices=[
                            ("Ampicillin", "Ampicillin"),
                            ("Amoxicillin/Clavulanic", "Amoxicillin/Clavulanic"),
                            ("Gentamicin", "Gentamicin"),
                            ("Co-trimoxazole", "Co-trimoxazole"),
                            ("Ciprofloxacin", "Ciprofloxacin"),
                            ("Cloxacillin", "Cloxacillin"),
                            ("Cefixime", "Cefixime"),
                            ("Tetracycline", "Tetracycline"),
                            ("Levofloxacin", "Levofloxacin"),
                            ("Doxycycline", "Doxycycline"),
                            ("Norfloxacin", "Norfloxacin"),
                            ("Penicillin", "Penicillin"),
                            ("Erythromycin", "Erythromycin"),
                            ("Linezolid", "Linezolid"),
                            ("Vancomycin", "Vancomycin"),
                            ("Imipenem", "Imipenem"),
                            ("Moxifloxacin", "Moxifloxacin"),
                            ("Ceftriaxone", "Ceftriaxone"),
                        ],
                        default="Select",
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClinicalSign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.CharField(max_length=100)),
                ("procalcitonin", models.CharField(max_length=100)),
                ("white_blood_cell", models.CharField(max_length=100)),
                ("neutrophil", models.CharField(max_length=100)),
                ("s_creatinine", models.CharField(max_length=100)),
                ("cratinine_clearance", models.CharField(max_length=100)),
                ("temperature", models.CharField(max_length=100)),
                ("blood_pressure", models.CharField(max_length=100)),
                ("o2_saturation", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Compliance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("serum_creatinine", models.IntegerField(default=None)),
                ("isAppropriate", models.BooleanField(default=False)),
                ("isRightDocumentation", models.BooleanField(default=False)),
                ("isRecommendationFiled", models.BooleanField(default=True)),
                ("isAntibioticChanged", models.BooleanField(default=False)),
                ("isComplance", models.BooleanField(default=False)),
                ("isDuration", models.BooleanField(default=False)),
                ("isAntibiotisDoseChanged", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="CultureReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_sent", models.CharField(max_length=100)),
                ("time_reported", models.CharField(max_length=100)),
                ("sentBeforeAntibiotic", models.BooleanField(default=False)),
                (
                    "specimen_type",
                    models.CharField(
                        choices=[
                            ("blood", "blood"),
                            ("urine", "urine"),
                            ("sputum", "sputum"),
                            ("CSF", "CSF"),
                            ("Wound", "Wound"),
                            ("Pus", "Pus"),
                            ("Bal", "Bal"),
                            ("Stool", "Stool"),
                            ("Mini Bal", "Mini Bal"),
                            ("Aseptic Fluid", "Aseptic Fluid"),
                            ("Pleural Fluid", "Pleural Fluid"),
                            ("TISSUE", "TISSUE"),
                        ],
                        default="",
                        max_length=100,
                    ),
                ),
                ("site_of_collection", models.CharField(max_length=100)),
                ("organism", models.CharField(max_length=100)),
                (
                    "multi_drug_resistant",
                    models.CharField(
                        choices=[
                            ("MDR", "MDR"),
                            ("Non MDR", "Non MDR"),
                            ("PS(Pan sensitive)", "PS(Pan sensitive)"),
                            ("NA(No organism)", "NA(No organism)"),
                        ],
                        default="",
                        max_length=100,
                    ),
                ),
                (
                    "resistance",
                    models.CharField(
                        choices=[
                            (
                                "CRE( Carbapenemase resistant enterobactereciae)",
                                "CRE( Carbapenemase resistant enterobactereciae)",
                            ),
                            (
                                "ESBL(Extended spectrum beta lactamase)",
                                "ESBL(Extended spectrum beta lactamase)",
                            ),
                            (
                                "MRSA(Methicillin resistant staphylococcus aureus)",
                                "MRSA(Methicillin resistant staphylococcus aureus)",
                            ),
                            (
                                "VRE(Vancomycin resistant enterococcus)",
                                "VRE(Vancomycin resistant enterococcus)",
                            ),
                            (
                                "CRAB( Carbapenem resistant acinetobacter baumannii)",
                                "CRAB( Carbapenem resistant acinetobacter baumannii)",
                            ),
                            (
                                "Col Re( Colistin resistant)",
                                "Col Re( Colistin resistant)",
                            ),
                            ("NA-None of the above", "NA-None of the above"),
                        ],
                        default="",
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DrugAdministeredReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isRightDocumentation", models.BooleanField(default=False)),
                ("isRightDrug", models.BooleanField(default=False)),
                ("isRightDose", models.BooleanField(default=False)),
                ("isRightRoute", models.BooleanField(default=False)),
                ("isRightFrequency", models.BooleanField(default=False)),
                ("isRightDuration", models.BooleanField(default=False)),
                ("isRightIndication", models.BooleanField(default=False)),
                ("isAppropriate", models.BooleanField(default=False)),
                ("score", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="FocusOfInfection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isUTI", models.BooleanField(default=False)),
                ("isCNS", models.BooleanField(default=False)),
                ("isPneumonia", models.BooleanField(default=False)),
                ("isSkin", models.BooleanField(default=False)),
                ("isAbdominal", models.BooleanField(default=False)),
                ("isPrimaryBacteraemia", models.BooleanField(default=False)),
                ("isSecondaryBacteraemia", models.BooleanField(default=False)),
                ("isCatheterLinesStents", models.BooleanField(default=False)),
                ("other", models.CharField(default="", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Imaging",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isxRay", models.BooleanField(default=False)),
                ("isUltraSound", models.BooleanField(default=False)),
                ("isCTScan", models.BooleanField(default=False)),
                ("isMRI", models.BooleanField(default=False)),
                ("isPETScan", models.BooleanField(default=False)),
                ("impression", models.CharField(default="", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "fullName",
                    models.CharField(max_length=100, verbose_name="Full Name"),
                ),
                ("dateOfBirth", models.CharField(default=None, max_length=100)),
                ("mrdNumber", models.CharField(max_length=100)),
                ("dateofAdmission", models.CharField(max_length=100)),
                (
                    "patientLocation",
                    models.CharField(
                        choices=[("ICU", "ICU"), ("WARD", "WARD"), ("NONE", "NONE")],
                        default="",
                        max_length=100,
                    ),
                ),
                ("department", models.CharField(max_length=100)),
                ("admittingDoctor", models.CharField(max_length=100)),
                ("diagnostic", models.CharField(max_length=100)),
                ("cormorbodities", models.CharField(max_length=100)),
                ("height", models.CharField(blank=True, max_length=100)),
                ("weight", models.CharField(blank=True, max_length=100)),
                (
                    "lastReviewDate",
                    models.DateField(blank=True, default=None, null=True),
                ),
                (
                    "lastAnalysisDate",
                    models.DateField(blank=True, default=None, null=True),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="PatientOutcome",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lenght_of_stay", models.IntegerField()),
                ("date_of_discharge", models.CharField(max_length=100)),
                (
                    "outcome",
                    models.CharField(
                        choices=[("DEAD", "DEAD"), ("ALIVE", "ALIVE")],
                        default="Select",
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recommendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("indication", models.CharField(default=None, max_length=100)),
                ("drug", models.CharField(default=None, max_length=100)),
                ("dose", models.CharField(default=None, max_length=100)),
                ("frequency", models.CharField(default=None, max_length=100)),
                ("duration", models.CharField(default=None, max_length=100)),
                ("deEscalation", models.CharField(default=None, max_length=100)),
                ("isindication", models.BooleanField()),
                ("isdrug", models.BooleanField(default=False)),
                ("isdose", models.BooleanField(default=False)),
                ("isfrequency", models.BooleanField(default=False)),
                ("isduration", models.BooleanField(default=False)),
                ("isdeEscalation", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Sepsis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isSepsis", models.BooleanField(default=False)),
                ("isSepticShock", models.BooleanField(default=False)),
                ("isNeutropenicSepsis", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="PatientForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isAnalyzed", models.BooleanField(default=False)),
                ("review_date", models.CharField(max_length=100)),
                ("review_department", models.CharField(max_length=100)),
                ("provisional_diagnosis", models.CharField(max_length=200)),
                ("final_diagnosis", models.CharField(max_length=200)),
                ("syndromic_diagnosis", models.CharField(max_length=200)),
                (
                    "diagnosis_choice",
                    models.CharField(
                        choices=[
                            ("probable", "probable"),
                            ("definite", "definite"),
                            ("NONE", "NONE"),
                        ],
                        default="null",
                        max_length=100,
                    ),
                ),
                ("isculture_report", models.BooleanField()),
                (
                    "antibiotic_used",
                    models.ManyToManyField(
                        blank=True, default=[], to="stewardship.antibiotic"
                    ),
                ),
                (
                    "clinical_signs",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.clinicalsign",
                    ),
                ),
                (
                    "culture_report",
                    models.ManyToManyField(
                        blank=True, default=[], to="stewardship.culturereport"
                    ),
                ),
                (
                    "focus_of_infection",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.focusofinfection",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.patient",
                    ),
                ),
                (
                    "sepsis",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.sepsis",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="culturereport",
            name="Imaging",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stewardship.imaging",
            ),
        ),
        migrations.AddField(
            model_name="culturereport",
            name="antibiotic_sensitivity",
            field=models.ManyToManyField(
                blank=True, default=[], to="stewardship.antibioticsensitivity"
            ),
        ),
        migrations.AddField(
            model_name="clinicalsign",
            name="patientId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="stewardship.patient"
            ),
        ),
        migrations.CreateModel(
            name="AnalysisForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("doctor", models.CharField(default=None, max_length=100)),
                (
                    "compliance",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.compliance",
                    ),
                ),
                (
                    "drugAdministered",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.drugadministeredreview",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.patient",
                    ),
                ),
                (
                    "patientForm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.patientform",
                    ),
                ),
                (
                    "patientOutcome",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.patientoutcome",
                    ),
                ),
                (
                    "recommendation",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stewardship.recommendation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("isStaff", models.BooleanField(default=False)),
                ("isAdmin", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
