import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel20FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel20FlatComponentChunk35

end RHP2Bridge
