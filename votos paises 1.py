
import pygal
worldmap = pygal.maps.world.World()
worldmap.title = "Countries"

paises=["italia","frança","tailandia","japão","espanha","estados unidos"]

votospaises=[0]*len(paises)

votos = -1

total_votos = 0

print('Se pudesse visitar um lugar do mundo, para onde você iria?')
print('='*100)

i = 0
print(f"{0:2d} --> Encerrar")
for i, pais in enumerate(paises):
    print(f"{i+1:2d} --> {pais}")
    i+=1

while votos != 0:
    votos=int(input(f"Digite o seu voto entre 1 e {len(paises)} ou 0 para encerrar:"))
    if not (0<votos<7):
        print(f'= Digite apenas opções de 1 a {len(paises)} ou 0 para encerrar-')
        continue
    if votos == 0:
        break
    votospaises[votos - 1] += 1
    total_votos += 1


print("="*100)
print("resultado da enquete:")
print("="*100)
maiorvoto = 0
i = 0
for k in range(len(paises)):
    print(f'{paises[i]:16s}  --->  {votospaises[i]:2d}  --->  {votospaises[i] / float(total_votos) * 100:.2f}%')
    if votospaises[i] > votospaises[maiorvoto]:
        maiorvoto = i
    i += 1

print("=" * 100)
print('Total de votos: {}'.format(total_votos))


print('=' * 100)
print('O vencedor da enquete foi {}, com {} votos, correspondendo ao percentual de {:.2f}% '
      'dos votos válidos.'.format(paises[maiorvoto], votospaises[maiorvoto],
                                  (votospaises[maiorvoto]) / float(total_votos) * 100))

paisesmap=["it","fr","th","jp","es","us"]
for k in range(len(paisesmap)):
    worldmap.add(paises[k], {
        f"{paisesmap[k]}": votospaises[k],
        
    })
    k+=1
worldmap.render_to_file("votos.svg")
print('Success')
