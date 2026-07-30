import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel8FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel8FlatComponentChunk29

end RHP2Bridge
