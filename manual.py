


q_list = []
a_list = []
filename = input("csv file name( no .csv ):  ")
while 1:
    q = input("quetion: ")
    a = input("answer:  ")

    if q == "q":
        print("status:")
        print(q_list)
        print(a_list)
        with open(filename + ".csv", "w") as f:
            for i in range(len(q_list)):
                f.write("{}, {}\n".format(q_list[i], a_list[i]))
        break
            
        

    print("q: ", q)
    print("a: ", a)
    q_list.append(q)
    a_list.append(a)

