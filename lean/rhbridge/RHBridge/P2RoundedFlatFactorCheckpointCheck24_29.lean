import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel24FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel24FlatComponentChunk29

end RHP2Bridge
