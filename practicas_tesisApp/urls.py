from django.urls import path
from .views import (
    listarEscuela,agregarEscuela,editarEscuela,eliminarEscuela,
    listarSecretaria,agregarSecretaria,editarSecretaria,eliminarSecretaria,
    listarAlumno,agregarAlumno,editarAlumno,eliminarAlumno,
    listarDocente,agregarDocente,editarDocente,eliminarDocente,
    listarJurado,agregarJurado,editarJurado,eliminarJurado,
    listarDirector,agregarDirector,editarDirector,eliminarDirector,
    listarAsesor,agregarAsesor,editarAsesor,eliminarAsesor,
    listarSolicitud,agregarSolicitud,editarSolicitud,eliminarSolicitud,listarSolicitudEvaluar,editarSolicitudEvaluar,
    listarTramiteInicioPractica,editarTramiteInicioPractica,listarTramiteInicioPracticaEvaluar,editarTramiteInicioPracticaEvaluar,
    listarTramiteFinPractica,editarTramiteFinPractica,listarTramiteFinPracticaEvaluar,editarTramiteFinPracticaEvaluar,
    listarActaAprobacion,editarActaAprobacion,
    listarSolicitudTesis,agregarSolicitudTesis,editarSolicitudTesis,eliminarSolicitudTesis,listarSolicitudTesisEvaluar,editarSolicitudTesisEvaluar,
    listarInscripcionTesis,editarInscripcionTesis,listarInscripcionTesisEvaluar,editarInscripcionTesisEvaluar,
    listarSustentacionTesis,editarSustentacionTesis,listarSustentacionTesisAsignar,editarSustentacionTesisAsignar,listarSustentacionTesisEvaluar,editarSustentacionTesisEvaluar
    )

urlpatterns = [
    #**********************************ESCUELA**********************************************************
    path('listarEscuela/',listarEscuela,name="listarEscuela"),
    path('agregarEscuela/',agregarEscuela,name="agregarEscuela"),
    path('editarEscuela/<id>/',editarEscuela,name="editarEscuela"),
    path('eliminarEscuela/<id>/',eliminarEscuela,name="eliminarEscuela"),
    #**********************************DIRECTOR**********************************************************
    path('listarDirector/',listarDirector,name="listarDirector"),
    path('agregarDirector/',agregarDirector,name="agregarDirector"),
    path('editarDirector/<id>/',editarDirector,name="editarDirector"),
    path('eliminarDirector/<id>/',eliminarDirector,name="eliminarDirector"),
    #**********************************SECRETARIA**********************************************************
    path('listarSecretaria/',listarSecretaria,name="listarSecretaria"),
    path('agregarSecretaria/',agregarSecretaria,name="agregarSecretaria"),
    path('editarSecretaria/<id>/',editarSecretaria,name="editarSecretaria"),
    path('eliminarSecretaria/<id>/',eliminarSecretaria,name="eliminarSecretaria"),
    #**********************************ALUMNO**********************************************************
    path('listarAlumno/',listarAlumno,name="listarAlumno"),
    path('agregarAlumno/',agregarAlumno,name="agregarAlumno"),
    path('editarAlumno/<id>/',editarAlumno,name="editarAlumno"),
    path('eliminarAlumno/<id>/',eliminarAlumno,name="eliminarAlumno"),
    #**********************************ALUMNO**********************************************************
    path('listarDocente/',listarDocente,name="listarDocente"),
    path('agregarDocente/',agregarDocente,name="agregarDocente"),
    path('editarDocente/<id>/',editarDocente,name="editarDocente"),
    path('eliminarDocente/<id>/',eliminarDocente,name="eliminarDocente"),
    #**********************************JURADO**********************************************************
    path('listarJurado/',listarJurado,name="listarJurado"),
    path('agregarJurado/',agregarJurado,name="agregarJurado"),
    path('editarJurado/<id>/',editarJurado,name="editarJurado"),
    path('eliminarJurado/<id>/',eliminarJurado,name="eliminarJurado"),
    #**********************************ASESOR**********************************************************
    path('listarAsesor/',listarAsesor,name="listarAsesor"),
    path('agregarAsesor/',agregarAsesor,name="agregarAsesor"),
    path('editarAsesor/<id>/',editarAsesor,name="editarAsesor"),
    path('eliminarAsesor/<id>/',eliminarAsesor,name="eliminarAsesor"),
    #**********************************SOLICITUD**********************************************************
    path('listarSolicitud/',listarSolicitud,name="listarSolicitud"),
    path('agregarSolicitud/',agregarSolicitud,name="agregarSolicitud"),
    path('editarSolicitud/<id>/',editarSolicitud,name="editarSolicitud"),
    path('eliminarSolicitud/<id>/',eliminarSolicitud,name="eliminarSolicitud"),
    #**********************************SOLICITUD EVALUAR**********************************************************
    path('listarSolicitudEvaluar/',listarSolicitudEvaluar,name="listarSolicitudEvaluar"),
    path('editarSolicitudEvaluar/<id>/',editarSolicitudEvaluar,name="editarSolicitudEvaluar"),
    #**********************************TRAMITE INICIO PRACTICAS**********************************************************
    path('listarTramiteInicioPractica/',listarTramiteInicioPractica,name="listarTramiteInicioPractica"),
    path('editarTramiteInicioPractica/<id>/',editarTramiteInicioPractica,name="editarTramiteInicioPractica"),
    # path('eliminarTramiteInicioPractica/<id>/',eliminarTramiteInicioPractica,name="eliminarTramiteInicioPractica"),
    #**********************************TRAMITE INICIO PRACTICAS EVALUAR**********************************************************
    path('listarTramiteInicioPracticaEvaluar/',listarTramiteInicioPracticaEvaluar,name="listarTramiteInicioPracticaEvaluar"),
    path('editarTramiteInicioPracticaEvaluar/<id>/',editarTramiteInicioPracticaEvaluar,name="editarTramiteInicioPracticaEvaluar"),
    #**********************************TRAMITE FIN PRACTICAS**********************************************************
    path('listarTramiteFinPractica/',listarTramiteFinPractica,name="listarTramiteFinPractica"),
    path('editarTramiteFinPractica/<id>/',editarTramiteFinPractica,name="editarTramiteFinPractica"),
    # path('eliminarTramiteFinPractica/<id>/',eliminarTramiteFinPractica,name="eliminarTramiteFinPractica"),
    #**********************************TRAMITE FIN PRACTICAS EVALUAR**********************************************************
    path('listarTramiteFinPracticaEvaluar/',listarTramiteFinPracticaEvaluar,name="listarTramiteFinPracticaEvaluar"),
    path('editarTramiteFinPracticaEvaluar/<id>/',editarTramiteFinPracticaEvaluar,name="editarTramiteFinPracticaEvaluar"),
     #**********************************ACTA APROBACION**********************************************************
    path('listarActaAprobacion/',listarActaAprobacion,name="listarActaAprobacion"),
    path('editarActaAprobacion/<id>/',editarActaAprobacion,name="editarActaAprobacion"),
     #**********************************SOLICITUD TESIS**********************************************************
    path('listarSolicitudTesis/',listarSolicitudTesis,name="listarSolicitudTesis"),
    path('agregarSolicitudTesis/',agregarSolicitudTesis,name="agregarSolicitudTesis"),
    path('editarSolicitudTesis/<id>/',editarSolicitudTesis,name="editarSolicitudTesis"),
    path('eliminarSolicitudTesis/<id>/',eliminarSolicitudTesis,name="eliminarSolicitudTesis"),
    #**********************************SOLICITUD TESIS EVALUAR**********************************************************
    path('listarSolicitudTesisEvaluar/',listarSolicitudTesisEvaluar,name="listarSolicitudTesisEvaluar"),
    path('editarSolicitudTesisEvaluar/<id>/',editarSolicitudTesisEvaluar,name="editarSolicitudTesisEvaluar"),
    #**********************************INSCRIPCION TESIS**********************************************************
    path('listarInscripcionTesis/',listarInscripcionTesis,name="listarInscripcionTesis"),
    path('editarInscripcionTesis/<id>/',editarInscripcionTesis,name="editarInscripcionTesis"),
    # path('eliminarInscripcionTesis/<id>/',eliminarInscripcionTesis,name="eliminarInscripcionTesis"),
    #**********************************INSCRIPCION TESIS EVALUAR**********************************************************
    path('listarInscripcionTesisEvaluar/',listarInscripcionTesisEvaluar,name="listarInscripcionTesisEvaluar"),
    path('editarInscripcionTesisEvaluar/<id>/',editarInscripcionTesisEvaluar,name="editarInscripcionTesisEvaluar"),
    #**********************************SUSTENTAR TESIS**********************************************************
    path('listarSustentacionTesis/',listarSustentacionTesis,name="listarSustentacionTesis"),
    path('editarSustentacionTesis/<id>/',editarSustentacionTesis,name="editarSustentacionTesis"),
    # path('eliminarSustentacionTesis/<id>/',eliminarSustentacionTesis,name="eliminarSustentacionTesis"),
    #**********************************SUSTENTAR TESIS ASIGNAR**********************************************************
    path('listarSustentacionTesisAsignar/',listarSustentacionTesisAsignar,name="listarSustentacionTesisAsignar"),
    path('editarSustentacionTesisAsignar/<id>/',editarSustentacionTesisAsignar,name="editarSustentacionTesisAsignar"),
    #**********************************SUSTENTAR TESIS EVALUAR**********************************************************
    path('listarSustentacionTesisEvaluar/',listarSustentacionTesisEvaluar,name="listarSustentacionTesisEvaluar"),
    path('editarSustentacionTesisEvaluar/<id>/',editarSustentacionTesisEvaluar,name="editarSustentacionTesisEvaluar"),
]