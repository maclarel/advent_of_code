#!/usr/bin/env ruby
# frozen_string_literal: true

input_file = "input.txt"

# Track each elf and their carry weight
class Elf
  attr_reader :id, :weight

  def initialize(id)
    @id = id
    @weight = 0
  end

  def add_weight(weight)
    @weight += weight
  end
end

# Create an elf-filled shelf
elves = []

# Create first elf
curr_elf = 0
elves << Elf.new(curr_elf + 1)

File.open(input_file).each do |line|
  if line.length < 2
    curr_elf += 1
    elves << Elf.new(curr_elf + 1)
  else
    elves[curr_elf].add_weight(line.to_i)
  end
end

# Stage 1
puts elves.max_by(&:weight).weight

# Stage 2
elves.sort_by!(&:weight).reverse!
puts elves.first(3).map(&:weight).sum
