# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"1354009","system":"gprdproduct"},{"code":"1354010","system":"gprdproduct"},{"code":"1976009","system":"gprdproduct"},{"code":"2281009","system":"gprdproduct"},{"code":"2281011","system":"gprdproduct"},{"code":"2906009","system":"gprdproduct"},{"code":"2906011","system":"gprdproduct"},{"code":"3166009","system":"gprdproduct"},{"code":"3166011","system":"gprdproduct"},{"code":"4351007","system":"gprdproduct"},{"code":"4758009","system":"gprdproduct"},{"code":"4782001","system":"gprdproduct"},{"code":"4782003","system":"gprdproduct"},{"code":"635010","system":"gprdproduct"},{"code":"635011","system":"gprdproduct"},{"code":"636009","system":"gprdproduct"},{"code":"636011","system":"gprdproduct"},{"code":"8780001","system":"gprdproduct"},{"code":"8780003","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-fentamox---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-fentamox---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-fentamox---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
