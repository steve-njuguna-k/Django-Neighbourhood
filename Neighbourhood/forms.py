
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .models import NeighbourHood, Profile

COUNTIES = [
    ('Choose County', ('Choose County')), 
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CATEGORIES = [
    ('1', 'Crimes and Safety'),
    ('2', 'Health Emergency'),
    ('3', 'Recommendations'),
    ('4', 'Fire Breakouts'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
]

class CustomSelectWidget(forms.Select):
    def create_option(self, name, value, *args, **kwargs):
        option = super().create_option(name, value, *args, **kwargs)
        if value:
            instance = self.choices.queryset.get(pk=value)  # get instance
            option['attrs']['custom_attr'] = instance.field_name  # set option attribute

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'dropify', 'data-height':420, 'data-max-file-size':"1M"}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Keep it short, preferably in one concise sentence'}))
    national_id = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'National ID'}))
    neighbourhood = forms.ChoiceField(label=u'Select Your Neighbourhood', required=False, widget=forms.Select(attrs={'class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]
    
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'national_id', 'neighbourhood']

class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'Old Password',}))
    new_password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'New Password',}))
    new_password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'Confirm Password',}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)

def clean_old_password(self):
    old_password = self.cleaned_data["old_password"]
    if not self.user.check_password(old_password):
        raise forms.ValidationError(
            self.error_messages['password_incorrect'],
            code='password_incorrect',
        )
    return old_password

class AddBussinessForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Business Name','class': 'form-control mb-4'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Business Description','class': 'form-control mb-4','rows': 5,}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Business Email','class': 'form-control mb-4'}))
    neighbourhood = forms.ChoiceField(required=True, widget=forms.Select(attrs={'placeholder': 'Neighbourhood','class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(AddBussinessForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]

class AddNeighbourhoodForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title','class': 'form-control mb-4'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location','class': 'form-control mb-4'}))
    county = forms.ChoiceField(widget=forms.Select( attrs={'class': 'form-control mb-4'}), choices=COUNTIES)
    neighbourhood_logo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'dropify', 'data-height':300, 'data-max-file-size':"1M"}))

    class Meta:
        model = NeighbourHood
        fields = ('title','location','county','neighbourhood_logo')

class AddPostForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Post Title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Description'}))
    category = forms.ChoiceField(choices=CATEGORIES, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'placeholder':'Select Category'}))
    neighbourhood = forms.ChoiceField(label=u'Select Your Neighbourhood', required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]