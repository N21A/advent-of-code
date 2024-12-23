%{
aoc2015_01.m
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2015 Day 1: "Not Quite Lisp
%}

% Read input.txt
fid = fopen('input.txt', 'r');

% Initialise arrays
basement_positions = [];

% Initialise variables
floor_counter = 0;
position = 0;
first_basement = 0;

% Read each character into the array
sequence = fread(fid, '*char')';

for i = 1:length(sequence)
    
    position = position + 1;
    
    if sequence(i) == '('
        floor_counter = floor_counter + 1;
    elseif sequence(i) == ')'
        floor_counter = floor_counter - 1;
    end
    
    if floor_counter == -1
        basement_positions(end+1) = position;
    end
end

% Find the first occurrence of Santa entering the basement
first_basement = basement_positions(1);

% Display Santa's final floor number
floor_counter

% Display the first occurrence of Santa entering the basement
first_basement

% Close the file
fclose(fid);