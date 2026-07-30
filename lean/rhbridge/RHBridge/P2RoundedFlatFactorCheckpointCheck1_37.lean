import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel1FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel1FlatComponentChunk37

end RHP2Bridge
