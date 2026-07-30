import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel24FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel24FlatComponentChunk27

end RHP2Bridge
