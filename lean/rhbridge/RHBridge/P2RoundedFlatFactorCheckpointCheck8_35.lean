import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel8FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel8FlatComponentChunk35

end RHP2Bridge
