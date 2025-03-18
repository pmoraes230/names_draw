import random
from django.shortcuts import render

def main(request):
    if request.method == 'POST':
        nomes = request.POST.get('nomes')
        vezes_rodadas = request.POST.get('vezes_rodadas')

        if nomes and vezes_rodadas:
            nomes_lista = [nome.strip() for nome in nomes.split(',') if nome.strip()]
            vezes_rodadas = int(vezes_rodadas)

            resultado = sortear_nomes(nomes_lista, vezes_rodadas)

            return render(request, 'index.html', {'resultado': resultado})

    return render(request, 'index.html')

def sortear_nomes(nomes_lista, qtd_individuos_por_grupo):
    random.shuffle(nomes_lista)
    
    grupos = [nomes_lista[i:i + qtd_individuos_por_grupo] for i in range(0, len(nomes_lista), qtd_individuos_por_grupo)]

    return grupos
