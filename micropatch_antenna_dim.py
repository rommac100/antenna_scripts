# Formulas from Constantine A. Balanis - Antenna Theory_ Analysis and Design
# Rather great Antenna Textbook that has good reference material

import math
class micropatch:
    def __init__(self):
        self.c = 299792458 # speed of light

        self.freq = 10*10**9 # operating/resonant frequency
        self.er = 2.2 # dielectric constant
        self.h = .1588*10**-2 # height of dielectric

    def approximate_calc(self):
        w = ((velocity)/(2*self.freq)*math.sqrt(2/(self.er+1)))
        e_eff = ((self.er+1)/2)+((self.er-1)/2)*(1+12*self.h/w)**(-0.5)
        print(e_eff)
        delta_l = self.h*(0.412*((e_eff+.3)*((w/self.h)+0.264))/((e_eff-.258)*((w/self.h)+0.8)))
        print(delta_l)
        wavelength = velocity/(self.freq*math.sqrt(e_eff))
        l = wavelength/2 - 2*delta_l
        l_eff = l+2*delta_l
        print("L = %f, W = %f, E_eff = %f, L_eff = %f"%(l,w,e_eff,l_eff))
        return (l,w,e_eff,l_eff)

if __name__ == '__main__':
    micropatch = micropatch()
    (l,w,e_eff,l_eff) = micropatch.approximate_calc()
