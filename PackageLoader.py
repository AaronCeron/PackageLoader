Item_number = int(input("Enter the number of products you want to send: "))

package_weight = 0

package_sent = 0 

total_sent_weight = 0

count_packages = 0 

package_with_most_empty_space = 0

Unused_capcity = 0

for item in range(Item_number):

    Item_weight = int(input("Enter the weight of each products: "))
    if Item_weight == 0:
        break
    if Item_weight < 1 or Item_weight > 10:
            print("wrong input ")
            continue
    total_sent_weight += Item_weight

    package_weight += Item_weight
    print("Package weight: " + str(package_weight))

    if package_weight == 20:
        package_sent += 1
        total_sent_weight += Item_weight
        Unused_capcity = 0
        print("Total weight: " + str(package_weight))
            
    elif package_weight >20:
        count_packages += 1
        total_sent_weight += package_weight - Item_weight
        print("Weight exceeds 20 kg. Package weight sent:" + str(total_sent_weight))
        package_sent += 1
        print(f"Leftover weight:  {Item_weight}")
        package_weight = Item_weight
        Unused_capcity = int(20 - package_weight)
       
    
    if Unused_capcity > max_unused_capacity:
        max_unused_capacity = Unused_capcity
        package_with_most_empty_space = package_sent

print(package_weight)
if package_weight >0:
    count_packages += 1
print(f"Sent packages: {count_packages}")
print(f"Sent weight: {total_sent_weight}")
print(f"Package with most empty space:  {package_with_most_empty_space}")
print("Thank you! Good Bye")