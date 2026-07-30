import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel1FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel1FlatComponentChunk35

end RHP2Bridge
