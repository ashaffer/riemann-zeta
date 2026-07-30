import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel1FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel1FlatComponentChunk27

end RHP2Bridge
