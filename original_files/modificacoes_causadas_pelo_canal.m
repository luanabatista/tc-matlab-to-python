clear
clc

sqrWave = [ones(1,10) zeros(1,10) ones(1,10) zeros(1,10) ones(1,10) zeros(1,10)];

nP = 0.1;
corruptType = 0; % 0: noise
                % 1: atenuation
                % 2: distortion

switch(corruptType)
  case 0
    y = sqrWave + sqrt(nP)*randn(1,length(sqrWave));

  case 1
    y = 0.5*sqrWave;

  case 2
    y = conv(sqrWave,0.4*[0.2 0.3 0.5 0.4 0.35 0.31 0.27]);
endswitch

hold
plot(sqrWave,"linewidth",2);
plot(y,'r--',"linewidth",2);
