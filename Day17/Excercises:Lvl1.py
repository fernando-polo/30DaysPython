# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'] 

try:
    *nordic_countries, estonia, russia = names
    es = [estonia, russia]
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
else:
    print(nordic_countries) 
    print(es)   
finally:
    print ('Gracias por probar')            