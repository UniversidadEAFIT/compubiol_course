## Hacer los BLAST ##

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

# Hace el blast de la secuencia trimada y devuelve un parse (objeto organizado) del BLAST
def buscarSecuenciaEnBasesRemotas(secuencia):
    result_handle = NCBIWWW.qblast("blastn", "nt", secuencia)
    return NCBIXML.parse(result_handle)

# Extraer la información requerida del parse BLAST
def infoBLAST (blast_records):
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                nombre = alignment.title.partition('gb|')[2].partition('|')[2]
                accesion = alignment.title.partition('gb|')[2].partition('|')[0]
                evalue = hsp.expect
                identidad = (hsp.positives/hsp.align_length)*100
            break
    return [accesion,nombre,evalue,identidad]


# Hace el blast y me devuelve la información requerida
def BLAST_e_info (secuencia):
    blast_records = buscarSecuenciaEnBasesRemotas(secuencia)
    return infoBLAST(blast_records)