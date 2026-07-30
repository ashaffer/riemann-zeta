import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel24FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel24FlatComponentChunk25

end RHP2Bridge
