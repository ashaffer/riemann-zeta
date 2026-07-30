import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel0FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel0FlatComponentChunk26

end RHP2Bridge
