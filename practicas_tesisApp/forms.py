from django.db.models import fields
from django.forms import widgets
from .models import (
    Escuela,Secretaria,Alumno,Docente,Jurado,Director,Asesor,Solicitud,TramiteInicioPractica,
    TramiteFinPractica,ActaAprobacion,SolicitudTesis,InscripcionTesis,SustentacionTesis,
    TesisJurado
    )
from django import forms

class EscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        exclude = ('usuario',)

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = '__all__'
        exclude = ('usuario',)

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        exclude = ('usuario','escuela',)

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        exclude = ('usuario','estado',)

class JuradoForm(forms.ModelForm):
    docente = forms.ModelChoiceField(queryset=Docente.objects.all(),widget=forms.Select(attrs={'class':'selectpicker'}))
    class Meta:
        model = Jurado
        fields = '__all__'

class AsesorForm(forms.ModelForm):
    docente = forms.ModelChoiceField(queryset=Docente.objects.all(),widget=forms.Select(attrs={'class':'selectpicker'}))
    class Meta:
        model = Asesor
        fields = '__all__'

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        exclude = ('observacion','alumno')
        widgets = {'estado': forms.HiddenInput()}

class SolicitudFormEvaluar(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        exclude = ('alumno','documento','enviar')

class TramiteInicioPracticaForm(forms.ModelForm):
    asesor = forms.ModelChoiceField(queryset=Asesor.objects.all(),widget=forms.Select(attrs={'class':'selectpicker'}))
    class Meta:
        model = TramiteInicioPractica
        fields = '__all__'
        exclude = ('solicitud','observacion',)
        widgets = {
            'fecha_aceptacion':forms.TextInput(attrs={'type': 'date','class': 'datetimepicker-input'}),   #CAMBIAR FORMATO DE IMPUT DE FECHA
            'estado': forms.HiddenInput()
        }

class TramiteInicioPracticaFormEvaluar(forms.ModelForm):
    class Meta:
        model = TramiteInicioPractica
        fields = '__all__'
        exclude = ('solicitud','enviar','asesor','voucher','carta_aceptacion','plan_practicas','fut_inicio_practicas')
        widgets = {
            'fecha_aceptacion':forms.TextInput(attrs={'type': 'date','readonly':'readonly','class': 'form-control  datetimepicker-input'})    #CAMBIAR FORMATO DE IMPUT DE FECHA
        }

class TramiteFinPracticaForm(forms.ModelForm):
    class Meta:
        model = TramiteFinPractica
        fields = '__all__'
        exclude = ('tramiteInicioPractica','observacion')
        widgets = {'estado': forms.HiddenInput()}

class TramiteFinPracticaFormEvaluar(forms.ModelForm):
    class Meta:
        model = TramiteFinPractica
        fields = '__all__'
        exclude = ('tramiteInicioPractica','enviar','voucher','informe_final_practicas','fut_fin_practicas','certificado_practicas')

class ActaAprobacionForm(forms.ModelForm):
    class Meta:
        model = ActaAprobacion
        fields = '__all__'
        exclude = ('tramiteFinPractica','asesor')

class SolicitudTesisForm(forms.ModelForm):
    class Meta:
        model = SolicitudTesis
        fields = '__all__'
        exclude = ('observacion','alumno')
        widgets = {'estado': forms.HiddenInput()}

class SolicitudTesisFormEvaluar(forms.ModelForm):
    class Meta:
        model = SolicitudTesis
        fields = '__all__'
        exclude = ('alumno','documento','enviar')

class InscripcionTesisForm(forms.ModelForm):
    asesor = forms.ModelChoiceField(queryset=Asesor.objects.all(),widget=forms.Select(attrs={'class':'selectpicker'}))
    class Meta:
        model = InscripcionTesis
        fields = '__all__'
        exclude = ('solicitud','observacion','asignada',)
        widgets = {
            'estado': forms.HiddenInput()
        }

class InscripcionTesisFormEvaluar(forms.ModelForm):
    class Meta:
        model = InscripcionTesis
        fields = '__all__'
        exclude = ('solicitud','enviar','asesor','voucher','fut_inscripcion_tesis','ejemplar_tesis','asignada',)

class SustentacionTesisForm(forms.ModelForm):
    
    class Meta:
        model = SustentacionTesis
        fields = '__all__'
        exclude = ('observacion','hora','enlace','inscripcionTesis','jurados','fecha_sustentacion','nota',)
        widgets = {
            'fecha_sustentacion':forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker-input'}),   #CAMBIAR FORMATO DE IMPUT DE FECHA
            'estado': forms.HiddenInput(),
            'asignada': forms.HiddenInput(),
            'hora':forms.TimeInput(attrs={'type': 'text','class': 'form-control  datetimepicker-input'}),
        }

class SustentacionTesisFormAsignar(forms.ModelForm):
    # jurados = forms.ModelChoiceField(queryset=Jurado.objects.all(),widget=forms.Select(attrs={'class':'selectpicker selectmultiple ','multiple':'multiple'}))
    class Meta:
        model = SustentacionTesis
        fields = '__all__'
        exclude = ('inscripcionTesis','observacion','enviar','estado','voucher','fut_sustentacion_tesis','resumen_tesis','nota')
        widgets = {
            'fecha_sustentacion':forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker-input'}),   #CAMBIAR FORMATO DE IMPUT DE FECHA
            'hora':forms.TextInput(attrs={'type': 'time','class': 'form-control  datetimepicker-input'}),
        }

class TesisJuradoForm(forms.ModelForm):
    class Meta:
        model = TesisJurado
        fields = '__all__'
        exclude = ('sustentacionTesis','jurado',)