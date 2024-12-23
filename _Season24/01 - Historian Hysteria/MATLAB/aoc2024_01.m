%{
aoc2024_01.m
----------------
Author: Nida Anis
Date: 01/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 1: "Historian Hysteria".
%}

% Import data from input.txt
f = importdata('input.txt');

% Declare and sort arrays
col1 = sort(f(:,1));
col2 = sort(f(:,2));

% Declare variables
count = 0

% Calculate distances between array items
for i = 1 : length(col1)
    dists(i) = abs(col1(i)-col2(i));
end

% Sum distances between array items
sum_dists = sum(dists)

% Calculate similarity scores for each left list item
for i = 1 : length(col1)
    for j = 1 : length(col2)
        if col1(i) == col2(j)
            count = count + 1;
        end
    end
    sim_scores(i) = col1(i) * count;
    count = 0;
end

% Sum similarity scores
sum_sims = sum(sim_scores)