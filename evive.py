from queue import PriorityQueue
class FoodOrderSystem:

    def check_rules(self, item, dict_final,*id):
        #Declare a priority queue to get elements in the order Main,Side and Drink
        print_list_break_fast = PriorityQueue()
        final_list_breakfast = []
       
        if len(id) > 0:
            for i in id:
                # For checking the rules for dinner that are different from breakfast and lunch
                if item == 'Dinner':
                    if id.count(4) == 0:
                        print("Unable to process: Desert is Missing")
                        break
                    elif id.count(i) > 1:
                        print_list_break_fast.put((i,dict_final[i]+"("+str(id.count(i))+")"))
                
                    else:
                        print_list_break_fast.put((3.5,"Water"))
                        print_list_break_fast.put((i,dict_final[i]))

                elif id.count(1) == 0:
                    print("Unable to process: Main is Missing")
                    break
                
                    
                elif id.count(2) == 0:
                    print("Unable to process: Side is Missing")
                    break
                
                
                elif id.count(1) > 1:
                    print(dict_final[i]+ " cannot be ordered more than once.")
                    break
                
                elif id.count(i) > 1:
                    print_list_break_fast.put((i,dict_final[i]+"("+str(id.count(i))+")"))
                
                elif id.count(3) == 0:
                    print_list_break_fast.put((5,"Water"))
                    print_list_break_fast.put((i,dict_final[i]))
                               
                else:
                    print_list_break_fast.put((i,dict_final[i]))
                                
        else:
            print("Unable to process: Main is missing, side is missing")
        
        #Code for not printing the duplicates.
        while not print_list_break_fast.empty():
            next_item = print_list_break_fast.get()
            if next_item not in final_list_breakfast:
                final_list_breakfast.append(next_item)
        
        
        #Print in the given order
        for i in final_list_breakfast:
            print(i[1])

    def make_menu(self,item,*id): 
        
        if item == 'Breakfast':
            #Dictionary to store breakfast menu items.
            break_fast_item_dict = {1: "Eggs", 2: "Toast", 3 : "Coffee"}
            self.check_rules(item,break_fast_item_dict,*id)

        if item == 'Lunch':
            #Dictionary to store lunch menu items.
            lunch_item_dict = {1: "Sandwich", 2: "Chips", 3 : "Soda"}
            self.check_rules(item,lunch_item_dict,*id)

        
        if item == 'Dinner':
            #Dictionary to store dinnner menu items.
            dinner_item_dict = {1: "Steak", 2: "Potatoes", 3 : "Wine", 4 : "Cake"}
            self.check_rules(item, dinner_item_dict, *id)


#Test Cases 
#Created a class and it's object for calling the functions of the class
b1 = FoodOrderSystem()
b1.make_menu("Breakfast",1,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Breakfast",2,3,1)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Breakfast",1,2,3,3,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Breakfast",1)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Breakfast",1,2,2)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2,2,2,2,2,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,1,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2,2)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch")
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2,2,2,2,2,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,1,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch",1,2,2)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Lunch")
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Dinner",1,2,3,4)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Dinner",1,2,3)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Dinner",1,2,2,3,3,4)
print(" ")
print("----------------------------------------------------")
print(" ")
b1.make_menu("Dinner")
print(" ")
