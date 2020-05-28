# --------------
#Code starts here

#Function to read file
def read_file(path):
    myfile = open(path,'r')
    sentence=myfile.readline() # Don't use readlines() instead of readline(),                          otherwise it will read whole file and give list of that.
    myfile.close()
    return sentence


    
    #Opening of the file located in the path in 'read' mode
    
    #Reading of the first line of the file and storing it in a variable
    
    #Closing of the file
    
    #Returning the first line of the file
sample_message = read_file(file_path)
print(sample_message)  
    

#Calling the function to read file


#Printing the line of the file

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
print(message_1)
print(message_2)

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=(int(message_b)//int(message_a))
    #Returning the quotient in string format
    return str(quotient)
    
#Calling the function to read file  
secret_msg_1 = fuse_msg(message_1,message_2)
#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 

print(secret_msg_1)
message_3=read_file(file_path_3)
print(message_3)

#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if(message_c=='Red'):
        sub='Army General'
    elif(message_c=='Green'):
        sub='Data Scientist'
    elif(message_c=='Blue'):
        sub= 'Marine Biologist'
    
    #Returning the substitute of the message
    return sub
    
    

#Calling the function to read file
secret_msg_2 = substitute_msg(message_3)


#Calling the function 'substitute_msg'


#Printing the secret message
print(secret_msg_2)
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)


#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list = message_d.split()
    b_list = message_e.split()  # = compare_msg.split()  gives the error :                                       function' object has no attribute 'split'.
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    c_list = list(set(a_list)-set(b_list))
    final_msg = " ".join(c_list)
    return final_msg
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file
secret_msg_3 = compare_msg(message_4,message_5)
print(secret_msg_3)


#Calling the function to read file
message_6 = read_file(file_path_6)
print(message_6)

#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message
def extract_msg(message_f):
    a_list = message_f.split()
    
    #Splitting the message into a list

    
    #Creating the lambda function to identify even length words
    even_word = lambda x:(len(x)%2==0)
    b_list = list(filter(even_word,a_list))
    final_msg = " ".join(b_list)
    return final_msg
    
    #Splitting the message into a list
    
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
print(message_parts)

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg = " ".join(message_parts)
print(secret_msg)

#Function to write inside a file
def write_file(secret_msg,path):
    myfile=open(path,'a+')
    myfile.write(secret_msg)
    myfile.close()
write_file(secret_msg,final_path)
print(secret_msg)
       
    #Opening a file named 'secret_message' in 'write' mode


    #Writing to the file


    #Closing the file


#Calling the function to write inside the file    


#Printing the entire secret message


#Code ends here


