import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel0FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel0FlatComponentChunk44

end RHP2Bridge
