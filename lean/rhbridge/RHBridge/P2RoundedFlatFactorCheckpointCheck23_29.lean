import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel23FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel23FlatComponentChunk29

end RHP2Bridge
