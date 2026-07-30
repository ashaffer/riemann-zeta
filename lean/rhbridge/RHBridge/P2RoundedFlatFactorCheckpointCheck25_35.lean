import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel25FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel25FlatComponentChunk35

end RHP2Bridge
