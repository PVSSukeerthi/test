N = int(input("Enter the number of bits in ADC :"))  #taking inputs for the the calculator
avi = int(input("Enter the Analog Voltage input to ADC :"))
ref = int(input("Enter the Reference voltage to ADC :"))

def Binary_converter(decimal):      #function to convert the output to binary
    binary = ""
    while decimal > 0:
        bit = decimal % 2
        binary = str(bit)+binary
        decimal = decimal //2
    return binary

def ADC_calculator(N,aiv,ref):   #function to calculate the digital output
    Digital_output = ((2 ** N)*(avi))//ref
    return Digital_output

Numerical_Digital_output = ADC_calculator(N,avi,ref)    #generating the output
Binary_Digital_output = Binary_converter(Numerical_Digital_output)
print("Numeric Digital Output :",Numerical_Digital_output)
print("Binary Digital Output :",Binary_Digital_output)
