%patch_antenna_calcs
% All equations are from balanis
er = 2.2;
% 1oz copper = 35um
H_total_mm = 1.6; %
cu_thickness_um = 35;
c = 2.99792458*10^8;
er_0 = 8.85418782*10^-12;
meu_0 = 1.25663706*10^-6;
%H = H_total_mm*10^-3-(cu_thickness_um)*2*10^-6 % assuming two layer with 35 um. Adjust as needed.
H = .1588*10^-2;
f_center = 10*10^9; % 10GHz
1.1
W = (c/(2*f_center))*sqrt(2/(er+1))


er_eff = ((er+1)/2) + ((er-1)/2)*(1+12*(H/W))^-.5

delta_l = .412*H*(er_eff+.3)*(W/H+.264)/((er_eff-.258)*(W/H+.8))
L = 1/(2*f_center*sqrt(er_eff)*sqrt(er_0*meu_0))-2*delta_l


% Inset Feed Position Calculations:
%Making rough assumption thickness of substrate is less than wavelength by a bit. Probably not valid here but oh well.
lambda_0 = c/f_center;
k_0 = 2*pi/lambda_0;

f_i1 = @(x) (sin(k_0*W/2*cos(x))/cos(x))^2*(sin(x))^3;

i1 = quad(f_i1,0,pi)
g1_exact = i1/(120*pi^2)

g1 = 1/120*(W/lambda_0)
f_g12 = @(x) (sin(k_0*W/2*cos(x))/cos(x))^2*besselj(0,k_0*L*sin(x))*(sin(x))^3
g12 = 1/(120*pi^2)*quad(f_g12,0,pi)

r_in_exact = 1/(2*(g1_exact+g12))

y_inset = acos(sqrt(50/r_in_exact))*L/pi





