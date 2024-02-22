    
"""
    This code takes as input a reweighting weight txt file, 
    and the name of the Wilson Coefficient of interest, e.g. FS0
    and produces as output all possibile quadratic, linear, sm weights for Latinos:
    
    quadReweight_op = '( 0.5* (1/WC) * (1/WC) * (LHEReweightingWeight[+WC] + LHEReweightingWeight[-WC] - 2*LHEReweightingWeight[WC=0]) )'
    LinReweight_op = '(0.5 * (1/WC) * (LHEReweightingWeight[+WC] - LHEReweightingWeight[-WC]) )'
    sm_op = '(LHEReweightingWeight[WC=0])'

    Run the code with "python readWCs.py".
    Arguments of the code at the end.
"""



def find_position(number, array):
    """
    Finds the position of a given number in an array.

    Args:
        number (float): The number to search for in the array.
        array (list): The array to search in.

    Returns:
        int: The position (index) of the number in the array if found, else -1.
    """
    if number in array:
        return array.index(number)
    else:
        return -1


def calculate_quadratic_function(filename,op,WC):

    # creates a dictionary of opearatos and Wilson Coefficients 
    vector = []
    with open(filename, 'r') as f:
        for line in f:
            if 'launch --rwgt_name' in line:
                if op not in line:
                    vector.append('x') 
                else:      
                    value_str = line.split("_")[-1].strip() # get the value string after "_" and remove any whitespace
                    #print(value_str)
                    if 'p' or 'm' in value_str:
                        value = float(value_str.replace("p", ".").replace("m", "-")) # replace "p" with "." and "m" with "-" and convert to float
                    else:
                        value = float(value_str)
                    vector.append(value)
    print(vector)
    print('**************************')
    LHEwPLUS = find_position(WC,vector)
    LHEwMINUS = find_position(-WC,vector)
    LHEwZERO = find_position(0,vector)

    if LHEwPLUS and LHEwMINUS is not -1:
        print('quadReweight_{4} = "( 0.5* (1/({0})) * (1/({0})) * ( LHEReweightingWeight[{1}] + LHEReweightingWeight[{2}] - 2 * LHEReweightingWeight[{3}]))"'.format(WC,LHEwPLUS,LHEwMINUS,LHEwZERO,op.replace("F","c")))
        print('LinReweight_{4} = "( 0.5* (1/({0})) * ( LHEReweightingWeight[{1}] - LHEReweightingWeight[{2}] ))"'.format(WC,LHEwPLUS,LHEwMINUS,LHEwZERO,op.replace("F","c")))
        print('sm_{4} = "( LHEReweightingWeight[{3}] )"'.format(WC,LHEwPLUS,LHEwMINUS,LHEwZERO,op.replace("F","c")))
        print('SMLinQuadReweight_{0} = "("+ sm_{0} + " + " +LinQuadReweight_{0}+")"'.format(op.replace("F","c")))
    else:
        print('wilson coefficient'+WC+'not found for the operator'+op)









filename = 'aQGC_WPlepWMhadJJ_EWK_LO_SM_mjj100_pTj10_reweight_card.dat'
op='FT8'
WC=20
calculate_quadratic_function(filename,op,WC)
