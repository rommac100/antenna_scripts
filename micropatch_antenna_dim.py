# Formulas from Constantine A. Balanis - Antenna Theory_ Analysis and Design
# Rather great Antenna Textbook that has good reference material

import math
class micropatch:
    def __init__(self):
        self.c = 299792458 # speed of light

        self.freq = 2.4*10**9 # operating/resonant frequency
        self.er = 4.6 # dielectric constant
        self.h = .93*10**-3 # height of dielectric

    def approximate_calc_dim(self):
        velocity = self.c
        w = ((velocity)/(2*self.freq)*math.sqrt(2/(self.er+1)))
        e_eff = ((self.er+1)/2)+((self.er-1)/2)*(1+12*self.h/w)**(-0.5)
        print(e_eff)
        delta_l = self.h*(0.412*((e_eff+.3)*((w/self.h)+0.264))/((e_eff-.258)*((w/self.h)+0.8)))
        print(delta_l)
        wavelength = velocity/(self.freq*math.sqrt(e_eff))
        l = wavelength/2 - 2*delta_l
        l_eff = l+2*delta_l

        self.w = w
        self.e_eff = e_eff
        self.delta_l = delta_l
        self.l = l
        self.l_eff = l_eff

        self.g_l = self.l+self.h*6
        self.g_w = self.w+self.h*6
        print("L = %f, W = %f, E_eff = %f, L_eff = %f, g_l = %f, g_w =%f"%(l,w,e_eff,l_eff,self.g_l,self.g_w))
        return (l,w,e_eff,l_eff)
    def approximate_calc_imped_res(self):
        r_in = 90*(self.er)**2/(self.er-1)*(self.l/self.w)
        return r_in
        print("calc_imped")

if __name__ == '__main__':
    micropatch = micropatch()
    (l,w,e_eff,l_eff) = micropatch.approximate_calc_dim()
    print(micropatch.approximate_calc_imped_res())

