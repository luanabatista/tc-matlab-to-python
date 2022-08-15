clear all
close all
pkg load communications

global sound_play_utility = 'aplay';
%graphics_toolkit('fltk');

b = 1;
delta = 2/(2^b - 1);
temp_Rep = 20;

[x Fs] = audioread("Pe-na-Areia.wav");
%soundsc(x,Fs);
x = x(1:temp_Rep*Fs,1);

[xq,integercodeword,indices] = quantiz(x,delta,b);

soundsc(xq,Fs);

hold on
plot(x(17000:20000),'LineWidth',2,'b+');
plot(xq(17000:20000),'LineWidth',2,'k');
plot(x(17000:20000) - xq(17000:20000),'LineWidth',2,'r');
grid
