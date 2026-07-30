import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel1FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel1FlatComponentChunk43

end RHP2Bridge
