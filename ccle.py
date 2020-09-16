#%%
import pandas as pd
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen



# %%

mut = pd.read_csv('/media/hkim/SH/Cancer/CCLE/GI_project/GI_Mutation.txt',sep='\t')

#%%

LIST = []

for idx in mut.index:
    proj = 'GI'
    samp = mut.loc[idx,'DepMap_ID']
    sampID = '.'
    genome = "GRCh38"
    muttype = mut.loc[idx,'Variant_Type']
    chrom = mut.loc[idx,'Chromosome']
    pos = mut.loc[idx,'Start_position']
    end = mut.loc[idx,'End_position']
    ref = mut.loc[idx,'Reference_Allele']
    alt = mut.loc[idx,'Tumor_Seq_Allele1']
    tp = 'SOMATIC'

    eachLine = [proj,samp,sampID,genome,muttype,chrom,pos,end,ref,alt,tp]
    LIST.append(eachLine)

final = pd.DataFrame(LIST, columns=['Project','Sample',	'ID'	,'Genome'	,'mut_type'	,'chrom'	,'pos_start',	'pos_end',	'ref',	'alt',	'Type'])
#%%

final.to_csv('/media/hkim/SH/Cancer/CCLE/Mutation_Signature/input/GI_Mutation_Input.txt',sep='\t',index=None)

#%%


matrices = matGen.SigProfilerMatrixGeneratorFunc('GI', 'GRCh38',
 '/media/hkim/SH/Cancer/CCLE/Mutation_Signature', exome=False, bed_file=None, chrom_based=False, plot=False, tsb_stat=False, seqInfo=False)

# %%
spss.single_sample(df,'/media/hkim/SH/Cancer/CCLE/Mutation_Signature/SingleSample',exome=False,ref='GRCh38')

# %%
sig.sigProfilerExtractor(input_type = 'text', output = '/media/hkim/SH/Cancer/CCLE/Mutation_Signature/Extractor/DBS', input_data='/media/hkim/SH/Cancer/CCLE/Mutation_Signature/output/DBS/GI.DBS78.all',reference_genome='GRCh38',context_type = 'DBS78')
