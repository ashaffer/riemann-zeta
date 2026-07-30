import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel23FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel23FlatComponentChunk24

end RHP2Bridge
