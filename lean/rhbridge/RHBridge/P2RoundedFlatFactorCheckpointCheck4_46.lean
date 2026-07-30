import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel4FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel4FlatComponentChunk46

end RHP2Bridge
