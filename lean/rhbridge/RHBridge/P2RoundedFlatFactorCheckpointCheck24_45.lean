import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel24FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel24FlatComponentChunk45

end RHP2Bridge
