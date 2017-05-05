#Pam Hart RevBayes Species Tree attempt
#Comment: Unfinished due to error in BirthDeath function

> data_nd2 <- readDiscreteCharacterData("Desktop/Tsub_ND2_Alignment.nex")
   Successfully read one character matrix from file 'Desktop/Tsub_ND2_Alignment.nex'
> data_s7 <- readDiscreteCharacterData("Desktop/Tsub_S7_Alignment.nex") 
   Successfully read one character matrix from file 'Desktop/Tsub_S7_Alignment.nex'
> data <- concatenate(data_nd2, data_s7)
> data

   DNA character matrix with 107 taxa and 1887 characters
   ======================================================
   Origination:                   Tsub_ND2_Alignment.nex
   Number of taxa:                107
   Number of included taxa:       107
   Number of characters:          1887
   Number of included characters: 1887
   Datatype:                      DNA

> data.ntaxa()
   107
> taxa <- data.ntaxa()
> num_loci = data.size()
> n_species <- data.ntaxa()    
> n_branches <- 2 * n_species - 1 # number of branches in a rooted tree
> mi = 0
> speciation ~ dnGamma(2,2)
> relativeExtinction ~ dnBeta(1,1)
> extinction := speciation * relativeExtinction
> root ~ dnNormal(mean=6,sd=2.5,min=0.0, max=Inf)
> moves[++mi] = mvSlide(speciation,delta=1,tune=true,weight=2)
> moves[++mi] = mvSlide(relativeExtinction,delta=1,tune=true,weight=2)
> moves[++mi] = mvScale(speciation,lambda=1,tune=true,weight=2)
> moves[++mi] = mvScale(relativeExtinction,lambda=1,tune=true,weight=2)
> moves[++mi] = mvSlide(root,delta=1,tune=true,weight=0.2)
> sampling_fraction <- 107 / 107 # 107 out of the ~ 107 individuals
> a=speciation, mu=extinction, rootAge=root, rho=sampling_fraction, taxa=taxa )
   Error:	Argument or label mismatch for function call 'dnBDP' with arguments ( RealPos<stochastic> 'lambda', RealPos<deterministic> 'mu', RealPos<stochastic>
   'rootAge', RealPos<constant> 'rho', Natural<constant> 'taxa' ).
   Correct usage is:
   dnBirthDeath (RealPos<any> lambda,
                 RealPos<any> mu,
                 RealPos<any> rootAge,
                 Probability<any> rho,
                 String<any> samplingStrategy {valid options: "uniform"|"diversified"},
                 String<any> condition {valid options: "time"|"survival"|"nTaxa"},
                 Taxon[]<any> taxa,
                 Clade[]<any> incompleteClades)
> psi ~ dnBDP(lambda=speciation, mu=extinction, rootAge=root, rho=sampling_fraction, taxa=taxa)
   Error:	Argument or label mismatch for function call 'dnBDP' with arguments ( RealPos<stochastic> 'lambda', RealPos<deterministic> 'mu', RealPos<stochastic>
   'rootAge', RealPos<constant> 'rho', Natural<constant> 'taxa' ).
   Correct usage is:
   dnBirthDeath (RealPos<any> lambda,
                 RealPos<any> mu,
                 RealPos<any> rootAge,
                 Probability<any> rho,
                 String<any> samplingStrategy {valid options: "uniform"|"diversified"},
                 String<any> condition {valid options: "time"|"survival"|"nTaxa"},
                 Taxon[]<any> taxa,
                 Clade[]<any> incompleteClades)
> psi ~ dnBirthDeath(lambda=speciation, mu=extinction, rootAge=root, rho=sampling_fraction, taxa=taxa)
   Error:	Argument or label mismatch for function call 'dnBirthDeath' with arguments ( RealPos<stochastic> 'lambda', RealPos<deterministic> 'mu',
   RealPos<stochastic> 'rootAge', RealPos<constant> 'rho', Natural<constant> 'taxa' ).
   Correct usage is:
   dnBirthDeath (RealPos<any> lambda,
                 RealPos<any> mu,
                 RealPos<any> rootAge,
                 Probability<any> rho,
                 String<any> samplingStrategy {valid options: "uniform"|"diversified"},
                 String<any> condition {valid options: "time"|"survival"|"nTaxa"},
                 Taxon[]<any> taxa,
                 Clade[]<any> incompleteClades)
