import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel0FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel0FlatComponentChunk46

end RHP2Bridge
