import datetime
from multiprocessing import Process, Queue

def collatz_conjecture(a):
    sequence = [] # List of sequence for each number
    while a != 1: # To exit the cycle
        sequence.append(a) # Add current a in list
        if a % 2 == 0: # Check for parity, if not --> else
            a = a // 2 # If the number is even, divide a by 2 (a//2)
        else: # Number a is not even
            a = a * 3 + 1 # if the number is not even, multiply a by 3 and add 1 (a*3+1)
    sequence.append(1) # Add number 1 in the end of the list, because 1 is last number of our sequence
    return sequence # Return list of our sequence for one number


def part_count(start_number, end_number, queue_obj):
    for i in range(start_number, end_number): # For each i in range start_number to end_number
        sequence = collatz_conjecture(i) # For each i calculating Collatz conjecture
        queue_obj.put((i, sequence)) # Save the result of the Collatz conjecture in the queue


if __name__ == '__main__':
    a = Queue() # Create a queue to store the results
    # Next step we create four process, each of which will process a different part of the range of numbers
    t1 = Process(target=part_count, args=(1, 50, a)) # Create the first process
    t2 = Process(target=part_count, args=(50, 100, a)) # Create a second process
    t3 = Process(target=part_count, args=(100, 150, a)) # Create a third process
    t4 = Process(target=part_count, args=(150, 210, a)) # Create a fourth process
    print("Counting...")
    print("Please wait...")
    # Start the process
    start_time = datetime.datetime.now() # Time of process start
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # Wait when all process complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    end_time = datetime.datetime.now() # End time of process

    print("Time taken: " + str(end_time - start_time)) # Output to user the program execution time

    total = 0
    while not a.empty(): # As long as there are items in the queue
        number, sequence = a.get() # Extract a number and its sequence
        print(f"Number: {number}, Collatz conjecture for this number: {sequence}") # Output to user Number and Collatz conjecture for this number
        total += len(sequence) # Count the total number of numbers in the sequences

    print(f"Total: {total}") # Output total number of numbers in Collatz conjecture