import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel24FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel24FlatComponentChunk30

end RHP2Bridge
