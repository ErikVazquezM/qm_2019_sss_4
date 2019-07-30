# initialized with a gas type
class NobleGasModel:
    def __init__(self, gas_type):
        """Creates an instance of the class for a given gas type

        Parameters
        ----------
        gas_type : string
            Defines the gas type in the system (out of Ar or Ne)
        """
        if isinstance(gas_type, str):
            self.gas_type = gas_type
        else:
            raise TypeError("Name should be a string!")

        if (self.gas_type.lower() == "ar" or self.gas_type.lower() == "argon"):
            self.model_parameters = {
            'r_hop' : 3.1810226927827516,
            't_ss' : 0.03365982238611262,
            't_sp' : -0.029154833035109226,
            't_pp1' : -0.0804163845390335,
            't_pp2' : -0.01393611496959445,
            'r_pseudo' : 2.60342991362958,
            'v_pseudo' : 0.022972992186364977,
            'dipole' : 2.781629275106456,
            'energy_s' : 3.1659446174413004,
            'energy_p' : -2.3926873325346554,
            'coulomb_s' : 0.3603533286088998,
            'coulomb_p' : -0.003267991835806299
            }

        elif (self.gas_type.lower() == "ne" or self.gas_type.lower() == "neon"):
            self.model_parameters = {
            'coulomb_p': -0.010255409806855187,
            'coulomb_s': 0.4536486561938202,
            'dipole': 1.6692376991516769,
            'energy_p': -3.1186533988406335,
            'energy_s': 11.334912902362603,
            'r_hop': 2.739689713337267,
            'r_pseudo': 1.1800779720963734,
            't_pp1': -0.029546671673199854,
            't_pp2': -0.0041958662271044875,
            't_sp': 0.000450562836426027,
            't_ss': 0.0289251941290921,
            'v_pseudo': -0.015945813280635074
            }

        else:
            raise TypeError("Noble Gas Model Not Supported! Ar, Argon, Ne and Neon expected")

        self.ionic_charge = 6

        self.orbital_types = ['s', 'px', 'py', 'pz']

        self.orbitals_per_atom = len(self.orbital_types)

        self.p_orbitals = ['px', 'py', 'pz']

        self.vec = { 'px':[1,0,0], 'py':[0,1,0], 'pz':[0,0,1] }

        self.orbital_occupation = {'s':0, 'px':1, 'py':1, 'pz':1}


    def ao_index(self, atom_p, orb_p):
        """
	Returns the index of the atomic orbital based on the index of atom and orbital type
	
        Parameters
        ----------
        atom_p : integer
	       index of the atom where the orbital centers
        orb_p : string
	       The type of the orbital out of 's', 'px', 'py', 'pz'

        Returns
        -------
        p : integer
	       The index of the orbital based on the atom number and the orbital type
        """
        p = atom_p * self.orbitals_per_atom
        p += self.orbital_types.index(orb_p)

        return p

    def atom(self, ao_index):
        """
        Returns the atom index part of an atomic orbital index

        Parameters
        ----------
        ao_index : integer
	       It is the index assigned to a particular orbital in the system

        Returns
        -------
        atom_num : integer
	       The atom number to which the orbital associated with the given atomic index belongs
        """

        return ao_index // self.orbitals_per_atom


    def orb(self, ao_index):
        """
        Returns the orbital type of an atomic orbital index

        Parameters
        ----------
        ao_index : integer
	       It is the index assigned to a particular orbital in the system

        Returns
        -------
        orbital_type : string
    	   It returns the type of the orbital based on the atomic index as a string out of 's', 'px', 'py', 'pz'
        """

        orb_index = ao_index % self.orbitals_per_atom
        orb_type = self.orbital_types[orb_index]
        return orb_type
