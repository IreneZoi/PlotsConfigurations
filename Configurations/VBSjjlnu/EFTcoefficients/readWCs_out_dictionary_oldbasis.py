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


def calculate_quadratic_function(filename, op, WC, result_dict):
    # creates a dictionary of operators and Wilson Coefficients
    vector = []
    with open(filename, 'r') as f:
        for line in f:
            if 'set param_card anoinputs' in line:
                if op not in line:
                    vector.append('x')
                else:
                    value_str = line.split(" ")[1].replace('id="','').replace('">set','')
                    value_str = value_str.split("_")[-1].strip()  # get the value string after "_" and remove any whitespace
                    print(value_str)
                    if 'p' or 'm' in value_str:
                        value = float(value_str.replace("p", ".").replace("m", "-"))  # replace "p" with "." and "m" with "-" and convert to float
                    else:
                        value = float(value_str)
                    vector.append(value)
    #print('**************************')         # debug
    #print(vector)                               # debug
    LHEwPLUS = find_position(WC, vector)
    LHEwMINUS = find_position(-WC, vector)
    LHEwZERO = find_position(0, vector)

    if LHEwPLUS and LHEwMINUS != -1:
        result_dict[op] = {
            'quadReweight': '( 0.5* (1/({0})) * (1/({0})) * ( LHEReweightingWeight[{1}] + LHEReweightingWeight[{2}] - 2 * LHEReweightingWeight[{3}]))'.format(WC, LHEwPLUS, LHEwMINUS, LHEwZERO, op),
            'LinReweight': '( 0.5* (1/({0})) * ( LHEReweightingWeight[{1}] - LHEReweightingWeight[{2}] ))'.format(WC, LHEwPLUS, LHEwMINUS, LHEwZERO, op),
            'sm': '( LHEReweightingWeight[{3}] )'.format(WC, LHEwPLUS, LHEwMINUS, LHEwZERO, op)
        }   
        #print(op)                               # debug
        #print(result_dict[op])                  # debug
    else:
        print('wilson coefficient {} not found for the operator {}'.format(WC, op))


filename = 'initrwgt_aQGC17.header'
ops = ['ft0','ft1','ft2','ft5','ft6','ft7', 'ft8','ft9','fs0','fs1','fs2','fm0','fm1','fm2','fm3','fm4','fm5','fm7']  # List of operators
WCs = [0.5, 0.5, 0.5, 1, 1, 2, 0.5, 1.5, 5, 5, 5, 2, 5, 3, 5, 5, 5, 10]  # List of Wilson Coefficients

results = {}  # Dictionary to store results

for op, WC in zip(ops, WCs):
    calculate_quadratic_function(filename, op, WC, results)

# Replace "F" with "c" in ops and results dictionary keys
ops = [op.replace('f', 'c').replace('t','T').replace('m','M').replace('t','T').replace('s','S') for op in ops]
results = {op.replace('f', 'c').replace('t','T').replace('m','M').replace('t','T').replace('s','S'): values for op, values in results.items()}


# Writing results to a Python file
with open('EFT_dim8_dictionary_oldbasis.py', 'w') as f:
    f.write('operators = {\n')
    for op, values in results.items():
        f.write("    '%s': {\n" % op)
        for key, value in values.items():
            f.write("        '%s': '%s',\n" % (key, value))
        f.write('    },\n')
    f.write('}')


