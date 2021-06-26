from django import forms

from cinema_room.models import CinemaRoom


class CinemaRoomAdminForm(forms.ModelForm):
    class Meta:
        model = CinemaRoom
        fields = ('name', 'films', 'seating', 'column', 'row')

    def save(self, commit=True):
        instance = super().save(commit=False)
        column = self.cleaned_data['column']
        row = self.cleaned_data['row']
        instance.seating = self._generate_matrix(column, row)
        instance.save()
        return instance

    def _generate_matrix(self, column, row):
        i = 0
        seating_column = []
        while i < column:
            j = 0
            seating_row = []
            while j < row:
                seating_row.append(False)
                j += 1
            seating_column.append(seating_row)
            i += 1
        return seating_column
