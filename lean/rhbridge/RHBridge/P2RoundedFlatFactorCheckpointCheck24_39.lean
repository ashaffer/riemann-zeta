import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel24FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel24FlatComponentChunk39

end RHP2Bridge
