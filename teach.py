#1 Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
   # multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
   # "FizzBuzz".

 #variable
def num(int):

    if num % 3 == 0:
        print("Fizz")

#Loop until 100.
for num in range(1, 101):
    string=""
    if num % 3 ==0:
        string = string + "Fizz"
    if num % 5 == 0:
        string =string + "Buzz"
    if num % 3 !=0 and num % 5 !=0:
        string = string + str(num)  
    print(string)

#2  Write a program to generate the Fibonacci sequence up to 100   
def PrintFibonacci(length):
    #variables
    firstnum = 0
    secondnum = 1

    print(firstnum, secondnum, end=" ")

    #decreasing the length by two
    length -= 2
    
    #Loop until the length= 0.
    while length > 0:

        print(firstnum + secondnum, end=" ")
 
        temp = secondnum
        secondnum = firstnum + secondnum
        firstnum = temp

        #Decreasing the length that states the Fibonacci numbers to be printed more.
        length -= 1

if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(12)
pass   


#3 Write a program that takes an integer as input and returns true if the input is a power of two.
num=int(input("\n" "enter the integer number: "))
i=0
result=0
while result< num:
    result = 1<<i
    if result == num:
        print("True")
        break
    i=i+1
else:
    print("False")    

#4 Write a program that accepts a string as input, capitalizes the first letter of each word in the 
    # string, and then returns the result string.

mystring=(input("\n" "Type something: "))
print (mystring.title())


#5 Write a program that takes an integer as input and returns an integer with reversed digit ordering.
num=int(input("\n" "enter the integer number: "))
print(str(num)[::-1])

#6 Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    sentence = input("Enter a sentence: ")
    num_vowels = count_vowels(sentence)
    print("Number of vowels:", num_vowels)

if __name__ == "__main__":
    main()
