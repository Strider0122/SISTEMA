from django.shortcuts import render,redirect
import datetime
from dateutil import parser
from seguridadApp.models import Usuario
from .models import (
    Escuela,Secretaria,Alumno,Docente,Jurado,Director,Asesor,Solicitud,TramiteInicioPractica,
    TramiteFinPractica,TramiteFinPractica,ActaAprobacion,SolicitudTesis,InscripcionTesis,
    SustentacionTesis,TesisJurado
    )
from .forms import (
    EscuelaForm,SecretariaForm,AlumnoForm,DocenteForm,JuradoForm,DirectorForm,AsesorForm,SolicitudForm,
    SolicitudFormEvaluar,TramiteInicioPracticaForm,TramiteInicioPracticaFormEvaluar,
    TramiteFinPracticaForm,TramiteFinPracticaFormEvaluar,ActaAprobacionForm,SolicitudTesisForm,
    SolicitudTesisFormEvaluar,InscripcionTesisForm,InscripcionTesisFormEvaluar,SustentacionTesisForm,
    SustentacionTesisFormAsignar,TesisJuradoForm
    )
from django.db.models import Q
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.
#**********************************ESCUELA**********************************************************
@login_required(login_url="login")
def listarEscuela(request):
    queryset = request.GET.get("buscar")
    escuelas=Escuela.objects.all()
    page = request.GET.get("page",1)
    if queryset:
        escuelas=Escuela.objects.filter(
            Q(escuela__icontains=queryset)
        ).distinct()
    try:
        paginator = Paginator(escuelas,5)
        escuelas = paginator.page(page)
    except:
        raise Http404
    context={'entity':escuelas, 'paginator':paginator}
    return render(request,"escuela/listar.html",context)

@login_required(login_url="login")
def agregarEscuela(request):
    if request.method=="POST":
        form=EscuelaForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Escuela Guardada Correctamente")
            return redirect("listarEscuela")
    else:
        form=EscuelaForm()
    context={'form':form}
    return render(request,"escuela/agregar.html",context)

@login_required(login_url="login")
def editarEscuela(request,id):
    escuela=Escuela.objects.get(id=id)
    if request.method=="POST":
        form=EscuelaForm(request.POST,instance=escuela)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Escuela Actualizada Correctamente")
            return redirect("listarEscuela")
    else:
        form=EscuelaForm(instance=escuela)
    context={"form":form}
    return render(request,"escuela/editar.html",context)

@login_required(login_url="login")
def eliminarEscuela(request,id):
    escuela=Escuela.objects.get(id=id)
    escuela.delete()
    messages.success(request,"Escuela Eliminada")
    return redirect(to="listarEscuela")

#**********************************DIRECTOR**********************************************************
@login_required(login_url="login")
def listarDirector(request):
    queryset = request.GET.get("buscar")
    directores=Director.objects.all()
    page = request.GET.get("page",1)
    if queryset:
        directores=Director.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(apellido_paterno__icontains=queryset) |
            Q(apellido_materno__icontains=queryset)
        ).distinct()
    try:
        paginator = Paginator(directores,5)
        directores = paginator.page(page)
    except:
        raise Http404
    context={'entity':directores, 'paginator':paginator}
    return render(request,"director/listar.html",context)

@login_required(login_url="login")
def agregarDirector(request):
    if request.method=="POST":
        form=DirectorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                nombre_usuario = form.cleaned_data.get('nombre') +" "+ form.cleaned_data.get('apellido_paterno') +" "+ form.cleaned_data.get('apellido_materno')
                contraseña = form.cleaned_data.get('dni')
                tipo_usuario = "director"
                usuario = Usuario(username = nombre_usuario, tipo=tipo_usuario)
                usuario.set_password(contraseña)
                usuario.save()
                director = form.save(commit=False)
                director.usuario = usuario
                director.save()
            except:
                 raise Http404
            messages.success(request,"Director Guardado Correctamente")
            return redirect("listarDirector")

    else:
        form=DirectorForm()
    context={'form':form}
    return render(request,"director/agregar.html",context)

@login_required(login_url="login")
def editarDirector(request,id):
    director=Director.objects.get(id=id)
    if request.method=="POST":
        form=DirectorForm(request.POST,instance=director, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Director Actualizada Correctamente")
            return redirect("listarDirector")
    else:
        form=DirectorForm(instance=director)
    context={"form":form}
    return render(request,"director/editar.html",context)

@login_required(login_url="login")
def eliminarDirector(request,id):
    director=Director.objects.get(id=id)
    director.delete()
    messages.success(request,"Director Eliminada")
    return redirect(to="listarDirector")
#**********************************SECRETARIA**********************************************************
@login_required(login_url="login")
def listarSecretaria(request):
    queryset = request.GET.get("buscar")
    secretarias=Secretaria.objects.all()
    page = request.GET.get("page",1)
    if queryset:
        secretarias=Secretaria.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(apellido_paterno__icontains=queryset) |
            Q(apellido_materno__icontains=queryset)
        ).distinct()
    try:
        paginator = Paginator(secretarias,5)
        secretarias = paginator.page(page)
    except:
        raise Http404
    context={'entity':secretarias, 'paginator':paginator}
    return render(request,"secretaria/listar.html",context)

@login_required(login_url="login")
def agregarSecretaria(request):
    if request.method=="POST":
        form=SecretariaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                nombre_usuario = form.cleaned_data.get('nombre') +" "+ form.cleaned_data.get('apellido_paterno') +" "+ form.cleaned_data.get('apellido_materno')
                contraseña = form.cleaned_data.get('dni')
                tipo_usuario = "secretaria"
                usuario = Usuario(username = nombre_usuario, tipo=tipo_usuario)
                usuario.set_password(contraseña)
                usuario.save()
                secretaria = form.save(commit=False)
                secretaria.usuario = usuario
                secretaria.save()
            except:
                 raise Http404
            messages.success(request,"Secretaria Guardada Correctamente")
            return redirect("listarSecretaria")

    else:
        form=SecretariaForm()
    context={'form':form}
    return render(request,"secretaria/agregar.html",context)

@login_required(login_url="login")
def editarSecretaria(request,id):
    secretaria=Secretaria.objects.get(id=id)
    if request.method=="POST":
        form=SecretariaForm(request.POST,instance=secretaria, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Secretaria Actualizada Correctamente")
            return redirect("listarSecretaria")
    else:
        form=SecretariaForm(instance=secretaria)
    context={"form":form}
    return render(request,"secretaria/editar.html",context)

@login_required(login_url="login")
def eliminarSecretaria(request,id):
    secretaria=Secretaria.objects.get(id=id)
    secretaria.delete()
    messages.success(request,"Secretaria Eliminada")
    return redirect(to="listarSecretaria")
#**********************************ALUMNO**********************************************************
@login_required(login_url="login")
def listarAlumno(request):
    queryset = request.GET.get("buscar")
    alumnos=Alumno.objects.all()
    page = request.GET.get("page",1)
    if queryset:
        alumnos=Alumno.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(apellido_paterno__icontains=queryset) |
            Q(apellido_materno__icontains=queryset)
        ).distinct()
    try:
        paginator = Paginator(alumnos,5)
        alumnos = paginator.page(page)
    except:
        raise Http404
    context={'entity':alumnos, 'paginator':paginator}
    return render(request,"alumno/listar.html",context)

@login_required(login_url="login")
def agregarAlumno(request):
    if request.method=="POST":
        form=AlumnoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                nombre_usuario = form.cleaned_data.get('nombre') +" "+ form.cleaned_data.get('apellido_paterno') +" "+ form.cleaned_data.get('apellido_materno')
                contraseña = form.cleaned_data.get('dni')
                tipo_usuario = "alumno"
                usuario = Usuario(username = nombre_usuario, tipo=tipo_usuario)
                usuario.set_password(contraseña)
                usuario.save()
                alumno = form.save(commit=False)
                alumno.usuario = usuario
                alumno.save()
            except:
                 raise Http404
            messages.success(request,"Alumno Guardado Correctamente")
            return redirect("listarAlumno")

    else:
        form=AlumnoForm()
    context={'form':form}
    return render(request,"alumno/agregar.html",context)

@login_required(login_url="login")
def editarAlumno(request,id):
    alumno=Alumno.objects.get(id=id)
    if request.method=="POST":
        form=AlumnoForm(request.POST,instance=alumno, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Alumno Actualizado Correctamente")
            return redirect("listarAlumno")
    else:
        form=AlumnoForm(instance=alumno)
    context={"form":form}
    return render(request,"alumno/editar.html",context)

@login_required(login_url="login")
def eliminarAlumno(request,id):
    alumno=Alumno.objects.get(id=id)
    alumno.delete()
    messages.success(request,"Alumno Eliminado")
    return redirect(to="listarAlumno")

#**********************************DOCENTE**********************************************************

@login_required(login_url="login")
def listarDocente(request):
    queryset = request.GET.get("buscar")
    docentes=Docente.objects.filter(
        escuela= request.user.secretaria.escuela
    )
    page = request.GET.get("page",1)
    if queryset:
        docentes=Docente.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(apellido_paterno__icontains=queryset) |
            Q(apellido_materno__icontains=queryset)
        ).filter(
            escuela= request.user.secretaria.escuela
        ).distinct()
    try:
        paginator = Paginator(docentes,5)
        docentes = paginator.page(page)
    except:
        raise Http404
    context={'entity':docentes, 'paginator':paginator}
    return render(request,"docente/listar.html",context)

@login_required(login_url="login")
def agregarDocente(request):
    if request.method=="POST":
        form=DocenteForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                nombre_usuario = form.cleaned_data.get('nombre') +" "+ form.cleaned_data.get('apellido_paterno') +" "+ form.cleaned_data.get('apellido_materno')
                contraseña = form.cleaned_data.get('dni')
                tipo_usuario = "docente"
                usuario = Usuario(username = nombre_usuario, tipo=tipo_usuario)
                usuario.set_password(contraseña)
                usuario.save()
                docente = form.save(commit=False)
                docente.usuario = usuario
                docente.escuela = request.user.secretaria.escuela
                docente.save()
            except:
                 raise Http404
            messages.success(request,"Docente Guardado Correctamente")
            return redirect("listarDocente")

    else:
        form=DocenteForm()
    context={'form':form}
    return render(request,"docente/agregar.html",context)

@login_required(login_url="login")
def editarDocente(request,id):
    docente=Docente.objects.get(id=id)
    if request.method=="POST":
        form=DocenteForm(request.POST,instance=docente, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Docente Actualizado Correctamente")
            return redirect("listarDocente")
    else:
        form=DocenteForm(instance=docente)
    context={"form":form}
    return render(request,"docente/editar.html",context)

@login_required(login_url="login")
def eliminarDocente(request,id):
    docente=Docente.objects.get(id=id)
    docente.delete()
    messages.success(request,"Docente Eliminado")
    return redirect(to="listarDocente")

#**********************************JURADO**********************************************************

@login_required(login_url="login")
def listarJurado(request):
    queryset = request.GET.get("buscar")
    jurados=Jurado.objects.filter(
        docente__id__in = Docente.objects.filter(
            escuela = request.user.secretaria.escuela
        )
    )
    page = request.GET.get("page",1)
    if queryset:
        jurados=Jurado.objects.filter( 
            docente__id__in = Docente.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
            ).filter(
            escuela= request.user.secretaria.escuela
            )
        ).distinct()
    try:
        paginator = Paginator(jurados,5)
        jurados = paginator.page(page)
    except:
        raise Http404
    context={'entity':jurados, 'paginator':paginator}
    return render(request,"jurado/listar.html",context)

@login_required(login_url="login")
def agregarJurado(request):
    if request.method=="POST":
        form=JuradoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Jurado Guardado Correctamente")
            return redirect("listarJurado")

    else:
        form=JuradoForm()
        docentes = Docente.objects.filter(
            escuela = request.user.secretaria.escuela
        )
        form.fields['docente'].queryset = docentes
    context={'form':form}
    return render(request,"jurado/agregar.html",context)

@login_required(login_url="login")
def editarJurado(request,id):
    jurado=Jurado.objects.get(id=id)
    if request.method=="POST":
        form=JuradoForm(request.POST,instance=jurado, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Jurado Actualizado Correctamente")
            return redirect("listarJurado")
    else:
        form=JuradoForm(instance=jurado)
        docentes = Docente.objects.filter(
            escuela = request.user.secretaria.escuela
        )
        form.fields['docente'].queryset = docentes
    context={"form":form}
    return render(request,"jurado/editar.html",context)

@login_required(login_url="login")
def eliminarJurado(request,id):
    jurado=Jurado.objects.get(id=id)
    jurado.delete()
    messages.success(request,"Jurado Eliminado")
    return redirect(to="listarJurado")
#**********************************ASESOR**********************************************************

@login_required(login_url="login")
def listarAsesor(request):
    queryset = request.GET.get("buscar")
    asesores=Asesor.objects.filter(
         docente__id__in = Docente.objects.filter(
            escuela = request.user.secretaria.escuela
        )
    )
    page = request.GET.get("page",1)
    if queryset:
        asesores=Asesor.objects.filter( 
            docente__id__in = Docente.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
            ).filter(
            escuela= request.user.secretaria.escuela
            )
        ).distinct()
    try:
        paginator = Paginator(asesores,5)
        asesores = paginator.page(page)
    except:
        raise Http404
    context={'entity':asesores, 'paginator':paginator}
    return render(request,"asesor/listar.html",context)

@login_required(login_url="login")
def agregarAsesor(request):
    if request.method=="POST":
        form=AsesorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Asesor Guardado Correctamente")
            return redirect("listarAsesor")
    else:
        form=AsesorForm()
        docentes = Docente.objects.filter(
            escuela = request.user.secretaria.escuela
        )
        form.fields['docente'].queryset = docentes
    context={'form':form}
    return render(request,"asesor/agregar.html",context)

@login_required(login_url="login")
def editarAsesor(request,id):
    asesor=Asesor.objects.get(id=id)
    if request.method=="POST":
        form=AsesorForm(request.POST,instance=asesor, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Asesor Actualizado Correctamente")
            return redirect("listarAsesor")
    else:
        form=AsesorForm(instance=asesor)
        docentes = Docente.objects.filter(
            escuela = request.user.secretaria.escuela
        )
        form.fields['docente'].queryset = docentes
        print('IMPRESION: '+str(form))
    context={"form":form}
    return render(request,"asesor/editar.html",context)

@login_required(login_url="login")
def eliminarAsesor(request,id):
    asesor=Asesor.objects.get(id=id)
    asesor.delete()
    messages.success(request,"Asesor Eliminado")
    return redirect(to="listarAsesor")

#**********************************SOLICITUD**********************************************************

@login_required(login_url="login")
def listarSolicitud(request):
    queryset = request.GET.get("buscar")
    solicitudes=Solicitud.objects.filter(alumno = request.user.alumno)
    page = request.GET.get("page",1)
    if queryset:
        solicitudes=Solicitud.objects.filter( 
            alumno__id__in = Alumno.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
            )
        ).distinct()
    try:
        paginator = Paginator(solicitudes,5)
        solicitudes = paginator.page(page)
    except:
        raise Http404
    context={'entity':solicitudes, 'paginator':paginator}
    return render(request,"solicitud/listar.html",context)

@login_required(login_url="login")
def agregarSolicitud(request):
    if request.method=="POST":
        form=SolicitudForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.alumno = request.user.alumno
            solicitud.save()
            messages.success(request,"Solicitud Guardado Correctamente")
            return redirect("listarSolicitud")

    else:
        form=SolicitudForm()
    context={'form':form}
    return render(request,"solicitud/agregar.html",context)

@login_required(login_url="login")
def editarSolicitud(request,id):
    solicitud=Solicitud.objects.get(id=id)
    if request.method=="POST":
        form=SolicitudForm(request.POST,instance=solicitud, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Solicitud Actualizado Correctamente")
            return redirect("listarSolicitud")
    else:
        form=SolicitudForm(instance=solicitud)
    context={"form":form}
    return render(request,"solicitud/editar.html",context)

@login_required(login_url="login")
def eliminarSolicitud(request,id):
    solicitud=Solicitud.objects.get(id=id)
    solicitud.delete()
    messages.success(request,"Solicitud Eliminado")
    return redirect(to="listarSolicitud")

#**********************************SOLICITUD EVALUAR**********************************************************
@login_required(login_url="login")
def listarSolicitudEvaluar(request):
    queryset = request.GET.get("buscar")
    solicitudes=Solicitud.objects.filter(
        alumno__id__in = Alumno.objects.filter(
            escuela__id__in= Escuela.objects.filter(
                escuela= request.user.director.escuela.escuela
            )
        ),
        enviar = True
    )
    page = request.GET.get("page",1)
    if queryset:
        solicitudes=Solicitud.objects.filter(
            alumno__id__in = Alumno.objects.filter(
                escuela__id__in= Escuela.objects.filter(
                    escuela= request.user.director.escuela.escuela
                )  
            ).filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
            ),
        enviar = True
        ).distinct()
    try:
        paginator = Paginator(solicitudes,5)
        solicitudes = paginator.page(page)
    except:
        raise Http404
    context={'entity':solicitudes, 'paginator':paginator}
    return render(request,"solicitud/evaluar/listar.html",context)

@login_required(login_url="login")
def editarSolicitudEvaluar(request,id):
    solicitud=Solicitud.objects.get(id=id)
    if request.method=="POST":
        form=SolicitudFormEvaluar(request.POST,instance=solicitud, files=request.FILES)
        if form.is_valid(): 
            form.save()
            if solicitud.estado == 'Aceptada':
                tramite_inicio_practicas = TramiteInicioPractica(solicitud=solicitud)
                tramite_inicio_practicas.save()
                print('IMPRESION: '+ str(tramite_inicio_practicas.solicitud)+ str(tramite_inicio_practicas.fecha_aceptacion))
            messages.success(request,"Solicitud Actualizado Correctamente")
            return redirect("listarSolicitudEvaluar")
    else:
        form=SolicitudFormEvaluar(instance=solicitud)
    context={"form":form, 'solicitud':solicitud}
    return render(request,"solicitud/evaluar/editar.html",context)

#**********************************TRAMITE INICIO PRACTICAS**********************************************************

@login_required(login_url="login")
def listarTramiteInicioPractica(request):
    queryset = request.GET.get("buscar")
    tramites_inicio_practicas=TramiteInicioPractica.objects.filter(
        solicitud__id__in = Solicitud.objects.filter(
            alumno=request.user.alumno.id
            )
        )
    page = request.GET.get("page",1)
    if queryset:
        tramites_inicio_practicas=TramiteInicioPractica.objects.filter( 
            solicitud__id__in = Solicitud.objects.filter(alumno=request.user.alumno.id),
            asesor__id__in = Asesor.objects.filter(
                docente__id__in = Docente.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
                )
            )
        ).distinct()
    try:
        paginator = Paginator(tramites_inicio_practicas,5)
        tramites_inicio_practicas = paginator.page(page)
    except:
        raise Http404
    context={'entity':tramites_inicio_practicas, 'paginator':paginator}
    return render(request,"tramite_inicio/listar.html",context)

@login_required(login_url="login")
def editarTramiteInicioPractica(request,id):
    tramite_inicio_practicas=TramiteInicioPractica.objects.get(id=id)
    asesores = Asesor.objects.filter(
            docente__id__in = Docente.objects.filter(
                escuela = request.user.alumno.escuela
            ),
            tipo = 'Practica'
        )
    if request.method=="POST":
        if datetime.datetime.today() > parser.parse(request.POST.get('fecha_aceptacion')):
            form=TramiteInicioPracticaForm(request.POST,instance=tramite_inicio_practicas, files=request.FILES)
            if form.is_valid(): 
                form.save()
                messages.success(request,"Tramite Inicio Practica Actualizado Correctamente")
                return redirect("listarTramiteInicioPractica")
        else:
            messages.error(request,"LA FECHA DE ACEPTACION ES PASADO")
            form=TramiteInicioPracticaForm(instance=tramite_inicio_practicas)
            form.fields['asesor'].queryset = asesores
    else:
        form=TramiteInicioPracticaForm(instance=tramite_inicio_practicas)
        form.fields['asesor'].queryset = asesores
    context={"form":form}
    return render(request,"tramite_inicio/editar.html",context)

# @login_required(login_url="login")
# def eliminarTramite(request,id):
#     tramite=Tramite.objects.get(id=id)
#     tramite.delete()
#     messages.success(request,"Tramite Eliminado")
#     return redirect(to="listarTramite")

#**********************************TRAMITE INICIO PRACTICAS EVALUAR**********************************************************
@login_required(login_url="login")
def listarTramiteInicioPracticaEvaluar(request):
    queryset = request.GET.get("buscar")
    tramites_inicio_practicas=TramiteInicioPractica.objects.filter(
        asesor__id__in = Asesor.objects.filter(
            docente=request.user.docente.id
        ),
        enviar=True
    )
    page = request.GET.get("page",1)
    if queryset:
        tramites_inicio_practicas=TramiteInicioPractica.objects.filter( 
            asesor__id__in = Asesor.objects.filter(
                docente=request.user.docente.id
            ),
            solicitud__id__in = Solicitud.objects.filter(
                alumno__id__in = Alumno.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
                )
            ),
            enviar=True
        ).distinct()
    try:
        paginator = Paginator(tramites_inicio_practicas,5)
        tramites_inicio_practicas = paginator.page(page)
    except:
        raise Http404
    context={'entity':tramites_inicio_practicas, 'paginator':paginator}
    return render(request,"tramite_inicio/evaluar/listar.html",context)

@login_required(login_url="login")
def editarTramiteInicioPracticaEvaluar(request,id):
    tramite_inicio_practicas=TramiteInicioPractica.objects.get(id=id)
    if request.method=="POST":
        form=TramiteInicioPracticaFormEvaluar(request.POST,instance=tramite_inicio_practicas, files=request.FILES)
        if form.is_valid(): 
            form.save()
            if tramite_inicio_practicas.estado == "Aprobado" :
                tramite_fin_practicas = TramiteFinPractica(tramiteInicioPractica=tramite_inicio_practicas)
                tramite_fin_practicas.save()
                print('IMPRESION: '+ str(tramite_fin_practicas.tramiteInicioPractica))
            messages.success(request,"Tramite Inicio Practica Actualizado Correctamente")
            return redirect("listarTramiteInicioPracticaEvaluar")
    else:
        form=TramiteInicioPracticaFormEvaluar(instance=tramite_inicio_practicas)
    context={"form":form, 'tramite':tramite_inicio_practicas}
    return render(request,"tramite_inicio/evaluar/editar.html",context)

#**********************************TRAMITE FIN PRACTICAS**********************************************************

@login_required(login_url="login")
def listarTramiteFinPractica(request):
    queryset = request.GET.get("buscar")
    tramites_fin_practicas=TramiteFinPractica.objects.filter(
        tramiteInicioPractica__id__in=TramiteInicioPractica.objects.filter( 
        solicitud__id__in = Solicitud.objects.filter(alumno=request.user.alumno.id)
        ))
    page = request.GET.get("page",1)
    if queryset:
        tramites_fin_practicas=TramiteFinPractica.objects.filter( 
            tramiteInicioPractica__id__in=TramiteInicioPractica.objects.filter( 
                solicitud__id__in = Solicitud.objects.filter(alumno=request.user.alumno.id),
                asesor__id__in = Asesor.objects.filter(
                    docente__id__in = Docente.objects.filter(
                    Q(nombre__icontains=queryset) |
                    Q(apellido_paterno__icontains=queryset) |
                    Q(apellido_materno__icontains=queryset)
                ))
            )
        ).distinct()
    try:
        paginator = Paginator(tramites_fin_practicas,5)
        tramites_fin_practicas = paginator.page(page)
    except:
        raise Http404
    context={'entity':tramites_fin_practicas, 'paginator':paginator}
    return render(request,"tramite_fin/listar.html",context)

@login_required(login_url="login")
def editarTramiteFinPractica(request,id):
    tramite_fin_practicas=TramiteFinPractica.objects.get(id=id)
    if request.method=="POST":
        form=TramiteFinPracticaForm(request.POST,instance=tramite_fin_practicas, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Tramite Fin Practica Actualizado Correctamente")
            return redirect("listarTramiteFinPractica")
    else:
        form=TramiteFinPracticaForm(instance=tramite_fin_practicas)
    context={"form":form}
    return render(request,"tramite_fin/editar.html",context)

# @login_required(login_url="login")
# def eliminarTramite(request,id):
#     tramite=Tramite.objects.get(id=id)
#     tramite.delete()
#     messages.success(request,"Tramite Eliminado")
#     return redirect(to="listarTramite")

#**********************************TRAMITE FIN PRACTICAS EVALUAR**********************************************************
@login_required(login_url="login")
def listarTramiteFinPracticaEvaluar(request):
    queryset = request.GET.get("buscar")
    tramites_fin_practicas=TramiteFinPractica.objects.filter(
        tramiteInicioPractica__id__in=TramiteInicioPractica.objects.filter(
            asesor__id__in = Asesor.objects.filter(
                docente=request.user.docente.id
            ),
            estado ='Aprobado'
        ),
        enviar = True
    )
    page = request.GET.get("page",1)
    if queryset:
        tramites_fin_practicas=TramiteFinPractica.objects.filter( 
            tramiteInicioPractica__id__in=TramiteInicioPractica.objects.filter(
                asesor__id__in = Asesor.objects.filter(docente=request.user.docente.id),
                solicitud__id__in = Solicitud.objects.filter(
                    alumno__id__in = Alumno.objects.filter(
                    Q(nombre__icontains=queryset) |
                    Q(apellido_paterno__icontains=queryset) |
                    Q(apellido_materno__icontains=queryset)
                )),
                estado ='Aprobado'
            ),
            enviar = True
        ).distinct()
    try:
        paginator = Paginator(tramites_fin_practicas,5)
        tramites_fin_practicas = paginator.page(page)
    except:
        raise Http404
    context={'entity':tramites_fin_practicas, 'paginator':paginator}
    return render(request,"tramite_fin/evaluar/listar.html",context)

@login_required(login_url="login")
def editarTramiteFinPracticaEvaluar(request,id):
    tramite_fin_practicas=TramiteFinPractica.objects.get(id=id)
    if request.method=="POST":
        form=TramiteFinPracticaFormEvaluar(request.POST,instance=tramite_fin_practicas, files=request.FILES)
        if form.is_valid(): 
            form.save()
            if tramite_fin_practicas.estado == "Aprobado" :
                acta_aprobacion = ActaAprobacion(tramiteFinPractica=tramite_fin_practicas,asesor= tramite_fin_practicas.tramiteInicioPractica.asesor)
                acta_aprobacion.save()
            messages.success(request,"Tramite Fin Practica Actualizado Correctamente")
            return redirect("listarTramiteFinPracticaEvaluar")
    else:
        form=TramiteFinPracticaFormEvaluar(instance=tramite_fin_practicas)
    context={"form":form, 'tramite':tramite_fin_practicas}
    return render(request,"tramite_fin/evaluar/editar.html",context)

#**********************************ACTA APROBACION**********************************************************

@login_required(login_url="login")
def listarActaAprobacion(request):
    queryset = request.GET.get("buscar")
    actas_aprobacion=ActaAprobacion.objects.filter(
    asesor__id__in = Asesor.objects.filter(
            docente=request.user.docente,
            tipo='Practica'
    ))
    page = request.GET.get("page",1)
    if queryset:
        actas_aprobacion=ActaAprobacion.objects.filter( 
            tramiteFinPractica__id__in = TramiteFinPractica.objects.filter(
                tramiteInicioPractica__id__in = TramiteInicioPractica.objects.filter(
                    solicitud__id__in = Solicitud.objects.filter(
                        alumno__id__in = Alumno.objects.filter(
                            Q(nombre__icontains=queryset) |
                            Q(apellido_paterno__icontains=queryset) |
                            Q(apellido_materno__icontains=queryset)
                        )
                    )
                )
            )
        ).distinct()
    try:
        paginator = Paginator(actas_aprobacion,5)
        actas_aprobacion = paginator.page(page)
    except:
        raise Http404
    context={'entity':actas_aprobacion, 'paginator':paginator}
    return render(request,"acta_aprobacion/listar.html",context)

# @login_required(login_url="login")
# def agregarSolicitud(request):
#     if request.method=="POST":
#         form=SolicitudForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             solicitud = form.save(commit=False)
#             solicitud.alumno = request.user.alumno
#             solicitud.save()
#             messages.success(request,"Solicitud Guardado Correctamente")
#             return redirect("listarSolicitud")

#     else:
#         form=SolicitudForm()
#     context={'form':form}
#     return render(request,"solicitud/agregar.html",context)

@login_required(login_url="login")
def editarActaAprobacion(request,id):
    acta_aprobacion=ActaAprobacion.objects.get(id=id)
    if request.method=="POST":
        form=ActaAprobacionForm(request.POST,instance=acta_aprobacion, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Acta Aprobacion Actualizado Correctamente")
            return redirect("listarActaAprobacion")
    else:
        form=ActaAprobacionForm(instance=acta_aprobacion)
    context={"form":form , "tramite":acta_aprobacion}
    return render(request,"acta_aprobacion/editar.html",context)

# @login_required(login_url="login")
# def eliminarSolicitud(request,id):
#     solicitud=Solicitud.objects.get(id=id)
#     solicitud.delete()
#     messages.success(request,"Solicitud Eliminado")
#     return redirect(to="listarSolicitud")

#**********************************SOLICITUD TESIS**********************************************************

@login_required(login_url="login")
def listarSolicitudTesis(request):
    queryset = request.GET.get("buscar")
    solicitudes=SolicitudTesis.objects.filter(alumno = request.user.alumno)
    page = request.GET.get("page",1)
    if queryset:
        solicitudes=SolicitudTesis.objects.filter( 
            alumno__id__in = Alumno.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
            )
        ).distinct()
    try:
        paginator = Paginator(solicitudes,5)
        solicitudes = paginator.page(page)
    except:
        raise Http404
    context={'entity':solicitudes, 'paginator':paginator}
    return render(request,"solicitud_tesis/listar.html",context)

@login_required(login_url="login")
def agregarSolicitudTesis(request):
    if request.method=="POST":
        form=SolicitudTesisForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.alumno = request.user.alumno
            solicitud.save()
            messages.success(request,"Solicitud Tesis Guardado Correctamente")
            return redirect("listarSolicitudTesis")

    else:
        form=SolicitudTesisForm()
    context={'form':form}
    return render(request,"solicitud_tesis/agregar.html",context)

@login_required(login_url="login")
def editarSolicitudTesis(request,id):
    solicitud=SolicitudTesis.objects.get(id=id)
    if request.method=="POST":
        form=SolicitudTesisForm(request.POST,instance=solicitud, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Solicitud Tesis Actualizado Correctamente")
            return redirect("listarSolicitudTesis")
    else:
        form=SolicitudTesisForm(instance=solicitud)
    context={"form":form}
    return render(request,"solicitud_tesis/editar.html",context)

@login_required(login_url="login")
def eliminarSolicitudTesis(request,id):
    solicitud=SolicitudTesis.objects.get(id=id)
    solicitud.delete()
    messages.success(request,"Solicitud Tesis Eliminado")
    return redirect(to="listarSolicitudTesis")

#**********************************SOLICITUD EVALUAR**********************************************************
@login_required(login_url="login")
def listarSolicitudTesisEvaluar(request):
    queryset = request.GET.get("buscar")
    solicitudes=SolicitudTesis.objects.filter(
        alumno__id__in = Alumno.objects.filter(
            escuela__id__in= Escuela.objects.filter(
                escuela= request.user.director.escuela.escuela
            )
        ),
        enviar = True
    )
    page = request.GET.get("page",1)
    if queryset:
        solicitudes=SolicitudTesis.objects.filter(
            alumno__id__in = Alumno.objects.filter(
                escuela__id__in= Escuela.objects.filter(
                    escuela= request.user.director.escuela.escuela
                )  
            ).filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
            ),
        enviar = True
        ).distinct()
    try:
        paginator = Paginator(solicitudes,5)
        solicitudes = paginator.page(page)
    except:
        raise Http404
    context={'entity':solicitudes, 'paginator':paginator}
    return render(request,"solicitud_tesis/evaluar/listar.html",context)

@login_required(login_url="login")
def editarSolicitudTesisEvaluar(request,id):
    solicitud=SolicitudTesis.objects.get(id=id)
    if request.method=="POST":
        form=SolicitudFormEvaluar(request.POST,instance=solicitud, files=request.FILES)
        if form.is_valid(): 
            form.save()
            if solicitud.estado == 'Aceptada':
                inscripcion_tesis = InscripcionTesis(solicitud=solicitud)
                inscripcion_tesis.save()
            messages.success(request,"Solicitud Tesis Actualizado Correctamente")
            return redirect("listarSolicitudTesisEvaluar")
    else:
        form=SolicitudTesisFormEvaluar(instance=solicitud)
    context={"form":form, 'solicitud':solicitud}
    return render(request,"solicitud_tesis/evaluar/editar.html",context)

#**********************************INSCRIPCION TESIS**********************************************************

@login_required(login_url="login")
def listarInscripcionTesis(request):
    queryset = request.GET.get("buscar")
    inscripciones_tesis=InscripcionTesis.objects.filter(
        solicitud__id__in = SolicitudTesis.objects.filter(
            alumno=request.user.alumno.id
            )
        )
    page = request.GET.get("page",1)
    if queryset:
        inscripciones_tesis=InscripcionTesis.objects.filter( 
            solicitud__id__in = SolicitudTesis.objects.filter(alumno=request.user.alumno.id),
            asesor__id__in = Asesor.objects.filter(
                docente__id__in = Docente.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
                )
            )
        ).distinct()
    try:
        paginator = Paginator(inscripciones_tesis,5)
        inscripciones_tesis = paginator.page(page)
    except:
        raise Http404
    context={'entity':inscripciones_tesis, 'paginator':paginator}
    return render(request,"inscripcion_tesis/listar.html",context)

@login_required(login_url="login")
def editarInscripcionTesis(request,id):
    inscripcion_tesis=InscripcionTesis.objects.get(id=id)
    if request.method=="POST":
        form=InscripcionTesisForm(request.POST,instance=inscripcion_tesis, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Inscripcion Tesis Actualizado Correctamente")
            return redirect("listarInscripcionTesis")
    else:
        form=InscripcionTesisForm(instance=inscripcion_tesis)
        asesores = Asesor.objects.filter(
            docente__id__in = Docente.objects.filter(
                escuela = request.user.alumno.escuela
            ),
            tipo = 'Tesis'
        )
        form.fields['asesor'].queryset = asesores
    context={"form":form}
    return render(request,"inscripcion_tesis/editar.html",context)

# @login_required(login_url="login")
# def eliminarTramite(request,id):
#     tramite=Tramite.objects.get(id=id)
#     tramite.delete()
#     messages.success(request,"Tramite Eliminado")
#     return redirect(to="listarTramite")

#**********************************INSCRIPCION TESIS EVALUAR**********************************************************
@login_required(login_url="login")
def listarInscripcionTesisEvaluar(request):
    queryset = request.GET.get("buscar")
    inscripciones_tesis=InscripcionTesis.objects.filter(
        asesor__id__in = Asesor.objects.filter(
            docente=request.user.docente.id
        ),
        enviar=True
    )
    page = request.GET.get("page",1)
    if queryset:
        inscripciones_tesis=InscripcionTesis.objects.filter( 
            asesor__id__in = Asesor.objects.filter(
                docente=request.user.docente.id
            ),
            solicitud__id__in = SolicitudTesis.objects.filter(
                alumno__id__in = Alumno.objects.filter(
                Q(nombre__icontains=queryset) |
                Q(apellido_paterno__icontains=queryset) |
                Q(apellido_materno__icontains=queryset)
                )
            ),
            enviar=True
        ).distinct()
    try:
        paginator = Paginator(inscripciones_tesis,5)
        inscripciones_tesis = paginator.page(page)
    except:
        raise Http404
    context={'entity':inscripciones_tesis, 'paginator':paginator}
    return render(request,"inscripcion_tesis/evaluar/listar.html",context)

@login_required(login_url="login")
def editarInscripcionTesisEvaluar(request,id):
    inscripcion_tesis=InscripcionTesis.objects.get(id=id)
    if request.method=="POST":
        form=InscripcionTesisFormEvaluar(request.POST,instance=inscripcion_tesis, files=request.FILES)
        if form.is_valid(): 
            form.save()
            if inscripcion_tesis.estado == 'Aprobado':
                sustentacion_tesis = SustentacionTesis(inscripcionTesis=inscripcion_tesis)
                sustentacion_tesis.save()
            messages.success(request,"Inscripcion Tesis Actualizado Correctamente")
            return redirect("listarInscripcionTesisEvaluar")
    else:
        form=InscripcionTesisFormEvaluar(instance=inscripcion_tesis)
    context={"form":form, 'tramite':inscripcion_tesis}
    return render(request,"inscripcion_tesis/evaluar/editar.html",context)
#**********************************SUSTENTACION TESIS**********************************************************

@login_required(login_url="login")
def listarSustentacionTesis(request):
    queryset = request.GET.get("buscar")
    sustentacion_tesis=SustentacionTesis.objects.filter(
        inscripcionTesis__id__in=InscripcionTesis.objects.filter(
            solicitud__id__in = SolicitudTesis.objects.filter(
                alumno=request.user.alumno.id
            )
        )
    )
    page = request.GET.get("page",1)
    if queryset:
        sustentacion_tesis=SustentacionTesis.objects.filter(
            inscripcionTesis__id__in=InscripcionTesis.objects.filter(
                solicitud__id__in = SolicitudTesis.objects.filter(alumno=request.user.alumno.id),
                asesor__id__in = Asesor.objects.filter(
                    docente__id__in = Docente.objects.filter(
                    Q(nombre__icontains=queryset) |
                    Q(apellido_paterno__icontains=queryset) |
                    Q(apellido_materno__icontains=queryset)
                    )
                )
            )
        ).distinct()
    try:
        paginator = Paginator(sustentacion_tesis,5)
        sustentacion_tesis = paginator.page(page)
    except:
        raise Http404
    context={'entity':sustentacion_tesis, 'paginator':paginator}
    return render(request,"sustentacion_tesis/listar.html",context)

@login_required(login_url="login")
def editarSustentacionTesis(request,id):
    sustentacion_tesis=SustentacionTesis.objects.get(id=id)
    if request.method=="POST":
        form=SustentacionTesisForm(request.POST,instance=sustentacion_tesis, files=request.FILES)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Sustentacion Tesis Actualizado Correctamente")
            return redirect("listarSustentacionTesis")
    else:
        form=SustentacionTesisForm(instance=sustentacion_tesis)
    context={"form":form}
    return render(request,"sustentacion_tesis/editar.html",context)

# @login_required(login_url="login")
# def eliminarTramite(request,id):
#     tramite=Tramite.objects.get(id=id)
#     tramite.delete()
#     messages.success(request,"Tramite Eliminado")
#     return redirect(to="listarTramite")
#**********************************SUSTENTACION TESIS ASIGNAR**********************************************************
@login_required(login_url="login")
def listarSustentacionTesisAsignar(request):
    queryset = request.GET.get("buscar")
    sustentaciones_asignar = SustentacionTesis.objects.filter(
        inscripcionTesis__id__in=InscripcionTesis.objects.filter(
            solicitud__id__in = SolicitudTesis.objects.filter(
                alumno__id__in=Alumno.objects.filter(
                    escuela__id__in=Escuela.objects.filter(
                        escuela=request.user.director.escuela.escuela
                    )
                )
            ),
            enviar=True,
            estado= 'Aprobado'
        ),
        enviar=True,
    )
    page = request.GET.get("page",1)
    if queryset:
        sustentaciones_asignar = SustentacionTesis.objects.filter(
            inscripcionTesis__id__in=InscripcionTesis.objects.filter(
                solicitud__id__in = SolicitudTesis.objects.filter(
                    alumno__id__in = Alumno.objects.filter(
                    Q(nombre__icontains=queryset) |
                    Q(apellido_paterno__icontains=queryset) |
                    Q(apellido_materno__icontains=queryset)
                    ).filter(
                        escuela__id__in=Escuela.objects.filter(
                        escuela=request.user.director.escuela.escuela
                    )
                    )
                ),
                enviar=True,
            estado= 'Aprobado'
            ),
            enviar=True
        ).distinct()
    try:
        paginator = Paginator(sustentaciones_asignar,5)
        sustentaciones_asignar = paginator.page(page)
    except:
        raise Http404
    context={'entity':sustentaciones_asignar, 'paginator':paginator}
    return render(request,"sustentacion_tesis/asignar/listar.html",context)

@login_required(login_url="login")
def editarSustentacionTesisAsignar(request,id):
    sustentacion_tesis=SustentacionTesis.objects.get(id=id)
    jurados = Jurado.objects.filter(
            docente__id__in = Docente.objects.filter(
                escuela = request.user.director.escuela
            )
        )
    if request.method=="POST":
        if int(request.POST.get('jurados')) == 3:
            if datetime.datetime.today() < parser.parse(request.POST.get('fecha_sustentacion')):
                form=SustentacionTesisFormAsignar(request.POST,instance=sustentacion_tesis, files=request.FILES)
                if form.is_valid(): 
                    form.save()
                    messages.success(request,"Sustentacion Tesis Actualizado Correctamente")
                    return redirect("listarSustentacionTesisAsignar")
            else:
                messages.error(request,"LA FECHA DE SUSTENTACION DEBE SER UNA FECHA POSTERIOR A HOY")
                form=SustentacionTesisFormAsignar(instance=sustentacion_tesis)
                form.fields['jurados'].queryset = jurados
                context={"form":form,'tramite':sustentacion_tesis}
                return render(request,"sustentacion_tesis/asignar/editar.html",context)
        else:
            messages.error(request,"DEBEN SER 3 JURADOS SELECCIONADOS")
            form=SustentacionTesisFormAsignar(instance=sustentacion_tesis)
            form.fields['jurados'].queryset = jurados
            context={"form":form,'tramite':sustentacion_tesis}
            return render(request,"sustentacion_tesis/asignar/editar.html",context)
    else:
        form=SustentacionTesisFormAsignar(instance=sustentacion_tesis)
        form.fields['jurados'].queryset = jurados
    context={"form":form,'tramite':sustentacion_tesis}
    return render(request,"sustentacion_tesis/asignar/editar.html",context)

#**********************************SUSTENTACION TESIS EVALUAR**********************************************************
@login_required(login_url="login")
def listarSustentacionTesisEvaluar(request):
    queryset = request.GET.get("buscar")
    sustentaciones_evaluar = SustentacionTesis.objects.filter(
        jurados = request.user.docente.jurado,
        asignada= True,
        enviar=True
    ).order_by('-fecha_sustentacion')
    page = request.GET.get("page",1)
    if queryset:
        sustentaciones_evaluar = SustentacionTesis.objects.filter(
            jurados = request.user.docente.jurado,
            inscripcionTesis__id__in=InscripcionTesis.objects.filter(
                solicitud__id__in = SolicitudTesis.objects.filter(
                    alumno__id__in = Alumno.objects.filter(
                    Q(nombre__icontains=queryset) |
                    Q(apellido_paterno__icontains=queryset) |
                    Q(apellido_materno__icontains=queryset)
                    ).filter(
                        escuela__id__in=Escuela.objects.filter(
                            escuela=request.user.docente.escuela.escuela
                        )
                    )
                ),
                enviar=True,
            estado= 'Aprobado'
            ),
            asignada= True,
            enviar=True
        ).order_by('-fecha_sustentacion').distinct()
    try:
        paginator = Paginator(sustentaciones_evaluar,5)
        sustentaciones_evaluar = paginator.page(page)
    except:
        raise Http404
    context={'entity':sustentaciones_evaluar, 'paginator':paginator}
    return render(request,"sustentacion_tesis/evaluar/listar.html",context)

@login_required(login_url="login")
def editarSustentacionTesisEvaluar(request,id):
    sustentacion_tesis=SustentacionTesis.objects.get(id=id)
    tesis_jurado =  sustentacion_tesis.tesisjurado_set.filter(
        jurado = request.user.docente.jurado
    ).first()
    if request.method=="POST":
        form=TesisJuradoForm(request.POST,instance=tesis_jurado)
        if form.is_valid(): 
            form.save()
            jurados_notas = sustentacion_tesis.tesisjurado_set.filter(evaluada=True).count()
            if jurados_notas==3:
                promedio = sustentacion_tesis.tesisjurado_set.all().aggregate(Avg('nota'))
                promedio_entero = int(promedio.get('nota__avg'))
                sustentacion_tesis.nota = promedio_entero
                if promedio_entero > 14 :
                    sustentacion_tesis.estado = 'Aprobado'
                else:
                    sustentacion_tesis.estado = 'Desaprobado'
                sustentacion_tesis.save()
            messages.success(request,"Sustentacion Tesis Actualizado Correctamente")
            return redirect("listarSustentacionTesisEvaluar")
    else:
        form=TesisJuradoForm(instance=tesis_jurado)
    context={"form":form,'tramite':sustentacion_tesis}
    return render(request,"sustentacion_tesis/evaluar/editar.html",context)