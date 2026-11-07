def file_info(filename):
    with open(filename, "r") as file:
        line = file.readline()
        cut = line.split()
        scl = float(cut[1])

        total_dis = 0
        count = 0

        print("Dwight Barnette")
        print("Simple Map Distance Computations")
        print()
        print("Map Scale Factor: 0.25 miles per inch")
        print()
        print("       Map           Measure")
        print("       Mileage       Distance")
        print("=========================================")

        for line in file:
            dis = float(line)
            res = dis * scl
            total_dis += res

            print (f"#\t{count}\t {dis} \t      {res:.1f}")

            count += 1

        print ("=========================================")
        print (f"Total Distance:      {total_dis:.1f} miles")
        print("\n")

file_info("inmap0.dat")
file_info("inmap1.dat")
file_info("inmap2.dat")



