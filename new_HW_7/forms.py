from django import forms as f


class AutoForm(f.Form):
    auto_model = f.CharField(max_length=15)
    auto_country = f.CharField(max_length=20)
    auto_year = f.IntegerField()
    auto_number = f.CharField(max_length=10)