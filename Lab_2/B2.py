def file_info(filename, filename2):
    sum_air = 0
    float(sum_air)
    total_air = 0
    int(total_air)

    with open(filename, "r") as file:
        all_lines = file.readlines()
    with open(filename2, "a") as file_2:
        file_2.write(" Time            WC temp \t      WC Effect\n")
        file_2.write("---------------------------------------------------\n")
        for i in range(2, len(all_lines)):
            line_1 = all_lines[i]
            line1_air = line_1.split()
            if not line1_air:
                continue
            line1_air = float(line1_air[1])
            line1_speed = line_1.split()
            line1_speed = float(line1_speed[2])
            line1_time = line_1.split()
            line1_time = str(line1_time[0])

            res = 35.74 + 0.6125 * line1_air + (0.4275 * line1_air - 35.75) * pow(line1_speed, 0.16)
            res = float(res)
            res = f"{res:.1f}"
            res_wc = float(res) - line1_air
            res_wc = f"{res_wc:.1f}"
            sum_air += float(res)
            total_air += 1
            file_2.write(f"{line1_time:<18}{res:<12}\t{res_wc:<12}\n")

        res_air = sum_air / total_air
        res_air = f"{res_air:.1f}"
        file_2.write("---------------------------------------------------\n")
        file_2.write(f"The average adjusted temperature based on {total_air} observations, was {res_air}")


file_info("1.WCData.txt", "1.WindChillReport.txt")
file_info("2.WCData.txt", "2.WindChillReport.txt")
file_info("3.WCData.txt", "3.WindChillReport.txt")