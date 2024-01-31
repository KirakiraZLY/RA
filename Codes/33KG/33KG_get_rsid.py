from Bio import Entrez

def fetch_rsid(chromosome, position, build="37"):
    Entrez.email = "zly@qgg.au.dk"

    query = f"{chromosome}:{position}[{build}]"
    handle = Entrez.esearch(db="snp", term=query)
    record = Entrez.read(handle)
    count = int(record["Count"])
    if count > 0:
        snp_id = record["IdList"][0]
        handle = Entrez.efetch(db="snp", id=snp_id, rettype="json", retmode="text")
        snp_record = Entrez.read(handle)

        rsid = snp_record[0]["refsnp_id"]
        return rsid
    else:
        return None

chromosome_list = ["1", "2", "3"]
position_list = ["86028", "143169387", "103575958"]

for chrom, pos in zip(chromosome_list, position_list):
    rsids = fetch_rsid(chrom, pos)
    if rsids:
        print(f"Chromosome {chrom}, Position {pos}: RSIDs - {rsids}")
    else:
        print(f"Chromosome {chrom}, Position {pos}: No RSID found")
