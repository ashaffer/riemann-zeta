import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel24FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel24FlatComponentChunk36

end RHP2Bridge
