from django.db import models

# Create your models here.


class Source(models.Model):
    """The source of the resources."""

    SourceName = models.CharField(
        max_length=25, help_text="The name of the Source.")

    def __str__(self):
        return self.SourceName


class Category(models.Model):
    """The category of a resource."""

    CategoryName = models.CharField(
        max_length=30, help_text="The name of the Category.")

    def __str__(self):
        return self.CategoryName


class Resource(models.Model):
    """A resource that members can use."""

    ResourceName = models.CharField(
        max_length=75, help_text="The name of the Resource.")
    SourceName = models.ForeignKey(Source, on_delete=models.CASCADE)
    CategoryName = models.ForeignKey(Category, on_delete=models.CASCADE)
    Link = models.URLField(help_text="The Resource's website.")
    DateUploaded = models.DateField(
        null=True, help_text="The date that the Resource was uploaded."
    )

    def __str__(self):
        return f"{self.ResourceName} ({self.SourceName}) Category: {self.CategoryName}, Link: {self.Link}"


class ResourceRequest(models.Model):
    """A resource that members have requested to add to the approved resources."""

    Resource_Name = models.CharField(
        max_length=100, help_text="The name of the Resource requested.")
    Source_Name = models.CharField(
        max_length=100, help_text="The source of the Resource requested.")
    Link = models.URLField(help_text="The requested Resource's website.")

    def __str__(self):
        return f"{self.ReqResourceName} ({self.ReqSourceName}) Link: {self.ReqLink}"


class CustomerData(models.Model):
    """Monthly Time Series Data for Free vs Premium Members."""

    Year = models.IntegerField(help_text="Year")
    Month = models.CharField(max_length=10, help_text="Month")
    Free = models.IntegerField(help_text="Number of Free Members")
    Premium = models.IntegerField(help_text="Number of Premium Members")

    def __str__(self):
        return f"{self.Month} {self.Year}"


class Survey(models.Model):
    """Survey for Free Members."""

    Q1 = models.BooleanField(
        default=False, help_text="True or False (Check if true): You and your employees can successfully spot a phishing email.")
    Q2 = models.IntegerField(
        help_text="0 to 4: How many of the following does your business have? Strong passwords, Antivirus Software, Automatic Software Updates, and Backup(s) in place for data storage")
    Q3 = models.CharField(
        max_length=3, help_text="Yes or No: Does your business/organization have a cyber security plan and a ransomware plan?")


class SurveyData(models.Model):
    """Data from the Survey for Free Members plus additional data."""

    Q1Data = models.BooleanField(default=False, help_text="Response to Q1")
    Q2Data = models.IntegerField(help_text="Response to Q2")
    Q3Data = models.CharField(max_length=3, help_text="Response to Q3")
    NumEmployees = models.IntegerField(
        help_text="Number of people employed at the business/organization")
    AcctAge = models.IntegerField(help_text="Age of the account in months")
    City = models.CharField(
        max_length=75, help_text="City where the business/organization is located")
    State = models.CharField(
        max_length=2, help_text="Abbreviation of the State where the business/organization is located")
    Free = models.IntegerField(
        help_text="1 for free account, 0 if not free account")
    Premium = models.IntegerField(
        help_text="1 for premium account, 0 if not premium account")
    NewSignUp = models.IntegerField(
        help_text="1 if the business/organization signed up for premium after the survey, 0 if not")
