import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel1FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel1FlatComponentChunk33

end RHP2Bridge
