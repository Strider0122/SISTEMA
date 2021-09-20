from django.db import models
import datetime
from dateutil import parser
from django.core.validators import RegexValidator
from seguridadApp.models import Usuario
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import UniqueConstraint
from .validators import validate_file_extension
# Create your models here.
#**********************************VALIDADORES**********************************************************
validador_dni = [
    RegexValidator(regex='^\d{8}$',message='El tamaño tiene que ser de 8 digitos', code='nomatch')
    ]

#**********************************OPCIONES**********************************************************
opciones_genero=[
    ['Femenino','Femenino'],
    ['Masculino','Masculino'],
]

opciones_jurado_asesor_estado=[
    ['Disponible','Disponible'],
    ['Ocupado','Ocupado'],
]

opciones_tipo_asesor=[
    ['Practica','Practica'],
    ['Tesis','Tesis'],
]

opciones_estudiante_estado=[
    ['Estudiante','Estudiante'],
    ['Practicante','Practicante'],
    ['Tesis','Tesis'],
]

opciones_solicitud_estado=[
    ['Pendiente','Pendiente'],
    ['Aceptada','Aceptada'],
    ['Observada','Observada'],
    ['Rechazada','Rechazada'],
]

opciones_tramite_estado=[
    ['Pendiente','Pendiente'],
    ['Aprobado','Aprobado'],
    ['Observada','Observada'],
    ['Desaprobado','Desaprobado'],
]

#**********************************MODELOS ABSTRACTO**********************************************************
# class TimeStampMixin(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     class Meta:
#         abstract = True
#**********************************MODELOS FUERTES**********************************************************
class Escuela(models.Model):
    escuela=models.CharField(max_length=40)
    email=models.EmailField()
    telefono=models.CharField(max_length=15)
    def __str__(self):
        return self.escuela

class Director(models.Model):
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=20)
    apellido_materno=models.CharField(max_length=20)
    dni=models.CharField(max_length=8,unique=True,default="",validators=validador_dni)
    sexo = models.CharField(choices=opciones_genero,max_length=10)
    imagen = models.ImageField(upload_to="secretarias")
    direccion=models.CharField(max_length=30)
    usuario =models.OneToOneField(Usuario, on_delete=models.PROTECT)
    escuela =models.ForeignKey(Escuela, on_delete=models.PROTECT)
    def __str__(self):
        return (self.nombre+" "+self.apellido_paterno+" "+self.apellido_materno)

class Secretaria(models.Model):
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=20)
    apellido_materno=models.CharField(max_length=20)
    dni=models.CharField(max_length=8,unique=True,default="",validators=validador_dni)
    sexo = models.CharField(choices=opciones_genero,max_length=10)
    imagen = models.ImageField(upload_to="secretarias")
    direccion=models.CharField(max_length=30)
    usuario =models.OneToOneField(Usuario, on_delete=models.PROTECT)
    escuela =models.ForeignKey(Escuela, on_delete=models.PROTECT)
    def __str__(self):
        return (self.nombre+" "+self.apellido_paterno+" "+self.apellido_materno)

class Docente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=20)
    apellido_materno=models.CharField(max_length=20)
    dni=models.CharField(max_length=8,unique=True,default="",validators=validador_dni)
    sexo = models.CharField(choices=opciones_genero,max_length=10)
    imagen = models.ImageField(upload_to="docentes")
    direccion=models.CharField(max_length=30)
    usuario =models.OneToOneField(Usuario, on_delete=models.PROTECT)
    escuela =models.ForeignKey(Escuela, on_delete=models.PROTECT)
    def __str__(self):
        return (self.nombre+" "+self.apellido_paterno+" "+self.apellido_materno)
    def es_asesor_practicas_set(self):
        return self.asesor_set.filter(tipo='Practica')
    def es_asesor_tesis_set(self):
        return self.asesor_set.filter(tipo='Tesis')

class Alumno(models.Model):
    nombre=models.CharField(max_length=20)
    apellido_paterno=models.CharField(max_length=20)
    apellido_materno=models.CharField(max_length=20)
    dni=models.CharField(max_length=8,unique=True,default="",validators=validador_dni)
    sexo = models.CharField(choices=opciones_genero,max_length=10)
    imagen = models.ImageField(upload_to="alumnos")
    direccion=models.CharField(max_length=30)
    estado=models.CharField(max_length=30,default="Estudiante",choices=opciones_estudiante_estado,null=True)
    usuario =models.OneToOneField(Usuario, on_delete=models.PROTECT)
    escuela =models.ForeignKey(Escuela, on_delete=models.PROTECT)
    def __str__(self):
        return (self.nombre+" "+self.apellido_paterno+" "+self.apellido_materno)
    def tiene_tramite_inicio_practicas_set(self):
        return TramiteInicioPractica.objects.filter(
            solicitud__id__in = self.solicitud_set.all()
        )
    def tiene_tramite_fin_practicas_set(self):
        return TramiteFinPractica.objects.filter(
            tramiteInicioPractica__id__in= TramiteInicioPractica.objects.filter(
                solicitud__id__in = self.solicitud_set.all()
            )
        )
    def tiene_acta_aprobacion_set(self):
        return ActaAprobacion.objects.filter(
           tramiteFinPractica__id__in = TramiteFinPractica.objects.filter(
                tramiteInicioPractica__id__in= TramiteInicioPractica.objects.filter(
                    solicitud__id__in = self.solicitud_set.all()
                )
            ),
            terminado = True
        )
    def tiene_inscripcion_tesis_set(self):
        return InscripcionTesis.objects.filter(
            solicitud__id__in = self.solicitudtesis_set.all()
        )
    def tiene_sustentacion_tesis_set(self):
        return SustentacionTesis.objects.filter(
           inscripcionTesis__id__in = InscripcionTesis.objects.filter(
                solicitud__id__in = self.solicitudtesis_set.all()
            )
        )
#**********************************MODELOS DEBILES**********************************************************
#**********************************FUNCIONES SECRETARIA**********************************************************
class Jurado(models.Model):
    estado=models.CharField(max_length=30,choices=opciones_jurado_asesor_estado,default="Disponible")
    docente = models.OneToOneField(Docente, on_delete=models.PROTECT)
    def __str__(self):
        return (self.docente.nombre+" "+self.docente.apellido_paterno+" "+self.docente.apellido_materno)

class Asesor(models.Model):
    tipo = models.CharField(max_length=30,choices=opciones_tipo_asesor,default="")
    estado=models.CharField(max_length=30,choices=opciones_jurado_asesor_estado,default="Disponible")
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tipo', 'docente'], name='Tipo Asesor ya asignado')
        ]
    def __str__(self):
        return (self.docente.nombre+" "+self.docente.apellido_paterno+" "+self.docente.apellido_materno)

#**********************************FUNCIONES ALUMNO**********************************************************
class Solicitud(models.Model):
    documento = models.FileField(upload_to='solicitudes_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    enviar=models.BooleanField(default=False)
    observacion = models.TextField(null=True,default="Sin observacion")
    estado=models.CharField(max_length=30,choices=opciones_solicitud_estado,default="Pendiente")
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    def __str__(self):
        return (self.estado)

class TramiteInicioPractica(models.Model):
    voucher = models.FileField(upload_to='vouchers_inicio_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    carta_aceptacion = models.FileField(upload_to='aceptaciones/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    fut_inicio_practicas = models.FileField(upload_to='futs_inicio_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    plan_practicas = models.FileField(upload_to='planes_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    fecha_aceptacion = models.DateField(null=True)
    asesor = models.ForeignKey(Asesor, on_delete=models.PROTECT,null=True,default='')
    enviar=models.BooleanField(default=False)
    estado=models.CharField(max_length=30,choices=opciones_tramite_estado,default="Pendiente")
    solicitud = models.OneToOneField(Solicitud, on_delete=models.PROTECT,default='')
    observacion = models.TextField(null=True,default="Sin observacion")
    def __str__(self):
        return (self.estado)

class TramiteFinPractica(models.Model):
    voucher = models.FileField(upload_to='vouchers_final_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    informe_final_practicas = models.FileField(upload_to='informes_final_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    fut_fin_practicas = models.FileField(upload_to='futs_fin_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    certificado_practicas = models.FileField(upload_to='certificados_practicas/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    estado=models.CharField(max_length=30,choices=opciones_tramite_estado,default="Pendiente")
    tramiteInicioPractica = models.OneToOneField(TramiteInicioPractica, on_delete=models.PROTECT,null=True,default='')
    observacion = models.TextField(null=True,default="Sin observacion")
    enviar=models.BooleanField(default=False)
    def __str__(self):
        return (self.estado)
#**********************************FUNCIONES ASESOR**********************************************************
class ActaAprobacion(models.Model):
    acta_aprobacion = models.FileField(upload_to='actas_aprobacion/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    horas = models.IntegerField(null=True,validators=[MinValueValidator(600)])
    tramiteFinPractica = models.OneToOneField(TramiteFinPractica, on_delete=models.PROTECT,null=True,default='')
    asesor = models.ForeignKey(Asesor, on_delete=models.PROTECT,null=True,default='')
    terminado=models.BooleanField(default=False)
    def __str__(self):
        return (self.horas)

class SolicitudTesis(models.Model):
    documento = models.FileField(upload_to='solicitudes_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    enviar=models.BooleanField(default=False)
    observacion = models.TextField(null=True,default="Sin observacion")
    estado=models.CharField(max_length=30,choices=opciones_solicitud_estado,default="Pendiente")
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    def __str__(self):
        return (self.estado)

class InscripcionTesis(models.Model):
    voucher = models.FileField(upload_to='vouchers_inscripcion_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    fut_inscripcion_tesis = models.FileField(upload_to='futs_inscripcion_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    ejemplar_tesis = models.FileField(upload_to='ejemplares_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    asesor = models.ForeignKey(Asesor, on_delete=models.PROTECT,null=True,default='')
    enviar=models.BooleanField(default=False)
    estado=models.CharField(max_length=30,choices=opciones_tramite_estado,default="Pendiente")
    solicitud = models.OneToOneField(SolicitudTesis, on_delete=models.PROTECT,default='')
    observacion = models.TextField(null=True,default="Sin observacion")
    def __str__(self):
        return (self.estado)

class SustentacionTesis(models.Model):
    voucher = models.FileField(upload_to='vouchers_sustentacion_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    fut_sustentacion_tesis = models.FileField(upload_to='futs_sustentacion_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    resumen_tesis = models.FileField(upload_to='resumenes_tesis/%Y/%m/%d/',default=None, validators=[validate_file_extension])
    enlace = models.CharField(max_length=50,null=True)
    fecha_sustentacion = models.DateField(null=True)
    inscripcionTesis = models.OneToOneField(InscripcionTesis, on_delete=models.PROTECT,default='')
    hora = models.TimeField(auto_now=False, auto_now_add=False,null=True)
    jurados = models.ManyToManyField(Jurado, through='TesisJurado',default='')
    enviar=models.BooleanField(default=False)
    observacion = models.TextField(null=True,default="Sin observacion")
    asignada=models.BooleanField(default=False)
    estado = models.CharField(max_length=30,choices=opciones_tramite_estado,default="Pendiente")
    nota = models.IntegerField(null=True,validators=[MinValueValidator(0), MaxValueValidator(20)])
    def __str__(self):
        return (self.estado)
    def dias_restantes(self):
        resultado =   self.fecha_sustentacion - datetime.date.today()
        return resultado.days

class TesisJurado(models.Model):
    sustentacionTesis = models.ForeignKey(SustentacionTesis, on_delete=models.CASCADE)
    jurado = models.ForeignKey(Jurado, on_delete=models.CASCADE)
    nota = models.IntegerField(null=True,validators=[MinValueValidator(0), MaxValueValidator(20)])
    evaluada=models.BooleanField(default=False)
    def __str__(self):
        return (self.nota)
