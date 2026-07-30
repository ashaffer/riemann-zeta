import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel22FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel22FlatComponentChunk35

end RHP2Bridge
