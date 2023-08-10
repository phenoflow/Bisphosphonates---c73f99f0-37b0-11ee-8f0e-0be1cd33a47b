# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"11039001","system":"gprdproduct"},{"code":"12066001","system":"gprdproduct"},{"code":"12067001","system":"gprdproduct"},{"code":"12393001","system":"gprdproduct"},{"code":"12394001","system":"gprdproduct"},{"code":"1328001","system":"gprdproduct"},{"code":"135001","system":"gprdproduct"},{"code":"137001","system":"gprdproduct"},{"code":"13920001","system":"gprdproduct"},{"code":"13923001","system":"gprdproduct"},{"code":"14259001","system":"gprdproduct"},{"code":"14260001","system":"gprdproduct"},{"code":"1472002","system":"gprdproduct"},{"code":"3095001","system":"gprdproduct"},{"code":"3865001","system":"gprdproduct"},{"code":"441003","system":"gprdproduct"},{"code":"4652003","system":"gprdproduct"},{"code":"4695001","system":"gprdproduct"},{"code":"4695003","system":"gprdproduct"},{"code":"6597003","system":"gprdproduct"},{"code":"6771001","system":"gprdproduct"},{"code":"6771002","system":"gprdproduct"},{"code":"7914001","system":"gprdproduct"},{"code":"8001001","system":"gprdproduct"},{"code":"8002001","system":"gprdproduct"},{"code":"8466001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-injsoln---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-injsoln---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-injsoln---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
