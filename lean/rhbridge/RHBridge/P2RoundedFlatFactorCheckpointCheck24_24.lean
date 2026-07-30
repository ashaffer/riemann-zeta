import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel24FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel24FlatComponentChunk24

end RHP2Bridge
