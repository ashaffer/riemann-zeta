import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel1FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel1FlatComponentChunk25

end RHP2Bridge
