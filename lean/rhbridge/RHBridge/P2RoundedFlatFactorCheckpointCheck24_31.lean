import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel24FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel24FlatComponentChunk31

end RHP2Bridge
