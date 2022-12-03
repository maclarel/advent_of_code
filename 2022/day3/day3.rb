#!/usr/bin/env ruby
#frozen_string_literal: true

require 'set'

input_file = "input.txt" 

sum = 0

def assign_score(letter)
  # Assign a score to each letter
  # a = 1, b = 2, c = 3, etc.
  # A = 27, B = 28, C = 29, etc.
  if letter == letter.upcase
    letter.ord - 64 + 26
  else
    letter.ord - 96
  end
end

# Stage 1

File.open(input_file).each do |line|
  # Split the line into two sets of equal length
  line1 = line[0..(line.length/2-1)].split("").to_set
  line2 = line[(line.length/2)..-1].split("").to_set
  # Get the intersection of the two sets and print it
  sum += assign_score(line1.intersection(line2).to_a.join)
end

puts "Stage 1 - Sum of scores: #{sum}"

# Stage 2
stage2_sum = 0
stage2data = []

File.open(input_file).each do |line|
  stage2data << line
end

stage2data.each_slice(3) do |slice|
  line1 = slice[0].split("").to_set
  line2 = slice[1].split("").to_set
  line3 = slice[2].split("").to_set
  # Get the intersection of the two sets and print it
  stage2_sum += assign_score(line1.intersection(line2.intersection(line3)).to_a.join)
end

puts "Stage 2 - Sum of scores: #{stage2_sum}"
