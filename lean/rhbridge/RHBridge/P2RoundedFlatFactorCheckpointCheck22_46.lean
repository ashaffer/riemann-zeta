import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel22FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel22FlatComponentChunk46

end RHP2Bridge
