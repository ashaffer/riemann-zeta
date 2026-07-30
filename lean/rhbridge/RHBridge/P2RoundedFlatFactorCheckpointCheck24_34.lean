import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel24FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel24FlatComponentChunk34

end RHP2Bridge
