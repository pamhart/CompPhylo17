### RevBayes GTR+I+G model phylogenetic hypothesis for *Typhlichthys subterraneus* ###
#### Pamela Hart ####
##### Computational Phylogenetics Spring 2017 Final Assignment #####

#### Methods ####
I inferred phylogenetic relationships within the order Percopsiformes utilizing a mitochondrial gene dataset. Novel NADH Dehydrogenase subunit 2 (nd2) sequences and sequences from GenBank were utilized to develop Bayesian phylogenetic hypotheses. 9 sequences were used in the analysis, each a single representative for the species in the order. Tree topology and posterior probabilities were estimated in RevBayes v.1.0.4 (Hohna et al. 2016). For phylogenetic tree generation, a GTR+I+G model was selected. Two independent replicate runs were performed, each with five hundred thousand iterations under default settings.  Approximately, the first fifty thousand generations (10%) were discarded as burn-in.  Following analysis, the phylogenetic trees for each replicate were visualized using FigTree v.1.4.2. Additionally, I visualized and estimated convergence of the replicates with Tracer v.1.6.0.

#### Results ####
Bayesian phylogenies generated from both replicate runs in RevBayes were concordant (Fig. 1 and 2). Values for convergence and mixing were also consistent for both replicate runs (Fig. 3 and 4). 

![image](RevBayes_run1_nd2.pdf)
Figure 1. Bayesian nd2 phylogeny for the Percopsiformes replicate run one.

![image](RevBayes_run2_nd2.pdf)
Figure 2. Bayesian nd2 phylogeny for the Percopsiformes replicate run two.

![image](RevBayes_tracer_table.pdf)
Figure 3. Convergence and mixing quantification values of the replicate RevBayes runs.

![image](RevBayes_tracer_convergence.pdf)
Figure 4. Convergence visualization plot for replicate RevBayes runs.

#### References ####
Höhna, M.J. Landis, T.A. Heath, B. Boussau, N. Lartillot, B.R. Moore, J.P. Huelsenbeck, F. Ronquist (2016). RevBayes: Bayesian Phylogenetic Inference Using Graphical Models and an Interactive Model-Specification Language. Systematic Biology 65 (4): 726-736.
