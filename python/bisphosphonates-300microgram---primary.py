# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"10499001","system":"gprdproduct"},{"code":"10621001","system":"gprdproduct"},{"code":"10622001","system":"gprdproduct"},{"code":"10624001","system":"gprdproduct"},{"code":"10637001","system":"gprdproduct"},{"code":"10658001","system":"gprdproduct"},{"code":"10659001","system":"gprdproduct"},{"code":"10660001","system":"gprdproduct"},{"code":"10704001","system":"gprdproduct"},{"code":"10786001","system":"gprdproduct"},{"code":"10790002","system":"gprdproduct"},{"code":"10917002","system":"gprdproduct"},{"code":"10917003","system":"gprdproduct"},{"code":"11171001","system":"gprdproduct"},{"code":"1147001","system":"gprdproduct"},{"code":"12240001","system":"gprdproduct"},{"code":"12953001","system":"gprdproduct"},{"code":"12955001","system":"gprdproduct"},{"code":"12956001","system":"gprdproduct"},{"code":"13400001","system":"gprdproduct"},{"code":"14652001","system":"gprdproduct"},{"code":"2006001","system":"gprdproduct"},{"code":"2006002","system":"gprdproduct"},{"code":"2006003","system":"gprdproduct"},{"code":"2799009","system":"gprdproduct"},{"code":"3255001","system":"gprdproduct"},{"code":"3560001","system":"gprdproduct"},{"code":"3560002","system":"gprdproduct"},{"code":"397009","system":"gprdproduct"},{"code":"397010","system":"gprdproduct"},{"code":"4659001","system":"gprdproduct"},{"code":"4660001","system":"gprdproduct"},{"code":"4828009","system":"gprdproduct"},{"code":"5483002","system":"gprdproduct"},{"code":"5483003","system":"gprdproduct"},{"code":"5601001","system":"gprdproduct"},{"code":"5601002","system":"gprdproduct"},{"code":"5841002","system":"gprdproduct"},{"code":"704001","system":"gprdproduct"},{"code":"7846002","system":"gprdproduct"},{"code":"8121001","system":"gprdproduct"},{"code":"8379002","system":"gprdproduct"},{"code":"9027001","system":"gprdproduct"},{"code":"9030001","system":"gprdproduct"},{"code":"9030002","system":"gprdproduct"},{"code":"9105001","system":"gprdproduct"},{"code":"9239001","system":"gprdproduct"},{"code":"9249001","system":"gprdproduct"},{"code":"9252001","system":"gprdproduct"},{"code":"9341001","system":"gprdproduct"},{"code":"9345001","system":"gprdproduct"},{"code":"9349001","system":"gprdproduct"},{"code":"9352001","system":"gprdproduct"},{"code":"952001","system":"gprdproduct"},{"code":"9758002","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-300microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-300microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-300microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
