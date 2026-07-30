import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel1FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel1FlatComponentChunk47

end RHP2Bridge
