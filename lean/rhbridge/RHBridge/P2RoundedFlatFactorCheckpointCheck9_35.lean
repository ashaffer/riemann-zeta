import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel9FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel9FlatComponentChunk35

end RHP2Bridge
