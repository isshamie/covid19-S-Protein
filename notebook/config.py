import pathlib
import os
from dotenv import load_dotenv
from dotenv.main import dotenv_values


## Get the project directory
path = os.path.abspath(__file__)
dir_path = pathlib.Path(os.path.dirname(path))
ROOT_DIR = dir_path.parents[0]
print(f"Project Directory: {ROOT_DIR}")


############
# Head directories to be used
############
DATA_DIR = os.path.join(ROOT_DIR, "data")
RESULTS = os.path.join(DATA_DIR, "processed")
#RESULTS_DIR = os.path.join(ROOT_DIR, "models")
FIGURES_DIR = os.path.join(ROOT_DIR, "figures")
CONTACT_FIGURES_DIR = os.path.join(FIGURES_DIR, "contact")
FIG_NET_DIR = os.path.join(FIGURES_DIR,"networks")
PIPELINE_F = os.path.join(ROOT_DIR, "reports/pipeline/Pipeline.xlsx")
DATA_FIG_DIR = os.path.join(DATA_DIR, "processed/figures")
PARAMS_DIR = os.path.join(ROOT_DIR, "parameters")
TEST_DIR = os.path.join(ROOT_DIR, "tests")
NUM_CORES = 32



############
# Create necessary directories
############

dirs = [DATA_DIR, RESULTS, FIGURES_DIR, FIG_NET_DIR, DATA_FIG_DIR, TEST_DIR,CONTACT_FIGURES_DIR]
for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)



########################
# User files
########################



############
# Annotation and gene information
############

UNIPROT_MAP = os.path.join(DATA_DIR,
                         "external/biomart/mart_export_uniprot.txt")
GENE_MAP = os.path.join(DATA_DIR, "external/biomart/mart_export.txt")

SECM_ANNO = os.path.join(DATA_DIR, "external/secretory_annotations/SM_feizi.tsv")
SECP_ANNO = os.path.join(DATA_DIR,
                         "external/secretory_annotations/SP_feizi.tsv")

NETWORKS_DIR = "/data/isshamie/Secretory_Modeling/Databases/preprocessed/"
NETWORKS_EXAMPLE_DIR = os.path.join(DATA_DIR,
                                    "external/networks/examples")
#PREPPI_PREDICTION = os.path.join(DATA_DIR,
# "external/preppi/human.c600.sm.hc")
PREPPI_PREDICTION = "/data/isshamie/Secretory_Modeling" \
                  "/Databases/preprocessed/preppi_sm600.tsv"

# print(f"DATA_DIR: {DATA_DIR}")
# print(f"RESULTS_DIR: {RESULTS_DIR}")
# print(f"FIGURES_DIR: {FIGURES_DIR}")


print("\nConfig paths:")
for name, value in globals().copy().items():
    if type(value) == str:
        print(name, value)

##################################
# .env variables
##################################
# Look in directories above for .env file
# ROOT_DIR = os.getenv("ROOT_DIR")
load_dotenv()
EMAIL = os.getenv("EMAIL")


PATH_DICT = dotenv_values()
if len(PATH_DICT) > 0:
    print("Hidden parameters to load:")
    for d in PATH_DICT:
        print(d)






