import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel15FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel15FlatComponentChunk35

end RHP2Bridge
