Create a groceries list containing atleast six items 
groceries=['beans', 'rice', 'millet', 'oat', 'garri', 'wheat']
Write a python program to print the indexes of the previoiusly created list using the following index (index2,2 till end, 4 and 5)
print(groceries)
print(groceries[2])
print(groceries [2:])
print(groceries [4:6])

# # Write a program to append, insert, extend, remove to the list
groceries.append("soya")
print(groceries)
groceries.insert(0, "flakes")
print(groceries)
added_groceries = ["milk", "choco", "sugar"]
groceries.extend(added_groceries)
print(groceries)
groceries.remove("millet")
print(groceries)

# # Create a nested dictionary using different 3 kinds of phones and their keys should be name, model, storage and ram. 
# # Use the update method to change the ram size of the second phone.
Phone_Brands={
    "tecno":{
    "model":"spark7",
    "storage":"256gb",
    "ram":"4"
    },

    "infinix":{
    "model":"hot5",
    "storage":"32gb",
    "ram":"2"
    },

    "redmi":{
    "model":"10c",
    "storage":"64gb",
    "ram":"4"
    }
}
Phone_Brands['infinix'].update({'ram':'6'})
print(Phone_Brands['infinix'])