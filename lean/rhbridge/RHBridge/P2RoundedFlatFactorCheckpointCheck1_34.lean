import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel1FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel1FlatComponentChunk34

end RHP2Bridge
