# saved as greeting-client.py
import Pyro4

uri = input("Masukkan Pyro uri dari greeting object? ").strip()

# get a Pyro proxy to the greeting object
calculator = Pyro4.Proxy(uri)
# print(calculator.get_fortune(name))   # call method normally

num1 = float (input("Enter x : "))
num2 = float (input("Enter y : "))

print ("\nLebih besar mana ? ")
print (calculator.cek(num1,num2))

print ("\nA List Of Available Mathematical Operations")
print ("1.Add ")
print ("2.Substract")
print ("3.Multiple ")
print ("4.Divide \n ")
opr = int (input("Masukkan pilihan (1,2,3,4): "))

if opr==1:
    print ("Result: ")
    print (calculator.add(num1,num2))
elif opr==2:
    print ("Result: ")
    print (calculator.sub(num1,num2))
elif opr==3:
    print ("Result: ")
    print (calculator.mul(num1,num2))
elif opr==4:
    print ("Result: ")
    print (calculator.div(num1,num2))
else:
    print ("\n operasi matematika tidak ada")
