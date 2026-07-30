import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel24FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel24FlatComponentChunk33

end RHP2Bridge
