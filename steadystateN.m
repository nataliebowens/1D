% Steady state calculation of N(x)
load Nice.dat
Nx = length(Nice);
x = Nice(:,1);
Nice_numerical = Nice(:,2)
p = polyfit(x,Nice_numerical,2);
c0 = p(3);
c1 = p(2);
c2 = p(1);
figure(1)
plot (...
    x,Nice_numerical, ...
    x,c0 + c1*x+ c2*x.^2)
set (gca,'fontsize',16)
title('Nice')

S0 = 2;
alpha_terr = .2
alpha_edge = 1.0
k = S0*alpha_terr;
f = 0.8;
L = 501;
S=S0*f+x.^2*S0*(1-f)/L^2;
alpha_eff = k./S;

Nice_numerical_p = c1 + 2*c2*x;
figure(3)
plot(x,Nice_numerical_p)
set (gca,'fontsize',16)
title('N''')


b = (alpha_eff(1)-alpha_terr)/Nice_numerical_p(1)
alpha_eff_test = alpha_terr + b*Nice_numerical_p;


syms f_sym x_sym L_sym alpha_terr_sym
alpha_eff_sym = alpha_terr_sym/(f_sym+x_sym^2*(1-f_sym)/L_sym^2);
pretty(simple(alpha_eff_sym))
alpha_eff_sym_T = taylor(alpha_eff_sym,x_sym,6);
pretty(alpha_eff_sym_T)

c = (f-1)/(L^2*f^2)*alpha_terr/(4*c2^2)
b = -2*c*c1
a = alpha_terr/f -b*c1 -c*c1^2

alpha_eff_test2 = a + b*Nice_numerical_p + c*Nice_numerical_p.^2

figure(2)
plot(...
    x,alpha_eff, ...
    x,alpha_eff_test, ...
    x,alpha_eff_test2, ...
    'linewidth',2)
set (gca,'fontsize',16)
title('\alpha_{eff}')


return

L = 499
Nx = 500
x = linspace(0,L,Nx);
xm = 10
f = 0.8;
beta = (1-f)/f;
alpha_terr = .2
alpha_edge = 1
S0 = 1;
k = S0*alpha_terr;
S=S0*f+x.^2*S0*(1-f)/L^2;
alpha_eff = k./S;

subplot(3,1,1)
plot(x,S)
subplot(3,1,2)
plot(x,alpha_eff)

N = alpha_terr/alpha_edge*(atan(beta^(1/2)) - atan(beta^(1/2)*x/L))/(beta^(1/2)*f*xm/L);
%plot(x,N)