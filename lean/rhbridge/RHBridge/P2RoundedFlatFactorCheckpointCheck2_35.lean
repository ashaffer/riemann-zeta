import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel2FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel2FlatComponentChunk35

end RHP2Bridge
