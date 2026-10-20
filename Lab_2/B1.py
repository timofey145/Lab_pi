def file_info(filename):
    with open(filename, "r") as file:
        line = file.readline()
        cut = line.split()
        scl = float(cut[1])
        line_1 = file.readline()
        dis1 = float(line_1)
        line_2 = file.readline()
        dis2 = float(line_2)
        line_3 = file.readline()
        dis3 = float(line_3)
        line_4 = file.readline()
        dis4 = float(line_4)

        res1 = dis1 * scl
        res2 = dis2 * scl
        res3 = dis3 * scl
        res4 = dis4 * scl

        total_dis = res1 + res2 + res3 + res4

        print("Dwight Barnette")
        print("Simple Map Distance Computations")
        print()
        print("Map Scale Factor: 0.25 miles per inch")
        print()
        print("       Map           Measure")
        print("       Mileage       Distance")
        print("=========================================")
        print (f"#\t 1 \t {dis1} \t      {res1:.1f}")
        print (f"#\t 2 \t {dis2} \t      {res2:.1f}")
        print (f"#\t 3 \t {dis3} \t      {res3:.1f}")
        print (f"#\t 4 \t {dis4} \t      {res4:.1f}")
        print ("=========================================")
        print (f"Total Distance:      {total_dis:.1f} miles")
        print("\n")

file_info("inmap0.dat")
file_info("inmap1.dat")
file_info("inmap2.dat")



