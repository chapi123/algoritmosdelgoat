def sum_list(listt):
    if len(listt) == 0:
        return 0
    return listt[0] + sum_list(listt[1:])

def main () :
    listt = list((range(0,501)))
    print(sum_list(listt))

main ()

#en caso de no esctibir el caso base el codigo dice error de indice porque en un momento
#se vacia la lista y el codigo intenta acceder a un valor que no existe.