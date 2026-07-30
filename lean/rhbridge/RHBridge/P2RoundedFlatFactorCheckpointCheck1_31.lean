import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel1FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel1FlatComponentChunk31

end RHP2Bridge
