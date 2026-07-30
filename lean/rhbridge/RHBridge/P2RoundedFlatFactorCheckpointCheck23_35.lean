import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel23FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel23FlatComponentChunk35

end RHP2Bridge
