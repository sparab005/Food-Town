from django import forms
from .models import TopRestaurant ,menus1,food

class TopRestaurantAdminForm(forms.ModelForm):
    class Meta:
        model = TopRestaurant
        fields = '__all__'

    def clean_variety(self):
        variety = self.cleaned_data['variety']
        # Pad the value with spaces to reach the maximum length (32 characters)
        return variety.ljust(32)


class CustomTopRestaurantChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name 


# class McDonaldsAdminForm(forms.ModelForm):
#     class Meta:
#         model = McDonalds
#         fields = '__all__'

#     resid = CustomTopRestaurantChoiceField(
#         queryset=TopRestaurant.objects.all(),
#         empty_label=None,  # To hide the empty label
#         required=False,  # To make it non-required
#     )

# class menufilterAdminForm(forms.ModelForm):
#     class Meta:
#         model = menufilter
#         fields = '__all__'

#     resid = CustomTopRestaurantChoiceField(
#         queryset=TopRestaurant.objects.all(),
#         empty_label=None,  # To hide the empty label
#         required=False,  # To make it non-required
#     )
#     menuid= CustomTopRestaurantChoiceField(
#         queryset=menus1.objects.all(),
#         empty_label=None,  # To hide the empty label
#         required=False,  # To make it non-required
#     )


# class DominoPizzaAdminForm(forms.ModelForm):
#     class Meta:
#         model = DominoPizza
#         fields = '__all__'

#     resid = CustomTopRestaurantChoiceField(
#         queryset=TopRestaurant.objects.all(),
#         empty_label=None,  # To hide the empty label
#         required=False,  # To make it non-required
#     )

# class SubwayAdminForm(forms.ModelForm):
#     class Meta:
#         model = Subway
#         fields = '__all__'

#     resid = CustomTopRestaurantChoiceField(
#         queryset=TopRestaurant.objects.all(),
#         empty_label=None,  # To hide the empty label
#         required=False,  # To make it non-required
#     )

# class Belgian_WaffleAdminForm(forms.ModelForm):
#     class Meta:
#         model = Belgian_Waffle
#         fields = '__all__'

#     resid = CustomTopRestaurantChoiceField(
#         queryset=TopRestaurant.objects.all(),
#         empty_label=None,  # To hide the empty label
#         required=False,  # To make it non-required
#     )

class FoodMenuAdminForm(forms.ModelForm):
    class Meta:
        model = food
        fields = '__all__'

   
    menuid= CustomTopRestaurantChoiceField(
        queryset=menus1.objects.all(),
        empty_label=None,  # To hide the empty label
        required=False,  # To make it non-required
    )
