import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel0FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel0FlatComponentChunk35

end RHP2Bridge
