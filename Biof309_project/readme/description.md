The purpose of this script:

Start with the VDJ filtered_contig_annotation.csv output file from 10X genomics in the results folder:

Filter/cleanup according to the following criteria:
- Remove all sequences without a cdr3, are unproductive, or don't represent HC, LC, KC
- Remove all cells (represented by barcodes) with duplicate HC, KC, LC
- Only keep cells (barcodes) that have a HC, may or may not have a KC or LC
- Add a column containing the character length of the HC cdr3 column

Then two files are generated:

First:
- Remove all cells where a HC is paired with both a KC and LC, so all cells should now have two chains: one HC, and either a KC or LC
- Output into the results folder a csv file listing counts from the v_gene, d_gene, j_gene, c_gene columns for each chain for downstream analysis

Second:
- Multi-index and unstack the data frame based on the chain column so that the HC/KC/LC associated with one cell (barcode) are all on the same row
- Output into the results folder as a csv file this dataframe with columns of interest for downstream analysis

    
