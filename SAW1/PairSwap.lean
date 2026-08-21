namespace SAW1

/-- Exchange the two coordinates of an ordered pair. -/
def coordinateSwap {α β : Type} (p : α × β) : β × α :=
  (p.2, p.1)

/-- Coordinate exchange is an involution: swapping twice restores the pair. -/
theorem coordinateSwap_involutive {α β : Type} (p : α × β) :
    coordinateSwap (coordinateSwap p) = p := by
  cases p
  rfl

/-- The earlier candidate pair is sent exactly to `(3,2)`. -/
theorem swap_two_three :
    coordinateSwap ((2, 3) : Nat × Nat) = (3, 2) := by
  rfl

/-- Swapping `(3,2)` returns `(2,3)`. -/
theorem swap_three_two :
    coordinateSwap ((3, 2) : Nat × Nat) = (2, 3) := by
  rfl

/-- The two objects are different as ordered pairs. -/
theorem two_three_ne_three_two :
    ((2, 3) : Nat × Nat) ≠ (3, 2) := by
  decide

/-- Two pairs are in the same two-point orbit when one equals the other
    directly or after coordinate exchange. -/
def sameUpToSwap {α : Type} (p q : α × α) : Prop :=
  q = p ∨ q = coordinateSwap p

/-- `(2,3)` and `(3,2)` are in the same coordinate-swap orbit. -/
theorem two_three_sameUpToSwap_three_two :
    sameUpToSwap ((2, 3) : Nat × Nat) (3, 2) := by
  right
  rfl

/-- The orbit relation also holds in the reverse direction. -/
theorem three_two_sameUpToSwap_two_three :
    sameUpToSwap ((3, 2) : Nat × Nat) (2, 3) := by
  right
  rfl

/-- Named constants make the intended SAW-1 interpretation explicit without
    claiming that Lean proves any historical or psychological provenance. -/
def cyberneticCandidate : Nat × Nat := (2, 3)

def pettiniSignature : Nat × Nat := (3, 2)

/-- Conditional mathematical core of the proposed extension:
    if the earlier lyric feature is parsed as `(2,3)`, coordinate exchange
    produces the same ordered pair used by the Pettini signature. -/
theorem cybernetic_swap_matches_pettini :
    coordinateSwap cyberneticCandidate = pettiniSignature := by
  rfl

end SAW1
