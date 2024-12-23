%{
aoc2024_02.m
----------------
Author: Nida Anis
Date: 22/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 2: "Red-Nosed Reports"
%}

% Import data from input.txt
fid = fopen('input.txt', 'r');

% Initialise a cell array to store reports
reports = {};

% Initialise the safe_reports variable
safe_reports = 0;

% Read the file line by line
line = fgetl(fid);
while ischar(line)
    % Split each report into numbers and convert to a numeric array
    numbers = sscanf(line, '%d')';
    
    % Append the numeric array to the cell array
    reports{end+1} = numbers;
    
    % Read the next line
    line = fgetl(fid);
end

% Close the file
fclose(fid);

% For each report in reports:
for i = 1:length(reports)
    % Access the i-th report
    report = reports{i};
    
    % Calculate the differences
    differences = diff(report);
    
    % 01: Check for a consistent increase or decrease
    is_increasing = all(differences > 0);
    is_decreasing = all(differences < 0);
    
    % 02: Check if differences are within the valid range
    valid_differences = all(abs(differences) >= 1 & abs(differences) <= 3);
    
    if valid_differences && (is_increasing || is_decreasing)
        safe_reports = safe_reports + 1;
        
    else
        % 03: Use the Problem Dampener
        for j = 1:length(report)
            problem_dampener = report([1:j-1, j+1:length(report)]);
            differences = diff(problem_dampener);
            
            % 03.01: Check for a consistent increase or decrease
            is_increasing = all(differences > 0);
            is_decreasing = all(differences < 0);
            
            % 03.02: Check if differences are within the valid range
            valid_differences = all(abs(differences) >= 1 & abs(differences) <= 3);
            
            if valid_differences && (is_increasing || is_decreasing)
                safe_reports = safe_reports + 1;
                break
            end
        end
    end
end

safe_reports
        