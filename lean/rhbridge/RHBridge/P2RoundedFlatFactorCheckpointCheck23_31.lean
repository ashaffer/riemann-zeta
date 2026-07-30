import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel23FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel23FlatComponentChunk31

end RHP2Bridge
