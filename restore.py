import pickle

#Serialization
def checkpoint_save(data, filename):
    with open(filename,'wb') as file:
        pickle.dump(data,file)

#Deserialization
def load_checkpoint(filename):
    try:
        with open(filename,'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        return None

def entry_numbers():
    while True:
        try:
            entry=input("Enter de numbers separate with 'spaces': ")
            numbers=[int(x) for x in entry.split()]
            return numbers
        except ValueError:
            print("Error: Not a valid number")

def restore(checkpoint_file):
    checkpoint_data = load_checkpoint(checkpoint_file)
    if checkpoint_data:
        print("Recovering checkpoint data:",checkpoint_data)
    else:
        print("No data found in checkpoint.")
    
    while True:
        try:
            numbers=entry_numbers()
            add=sum(numbers)
            print("The addition of the numbers:",add)
            checkpoint_save(numbers,checkpoint_file)
            print("Checkpoint saved")
            break
        except KeyboardInterrupt:
            print("\nInterrupted process. Loading checkpoint...")
            if checkpoint_data:
                print("Last data valid:", checkpoint_data)
                break
            else:
                print("no chekpoint loaded. Restarting from the begining")

checkpoint_file = "checkpoint_data.pkl"
restore(checkpoint_file)