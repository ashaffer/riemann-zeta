import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel24FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel24FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel24FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel24TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel24FlatComponentChunk35

end RHP2Bridge
