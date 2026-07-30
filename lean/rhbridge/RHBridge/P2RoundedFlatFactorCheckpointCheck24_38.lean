import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel24FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel24FlatComponentChunk38

end RHP2Bridge
