
################################################################################
#
# This script can be used in activity 2.
#
# This script was adapted from: https://github.com/sergeitarasov/PhenoScript/wiki/Quick-start
#
# Last update: 18.nov.2025
#
# Before you start make sure you have your enviroment properly set up and available in VS Code!
#
################################################################################

# Import all libraries.
from phenospy import *
import os

# Get the current directory.
current_dir = os.getcwd()

# Set arguments.
phs_file = os.path.join(current_dir, 'phenotypes_model.phs') # input file name
yaml_file = os.path.join(current_dir, 'phs-config.yaml') # configuration file name
save_dir = os.path.join(current_dir, 'output/') # output folder name (you need to create this!)
save_pref = 'phenotypes' # output file name

# Convert PHS to OWL and XML.
phsToOWL(phs_file, yaml_file, save_dir, save_pref)

# Convert OWL to Markdown.
# Get owl file.
owl_file = os.path.join(save_dir, save_pref + '.owl')

# Make NL graph.
onto = owlToNLgraph(owl_file)

# Convert NL graph to Markdown.
taxon = 'organism_1'
file_md = os.path.join(current_dir, save_dir, 'phenotypes.md')
ind0 = onto.search(label = taxon)[0]
NLgraphToMarkdown(onto, ind0, file_save = file_md, verbose = False)
