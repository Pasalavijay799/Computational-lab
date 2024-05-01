clc;
clear all;
close all;
FileId=fopen('sin_t.txt','r');
A=fscanf(FileId,'%f');
fclose(FileId);
f=10;
x=sin(2*pi*f*A);
plot(A,x);
clc;
close all;
x=0:0.01:1;
fileId=fopen('sin_t.txt','w');
fprint(fileId,'%f'x);
fclose(fileId);

