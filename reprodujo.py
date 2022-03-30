from pregunyrespu import pregunta1, respuesta1

score = 0

print('Recuerda Respetar Mayusculas y minusculas ')
responder = input(pregunta1)
if (responder == respuesta1 ) :
    
    print('Correcto')
    score += 15
else: 
    print('Incorrecto')
    

    
    
print(score)


