# book_orders/forms.py

from django import forms
from .models import BookOrder, Book, Class

class BookOrderForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = BookOrder
        fields = ['name', 'phone', 'selected_class', 'books', 'total_amount']

    def __init__(self, *args, **kwargs):
        super(BookOrderForm, self).__init__(*args, **kwargs)
        self.fields['selected_class'].queryset = Class.objects.all()

        if 'selected_class' in self.data:
            try:
                selected_class_id = int(self.data.get('selected_class'))
                self.fields['books'].queryset = Book.objects.filter(available_classes__id=selected_class_id)
            except (ValueError, TypeError):
                self.fields['books'].queryset = Book.objects.none()
        elif self.instance.pk:
            self.fields['books'].queryset = self.instance.selected_class.book_set
