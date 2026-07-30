import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel7FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel7FlatComponentChunk46

end RHP2Bridge
