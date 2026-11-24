# sommare gli elementi di una lista dentro a una funzione di nome sum_list

def sum_list(a):
    somma = 0
    for i in range(len(a)):
        somma += a[i]
    return somma 



# ----- main --------

my_list = [10, 5, 4, 3, 2, 1, 8]        
final_grade = sum_list(my_list)
print(final_grade)

