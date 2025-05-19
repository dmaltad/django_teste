from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import CA, EPI, Estoque, Colaborador, Entrega

def index(request):
    return render(request, "base/index.html")

def ca_add(request):
    if request.method == "GET":
        cas = CA.objects.all()
        return render(request, "tabelas/tab_ca.html" , {'cas': cas})
    
    elif request.method == "POST":
        numero = request.POST.get('numero')
        validade = request.POST.get('validade')
        descricao = request.POST.get('descricao')
        ca = CA(numero=numero, validade=validade, descricao=descricao)
        ca.save()
        return redirect("/ca/") 
      
def ca_update(request, id):
    ca = get_object_or_404(CA, id=id)
    if request.method=="POST":
        numero = request.POST.get("numero")
        validade = request.POST.get('validade')
        descricao = request.POST.get('descricao')

        ca.numero= numero
        ca.validade = validade
        ca.descricao = descricao
        ca.save()
        return redirect('/ca/')
    return redirect('/ca/')

def ca_delete(request,id):
    ca = get_object_or_404(CA, id=id)
    ca.delete()
    return redirect("/ca/")
    
def epi_add(request):
    if request.method == "GET":
        epis = EPI.objects.all()
        return render(request, "tabelas/tab_epi.html" , {'epis': epis})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        ca = request.POST.get('validade')
        descricao = request.POST.get('descricao')
        vida_util = request.POST.get('vida_util')
        epi = CA(nome=nome, ca=ca, descricao=descricao, vida_util=vida_util)
        epi.save()
        return redirect("/epi/") 
      
def epi_update(request, id):
    epi = get_object_or_404(CA, id=id)
    if request.method=="POST":
        nome = request.POST.get('nome')
        ca = request.POST.get('validade')
        descricao = request.POST.get('descricao')
        vida_util = request.POST.get('vida_util')

        epi.nome= nome
        epi.ca = ca
        epi.descricao = descricao
        epi.vida_util = vida_util
        epi.save()
        return redirect('/epi/')
    return redirect('/epi/')

def epi_delete(request,id):
    epi = get_object_or_404(EPI, id=id)
    epi.delete()
    return redirect("/epi/")

def estoque_add(request):
    if request.method == "GET":
        estoques = Estoque.objects.all()
        return render(request, "tabelas/tab_estoque.html" , {'estoques': estoques})
    
    elif request.method == "POST":
        epi = request.POST.get('epi')
        quantidade = request.POST.get('quantidade')
        entrada = request.POST.get('entrada')
        estoque = Estoque(epi=epi, quantidade=quantidade, entrada=entrada)
        estoque.save()
        return redirect("/estoque/") 
      
def estoque_update(request, id):
    estoque = get_object_or_404(Estoque, id=id)
    if request.method=="POST":
        epi = request.POST.get('epi')
        quantidade = request.POST.get('quantidade')
        entrada = request.POST.get('entrada')

        estoque.epi= epi
        estoque.quantidade = quantidade
        estoque.entrada = entrada
        estoque.save()
        return redirect('/estoque/')
    return redirect('/estoque/')

def estoque_delete(request,id):
    estoque = get_object_or_404(Estoque, id=id)
    estoque.delete()
    return redirect("/estoque/")

def colaborador_add(request):
    if request.method == "GET":
        colaboradores = Colaborador.objects.all()
        return render(request, "tabelas/tab_colaborador.html" , {'colaboradores': colaboradores})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        matricula = request.POST.get('matricula')
        cargo = request.POST.get('cargo')
        setor = request.POST.get('setor')
        data_admissao = request.POST.get('data_admissao')
        colaborador = CA(nome=nome, cpf=cpf, matricula=matricula, cargo=cargo, setor=setor, data_admissao=data_admissao)
        colaborador.save()
        return redirect("/colaborador/") 
      
def colaborador_update(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method=="POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        matricula = request.POST.get('matricula')
        cargo = request.POST.get('cargo')
        setor = request.POST.get('setor')
        data_admissao = request.POST.get('data_admissao')

        colaborador.nome= nome
        colaborador.cpf = cpf
        colaborador.matricula = matricula
        colaborador.cargo = cargo
        colaborador.setor = setor
        colaborador.data_admissao = data_admissao
        colaborador.save()
        return redirect('/colaborador/')
    return redirect('/colaborador/')

def colaborador_delete(request,id):
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    return redirect("/colaborador/")
    

def entrega_add(request):
    if request.method == "GET":
        entregas = Entrega.objects.all()
        return render(request, "tabelas/tab_entrega.html" , {'entregas': entregas})
    
    elif request.method == "POST":
        colaborador = request.POST.get('colaborador')
        epi = request.POST.get('epi')
        quantidade = request.POST.get('quantidade')
        data_entrega = request.POST.get('data_entrega')
        entrega = Entrega(colaborador=colaborador, epi=epi, quantidade=quantidade, data_entrega=data_entrega)
        entrega.save()
        return redirect("/entrega/") 
      
def entrega_update(request, id):
    entrega = get_object_or_404(Entrega, id=id)
    if request.method=="POST":
        colaborador = request.POST.get('colaborador')
        epi = request.POST.get('epi')
        quantidade = request.POST.get('quantidade')
        data_entrega = request.POST.get('data_entrega')

        entrega.colaborador = colaborador
        entrega.epi = epi
        entrega.quantidade = quantidade
        entrega.data_entrega = data_entrega
        entrega.save()
        return redirect('/entrega/')
    return redirect('/entrega/')

def entrega_delete(request,id):
    entrega = get_object_or_404(Entrega, id=id)
    entrega.delete()
    return redirect("/entrega/")

