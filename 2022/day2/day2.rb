#!/usr/bin/ruby

# Frozen string literal: true

# Parse input
input_file = "input.txt"


def rps_score(opponent_choice, player_choice)
  round_score = 0

  # Points for choice
  if player_choice == "X"
    round_score += 1
  elsif player_choice == "Y"
    round_score += 2
  elsif player_choice == "Z"
    round_score += 3
  end

  # Points for winning
  if player_choice == "X" && opponent_choice == "C"
    round_score += 6
  elsif player_choice == "Y" && opponent_choice == "A"
    round_score += 6
  elsif player_choice == "Z" && opponent_choice == "B"
    round_score += 6
  end

  # Points for tie/loss
  if player_choice == "X" && opponent_choice == "A"
    round_score += 3
  elsif player_choice == "Y" && opponent_choice == "B"
    round_score += 3
  elsif player_choice == "Z" && opponent_choice == "C"
    round_score += 3
  end
  
  return round_score
end

player_score = 0

File.open(input_file).each do |line|
  opponent_choice, player_choice = line.split(" ")
  player_score += rps_score(opponent_choice, player_choice)
end

puts "Stage 1 - #{player_score}"

# Stage 2

def make_choice(opponent_choice, desired_outcome)
  round_score = 0

  if desired_outcome == "Z" # Win
    if opponent_choice == "A"
      return "Y"
    elsif opponent_choice == "B"
      return "Z"
    else
      return "X"
    end
  elsif desired_outcome == "Y" # Tie
    if opponent_choice == "A"
      return "X"
    elsif opponent_choice == "B"
      return "Y"
    else
      return "Z"
    end
  elsif desired_outcome == "X" # Lose
    if opponent_choice == "A"
      return "Z"
    elsif opponent_choice == "B"
      return "X"
    elsif opponent_choice == "C"
      return "Y"
    end
  end
end

player_score = 0

File.open(input_file).each do |line|
  opponent_choice, desired_outcome = line.split(" ")
  player_score += rps_score(opponent_choice, make_choice(opponent_choice, desired_outcome))
end

puts "Stage 2 - #{player_score}"
