# Extra functions for FBA



def find_index_of_compound(stoichiomatrix_array, compound_name):

    for i in range(len(stoichiomatrix_array)):
        if stoichiomatrix_array[i][0] == compound_name:
            return i

    return -1

#This function takes a file like the ones in the example folder and 
# Creates a d2 list (table list)
def get_rxn_list_d2_example(file_name):
    f = open(file_name, 'r')
    X = f.readlines()
    f.close()

    rxn_list_d2 = []

    for i in range(len(X)):
        rxn = X[i]
        rxn = rxn.replace('\n','')
        y = rxn.split(':')
        #We need to return a list with [[rxn string, rxn name], [rxnstr,rxnname],...]
        if len(y)>1:
            z = [y[1],y[0]]
            rxn_list_d2.append(z)

    

    return rxn_list_d2




