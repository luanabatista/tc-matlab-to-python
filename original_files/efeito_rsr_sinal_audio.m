clear all
close all

nPower = 0.0001;
temp_Rep = 100;

[x Fs] = audioread("Pe-na-Areia.wav");
x = x(1:temp_Rep*Fs,1);

n = sqrt(nPower)*randn(temp_Rep*Fs,1);

xCorrupt = x + n;

soundsc(x,Fs);
soundsc(xCorrupt,Fs);

Ps = mean(x.^2);
Pn = var(n);

RSR = Ps/Pn;

