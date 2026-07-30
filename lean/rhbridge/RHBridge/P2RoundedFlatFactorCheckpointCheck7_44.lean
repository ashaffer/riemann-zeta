import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel7FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel7FlatComponentChunk44

end RHP2Bridge
