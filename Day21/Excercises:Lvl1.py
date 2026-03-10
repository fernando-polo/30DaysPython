# Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. 
# Check the output below.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range()) # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29

#Crear una clase que acepte como parametro una variable que sea lista
#Hacer todos los métodos.

class Statitsitcs:
    def __init__(self, ages):
        self.ages = ages
    
    def count(self):
        #por cada iteración que haga, sumar un numero para saber el número total de elementos que hay
        suma = 0
        for i in self.ages:
            suma += 1
        return f'Count: {suma}'
    
    def sum(self):
        #por cada iteración sumar el valor de la iteración
        suma = 0
        for i in self.ages:
            suma += i
        return f'Sum: {suma}'
    
    def min(self):
        #ordenar la lista de menor a mayor e imprimir el numero menor
        self.ages.sort()
        return f'Min: {self.ages[0]}'
    
    def max(self):
        #ordenar la lista de menor a mayor y tomar el último número (el más alto)
        self.ages.sort()
        return f'Max: {self.ages[-1]}'
    
    def range(self):
        #ordenar la lista de menor a mayor, tomar el último valor y el primero valor y entonces restarlos.
        self.ages.sort()
        range = self.ages[-1] - self.ages[0]
        return f'Range: {range}'
    
    def mean(self):
        #sumar el valor de todas las iteraciones y dividir entre el número de datos en la lista
        suma = 0
        num_datos = len(self.ages)
        for i in self.ages:
            suma += i
        mean = round(suma / num_datos)
        return f'Mean: {mean}'
    
    def median(self):
        self.ages.sort()
        num_datos = len(self.ages)
        mid = num_datos // 2

        try:
            if num_datos % 2 == 0:  
                resultado = (self.ages[mid - 1] + self.ages[mid]) / 2
            else:                   
                resultado = self.ages[mid]
            return f'Median: {resultado}'
        except IndexError:
            return 'La lista está vacía'
        

        


Statitsitcs1 = Statitsitcs(ages)
print(Statitsitcs1.count())
print(Statitsitcs1.sum())
print(Statitsitcs1.min())
print(Statitsitcs1.max())
print(Statitsitcs1.range())
print(Statitsitcs1.mean())
print(Statitsitcs1.median())
    
