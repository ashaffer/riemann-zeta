import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel24FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel24FlatComponentChunk47

end RHP2Bridge
